from github import Github
from datatypes import RepoInfo
from typing import Optional
from datetime import datetime
from pytz import UTC
import os


# GitHub Related Utils
def get_github() -> Github:
	return Github(os.getenv("GITHUB_ACCESS_TOKEN"))


def get_user(github_username):
	try:
		usr = get_github().get_user(github_username)
	except Exception as e:
		return None


def get_repo_id(repo_url):
	if repo_url.endswith('.git'):
		repo_url = repo_url[:-4]
	return repo_url.rstrip('/').split("github.com/")[1]


def parse_commit_datetime(datetime_str) -> datetime:
	format = "%Y-%m-%dT%H:%M:%SZ"
	alternate_format = "%a, %d %b %Y %H:%M:%S %Z"
	return UTC.localize(datetime.strptime(datetime_str, format))


def get_repo_info(repo_url) -> Optional[RepoInfo]:
	repo_id = get_repo_id(repo_url)
	try:
		repo = get_github().get_repo(repo_id)
		commits = list(repo.get_commits())

		for commit in commits:
			datetime_str = commit.raw_data['commit']['author']['date']
			commit.last_modified_datetime = parse_commit_datetime(datetime_str)

		return RepoInfo(repo, commits)

	except Exception as e:
		print(e)
		return None

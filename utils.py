from github import Github
import os
from checks import BaseChecker
from typing import Tuple, List, Type

# GitHub Related Utils
ghub = Github(os.getenv("GITHUB_ACCESS_TOKEN"))


def get_user(github_username):
	try:
		usr = ghub.get_user(github_username)
	except Exception as e:
		return None


def get_repo_id(repo_url):
	if repo_url.endswith('.git'):
		repo_url = repo_url[:-4]
	return repo_url.rstrip('/').split("github.com/")[1]


# Datatype related utils
def get_all_registered_checks() -> List[Tuple[property, Type[BaseChecker]]]:
	subclasses = BaseChecker.__subclasses__()
	return [(cls.check_name, cls) for cls in subclasses]

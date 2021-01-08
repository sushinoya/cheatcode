from checks.base import BaseChecker
from datatypes import Submission, HackathonConfig, RepoInfo
from typing import Tuple, Optional


class CommitOnlyDuringHackathonChecker(BaseChecker):
	check_name = "commit_only_during_hackathon"

	@staticmethod
	def perform_check(submission: Submission, config: HackathonConfig, repo_info: RepoInfo) -> Tuple[bool, Optional[str]]:
		sorted_commits = sorted(repo_info.commits, key=lambda c: c.last_modified_datetime)
		last_commit_before_hackathon_started, first_commit_after_hackathon_ended = None, None

		for commit in sorted_commits:
			if commit.last_modified_datetime < config.start_at:
				last_commit_before_hackathon_started = commit

			if commit.last_modified_datetime > config.end_at:
				first_commit_after_hackathon_ended = commit
				break

		if not last_commit_before_hackathon_started and not first_commit_after_hackathon_ended:
			return True, None

		remarks = ""

		if last_commit_before_hackathon_started is not None:
			remarks += f"The last commit before the hackathon is {last_commit_before_hackathon_started.html_url}\n"

		if first_commit_after_hackathon_ended is not None:
			remarks += f"The first commit after the hackathon is {first_commit_after_hackathon_ended.html_url}"

		return False, remarks

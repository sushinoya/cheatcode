from checks.base import BaseChecker
from datatypes import Submission, HackathonConfig, RepoInfo
from typing import Tuple, Optional


class RepoNotForkedChecker(BaseChecker):
	check_name = "repo_not_forked"

	@staticmethod
	def perform_check(submission: Submission, config: HackathonConfig, repo_info: RepoInfo) -> Tuple[bool, Optional[str]]:
		if not repo_info.repo.parent:
			return True, None

		return False, f"Project was forked from {repo_info.repo.parent}"

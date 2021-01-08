from checks.base import BaseChecker
from datatypes import Submission, HackathonConfig
from typing import Tuple, Optional


class RepoNotForkedChecker(BaseChecker):
	check_name = "repo_not_forked"

	@staticmethod
	def perform_check(submission: Submission, config: HackathonConfig) -> Tuple[bool, Optional[str]]:
		# TODO Implement check method
		return True, "We won"

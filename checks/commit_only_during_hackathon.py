from checks.base import BaseChecker
from datatypes import Submission, HackathonConfig
from typing import Tuple, Optional


class CommitOnlyDuringHackathonChecker(BaseChecker):
	check_name = "commit_only_during_hackathon"

	@staticmethod
	def perform_check(submission: Submission, config: HackathonConfig) -> Tuple[bool, Optional[str]]:
		# TODO Implement check method
		return True, "Committed only during hackathon"

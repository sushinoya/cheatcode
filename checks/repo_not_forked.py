from checks.base import BaseChecker
from datatypes import Submission


class RepoNotForkedChecker(BaseChecker):
	check_name = "repo_not_forked"

	@staticmethod
	def perform_check(submission: Submission) -> bool:
		# TODO Implement check method
		pass

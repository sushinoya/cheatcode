from checks.base import BaseChecker
from datatypes import Submission, HackathonConfig, RepoInfo
from typing import Tuple, Optional


class SourceCodeSimilarityChecker(BaseChecker):
    check_name = "source_code_not_similar_to_other_user_project"

    @staticmethod
    def perform_check(submission: Submission, config: HackathonConfig, repo_info: RepoInfo) -> Tuple[bool, Optional[str]]:
        # TODO Implement check method
        return True, "Not Similar"

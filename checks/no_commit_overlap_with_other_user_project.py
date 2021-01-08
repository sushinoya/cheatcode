from checks.base import BaseChecker
from datatypes import Submission, HackathonConfig, RepoInfo
from typing import Tuple, Optional


class NoCommitOverlapWithOtherUserProjectChecker(BaseChecker):
    check_name = "no_commit_overlap_with_other_user_project"

    @staticmethod
    def perform_check(submission: Submission, config: HackathonConfig, repo_info: RepoInfo) -> Tuple[
        bool, Optional[str]]:
        # TODO Implement check method
        return True, "No commit overlap with other projects found"

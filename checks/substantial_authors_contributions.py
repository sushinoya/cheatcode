from checks.base import BaseChecker
from datatypes import Submission, HackathonConfig, RepoInfo
from typing import Tuple, Optional


class SubstantialAuthorsContributionsChecker(BaseChecker):
    check_name = "substantial_authors_contributions"

    @staticmethod
    def perform_check(submission: Submission, config: HackathonConfig, repo_info: RepoInfo) -> Tuple[bool, Optional[str]]:
        num_commits = len(repo_info.commits)

        if num_commits > 5:
            return True, None

        return False, f"This project only has {num_commits} commits"

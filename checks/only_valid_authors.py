from checks.base import BaseChecker
from datatypes import Submission, HackathonConfig, RepoInfo
from typing import Tuple, Optional


class OnlyValidAuthorsChecker(BaseChecker):
    check_name = "only_valid_authors"

    @staticmethod
    def perform_check(submission: Submission, config: HackathonConfig, repo_info: RepoInfo) -> Tuple[bool, Optional[str]]:
        contributors = {commit.author.login for commit in repo_info.commits}
        expected_contributors = set(submission.authors)

        if contributors == expected_contributors:
            return True, None
        elif contributors.issubset(expected_contributors):
            people_who_didnt_contribute = ", ".join(expected_contributors - contributors)
            return True, f"{people_who_didnt_contribute} did not commit anything"
        else:
            expected_contributors_names = ", ".join(expected_contributors)
            actual_contributors_names = ", ".join(contributors)
            return False, f"Expected {expected_contributors_names} to author commits but instead {actual_contributors_names} did"
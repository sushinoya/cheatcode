from abc import ABCMeta, abstractmethod
from datatypes import Submission, HackathonConfig, RepoInfo
from typing import Tuple, Optional


class BaseChecker(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def perform_check(submission: Submission, config: HackathonConfig, repo_info: RepoInfo) -> Tuple[bool, Optional[str]]:
        raise NotImplementedError

    @property
    def check_name(self) -> str:
        raise NotImplementedError

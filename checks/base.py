from abc import ABCMeta, abstractmethod
from datatypes import Submission, HackathonConfig
from typing import Tuple, Optional


class BaseChecker(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def perform_check(submission: Submission, config: HackathonConfig) -> Tuple[bool, Optional[str]]:
        raise NotImplementedError

    @property
    def check_name(self) -> str:
        raise NotImplementedError

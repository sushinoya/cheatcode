from abc import ABCMeta, abstractmethod


class BaseChecker(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def perform_check(self) -> bool:
        pass

    @property
    def check_name(self) -> str:
        raise NotImplementedError

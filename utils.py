from checks import BaseChecker
from typing import Tuple, List, Type


# Datatype related utils
def get_all_registered_checks() -> List[Tuple[property, Type[BaseChecker]]]:
	subclasses = BaseChecker.__subclasses__()
	return [(cls.check_name, cls) for cls in subclasses]

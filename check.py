import yaml
from datatypes import Submission, HackathonConfig
from utils import get_all_registered_checks


def check(config_file: str):
	with open(config_file) as file:
		config_dict = yaml.full_load(file)
		hackathon_config = HackathonConfig.from_config_dict(config_dict['hackathon_config'])
		submissions = [Submission(**s) for s in config_dict['submissions']]

	for submission in submissions:
		check_submission(submission, hackathon_config)


def check_submission(submission: Submission, config: HackathonConfig):
	for check_name, checker_class in get_all_registered_checks():
		# TODO Perform check
		pass

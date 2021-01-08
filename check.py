import yaml
import csv
from datatypes import Submission, HackathonConfig
from utils import get_all_registered_checks
from typing import Dict, Union
from dataclasses import asdict


def check(config_file: str, submissions_file: str):
	with open(config_file) as cfile:
		config_dict = yaml.full_load(cfile)

	with open(submissions_file) as sfile:
		submission_rows = [row for row in csv.DictReader(sfile, delimiter="\t")]

	hackathon_config = HackathonConfig.from_config_dict(config_dict['hackathon_config'])

	check_outcomes = []

	for row in submission_rows:
		submission = Submission(row['repo_url'], row['authors'].split(','))
		check_outcomes.append(check_submission(submission, hackathon_config))

	with open('results.tsv', 'w+') as output_file:
		dict_writer = csv.DictWriter(output_file, check_outcomes[0].keys())
		dict_writer.writeheader()
		dict_writer.writerows(check_outcomes)


def check_submission(submission: Submission, config: HackathonConfig) -> Dict[Union[str, property], Union[str, bool]]:
	check_outcome = {**asdict(submission), "remarks": ""}

	for check_name, checker_class in get_all_registered_checks():
		did_pass_check, remarks = checker_class.perform_check(submission, config)
		check_outcome[check_name] = did_pass_check

		if remarks:
			check_outcome["remarks"] += f"{remarks}\n"

	return check_outcome




import yaml
import csv
from datatypes import Submission, HackathonConfig
from utils import get_all_registered_checks
from typing import Dict, Union, Optional
from dataclasses import asdict
from checks.utils import get_repo_info
from scraper.scrape import collate_submissions


def check(config_file: str, submissions_file: Optional[str]=None):
	with open(config_file) as cfile:
		config_dict = yaml.full_load(cfile)

	hackathon_config = HackathonConfig.from_config_dict(config_dict['hackathon_config'])

	if not submissions_file:
		submissions_file = "autogen_submissions.tsv"
		collate_submissions(hackathon_config.devpost_link, submissions_file)

	with open(submissions_file) as sfile:
		submission_rows = [row for row in csv.DictReader(sfile, delimiter="\t")]

	check_outcomes = []

	for row in submission_rows:
		submission = Submission(row["devpost_url"], row['repo_url'], row['authors'].split(','))

		try:
			check_outcomes.append(check_submission(submission, hackathon_config))
		except:
			break

	with open('results.tsv', 'w+') as output_file:
		dict_writer = csv.DictWriter(output_file, check_outcomes[0].keys())
		dict_writer.writeheader()
		dict_writer.writerows(check_outcomes)


def check_submission(submission: Submission, config: HackathonConfig) -> Dict[Union[str, property], Union[str, bool]]:
	check_outcome = {**asdict(submission), "remarks": ""}
	repo_info = get_repo_info(submission.repo_url)

	for check_name, checker_class in get_all_registered_checks():
		if check_name not in config.checks:
			continue

		did_pass_check, remarks = checker_class.perform_check(submission, config, repo_info)
		check_outcome[check_name] = did_pass_check

		if remarks:
			check_outcome["remarks"] += f"{remarks}\n"

	return check_outcome




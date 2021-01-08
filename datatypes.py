from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime
from github import Commit, Repository

datetime_format = "%d-%m-%Y %H:%M:%S %z"


@dataclass
class Submission:
	devpost_url: str
	repo_url: str
	authors: List[str]


@dataclass
class RepoInfo:
	repo: Repository.Repository
	commits: List[Commit.Commit]


@dataclass
class HackathonConfig:
	start_at: datetime
	end_at: datetime
	checks: List[str]
	devpost_link: Optional[str]

	@staticmethod
	def from_config_dict(config_dict: dict):
		start_at = datetime.strptime(config_dict['start_at'], datetime_format)
		end_at = datetime.strptime(config_dict['end_at'], datetime_format)
		checks = config_dict["checks"]
		devpost_link = config_dict.get("devpost_link", None)
		return HackathonConfig(start_at, end_at, checks, devpost_link)

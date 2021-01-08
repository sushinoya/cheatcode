import sys
from check import check


def show_usage():
	print("usage: main.py <config_file> optional[<submissions_file>]")
	print("Either the config file should contain a link to the hackathon's devpost page. \
		Or the user should provide a submissions file")


if __name__ == "__main__":
	if len(sys.argv) not in [2, 3]:
		show_usage()
	else:
		check(*sys.argv[1:])

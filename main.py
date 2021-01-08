import sys
from check import check


def show_usage():
	print("usage: main.py <config_file> <submissions_file>")


if __name__ == "__main__":
	if len(sys.argv) != 3:
		show_usage()
	else:
		config_file = sys.argv[1]
		submissions_file = sys.argv[2]
		check(config_file, submissions_file)

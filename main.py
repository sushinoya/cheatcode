import sys
from check import check


def show_usage():
	print("usage: main.py <config_file>")


if __name__ == "__main__":
	if len(sys.argv) != 2:
		show_usage()
	else:
		config_file = sys.argv[1]
		check(config_file)

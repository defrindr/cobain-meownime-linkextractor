import sys

# Created on 22 jan 2019
# Defri Indra M
# https://github.com/greyxploiter

if __name__ == '__main__':
	if sys.version_info[0] < 3:
		sys.stdout.write("Must be using Python 3.x\n")
		exit()
	else:
		from assets import meownime_class
		meownime_class.main()
#!/usr/bin/env python3
import fileinput
import sys; sys.path.append("..")
from lib import *


class Classy:
	def __init__(self):
		pass


def function(input):
	return False


if __name__ == '__main__':
	lines = [line.strip() for line in fileinput.input('input.txt')]
	print('Lines: {}'.format(len(lines)))

	count_valid = 0
	for line in lines:
		fields = line.split(' ')

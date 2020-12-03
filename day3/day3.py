#!/usr/bin/env python

import sys; sys.path.append("..")
from lib import prod, Map2D

def print_map(input):
	for line in input:
		print(line)
	print()

def run_slope(mapp, row_jmp, col_jmp, debug=False):
	# mappy = mappy.copy()
	row = 0
	col = 0
	trees_found = 0
	while mapp.in_bounds(row, col, wrap=(False, True)):
		# Count
		if mapp.get(row, col, wrap=(False, True)) == '#':
			trees_found += 1
		if debug:
			# WARN: only make changes on copy!
			# mapp.set(row, col, 'O', wrap=(False, True))
			# Show
			print(row, col)
			print(mapp.get(row, col, wrap=(False, True)))
			print(mapp)
		# Move
		row += row_jmp
		col += col_jmp
	return (row, col), trees_found

if __name__ == '__main__':
	mappy = Map2D()
	mappy.load_from_file('input.txt')
	print(mappy)

	# Opposite order of question
	slopes = [
		[1, 1],
		[1, 3], # e.g. right 3, down 1
		[1, 5],
		[1, 7],
		[2, 1],
	]

	all_found = []
	for slope in slopes:
		print("Slope: {}".format(slope))
		curr_pos, trees_found = run_slope(mappy, slope[0], slope[1])
		print("End position: {}".format(curr_pos))
		print("Trees found: {}".format(trees_found))
		all_found.append(trees_found)
	print()
	print(all_found)
	print(prod(all_found))

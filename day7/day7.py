#!/usr/bin/env python3
import fileinput
import sys; sys.path.append("..")
from lib import *


def look_for(tree, iwant):
	# print('look_for( tree,', iwant, ')')
	containers = set()
	for big, inside in tree.items():
		for (_, desc) in inside:
			if iwant in desc:
				containers.add(big)
	# Base case
	if len(containers) == 0:
		return []
	for new_want in containers:
		# Recursion (reduction only needed if tree has loops)
		super_containers = look_for(tree, new_want)
		containers = containers.union(super_containers)
	return containers


def count_inside(tree, look_inside):
	# print('look_for( tree,', look_inside, ')')
	inside = tree[look_inside]
	counts = [ins[0] for ins in inside]
	total_count = sum(counts)
	for (count, desc) in inside:
		# Partial base case (we assume no loops)
		if count <= 0:
			continue
		# Recursion
		sub_count = count_inside(tree, desc)
		total_count += (count * sub_count)
		# print(look_inside, total_count, '+ (', sub_count, '*', count, new_look, ')')
	# print(look_inside, 'total:', total_count)
	return total_count


def parse_tree(input_lines):
	bags = {}
	for line in lines:
		assert line[-1] == '.'
		# Remove full stop at end of each sentence
		line = line[:-1]

		fields = line.split(' contain ')
		assert len(fields) == 2, fields
		big, inside = fields
		# Drop last word of description (either 'bag' or 'bags')
		big = ' '.join(big.split(' ')[:-1])
		# Double-check input doesn't duplicate bags
		assert big not in bags, big
		bags[big] = []
		for ins in inside.split(', '):
			words = ins.split(' ')
			count = 0 if words[0] == 'no' else int(words[0])
			# Get descriptive adjectives (ignoring last word which is 'bag' or 'bags')
			assert words[-1] in ['bag', 'bags']
			desc = ' '.join(words[1:-1])
			bags[big].append((count, desc))
	return bags


# part 1: infinite recursion -> reduction -> previously seen values
# part 2: multiplication, forgot "bag."
# 93873 @ 7:50, 158493 @ 8:12
if __name__ == '__main__':
	lines = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""
# 	lines = """shiny gold bags contain 2 dark red bags.
# dark red bags contain 2 dark orange bags.
# dark orange bags contain 2 dark yellow bags.
# dark yellow bags contain 2 dark green bags.
# dark green bags contain 2 dark blue bags.
# dark blue bags contain 2 dark violet bags.
# dark violet bags contain no other bags."""
	lines = lines.split('\n')
	lines = [line.strip() for line in fileinput.input('input.txt')]
	print('Lines: {}'.format(len(lines)))

	tree = parse_tree(lines)

	iwant = 'shiny gold'
	needs = look_for(tree, iwant)
	print('Bags containing:', len(needs))

	min_bags_needed = count_inside(tree, iwant)
	print('Bags inside:', min_bags_needed)

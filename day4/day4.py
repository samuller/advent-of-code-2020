#!/usr/bin/env python
import sys; sys.path.append("..")
from lib import prod, Map2D, wrap
import re


def byr(val):
	# byr (Birth Year) - four digits; at least 1920 and at most 2002.
	val = int(val)
	if not (1920 <= val <= 2002):
		return False
	return True

def iyr(val):
	# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
	val = int(val)
	if not (2010 <= val <= 2020):
		return False
	return True

def eyr(val):
	# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
	val = int(val)
	if not (2020 <= val <= 2030):
		return False
	return True

def hgt(val):
	# hgt (Height) - a number followed by either cm or in:
	#     If cm, the number must be at least 150 and at most 193.
	#     If in, the number must be at least 59 and at most 76.
	if len(val) <= 2:
		return False
	unit = val[-2:]
	if unit not in ['in', 'cm']:
		return False
	val = int(val[:-2])
	if unit == 'cm' and not (150 <= val <= 193):
		return False
	if unit == 'in' and not (59 <= val <= 76):
		return False
	return True

def hcl(val):
	# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
	# if len(val) != 7 or val[0] != '#':
	# 	return False
	if not re.match("^#[a-f0-9]{6}$", val):
		return False
	return True

def ecl(val):
	# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
	if val not in ['amb','blu','brn','gry','grn','hzl','oth']:
		return False
	return True

def pid(val):
	# pid (Passport ID) - a nine-digit number, including leading zeroes.
	if len(val) != 9 or not re.match("^[0-9]+$", val):
		return False
	return True

def cid(val):
	# cid (Country ID) - ignored, missing or not.
	return True


def check_field_value(key, val):
	# Dirty switch-case/dict-to-func workaround
	if not eval(key + '(val)'):
		return False
	return True


# ['byr','iyr','eyr','hgt','hcl','ecl','pid','cid']
def check_passport(full_fields, debug=False):
	fields_found = []
	for field in full_fields:
		assert(len(field.split(':')) == 2)
		key, val = field.split(':')
		assert(len(key) == 3)
		fields_found.append(key)

		if not check_field_value(key, val):
			return False

	if 'cid' in fields_found:
				fields_found.remove('cid') #optional
	# print(len(curr_fields_found))
	assert(len(set(fields_found)) == len(fields_found) )
	if sorted(fields_found) == \
		sorted(['byr','iyr','eyr','hgt','hcl','ecl','pid']):
		if debug:
			print(idx)
			print(fields_found)
			print(sorted(fields_found))
			print(sorted(['byr','iyr','eyr','hgt','hcl','ecl','pid']))
			print()
		return True
	return False


# 181, 182 / 110, 110, 112, 111 (5min), 109
# bugs:
# - part 1: last count
# - part 2: iyr copy-paste range / hgt elif unit / hcl a-z / pid and/or
if __name__ == '__main__':
	# Line-based (day 1,2)
	input_file = open('input.txt','r')
	lines = [line.strip() for line in input_file.readlines()]
	print('Lines: {}'.format(len(lines)))

	# curr_passport
	curr_full_fields = []
	valid_passports = 0
	for idx, line in enumerate(lines):
		if line.strip() == '':
			# process prev. passport
			if check_passport(curr_full_fields):
				valid_passports += 1

			# new passport
			curr_full_fields = []
		else:
			for field in line.split(' '):
				assert(len(field.split(':')) == 2)
				key, val = field.split(':')
				assert(len(key) == 3)
				curr_full_fields.append(field)

	if check_passport(curr_full_fields):
		valid_passports += 1
	print(valid_passports)

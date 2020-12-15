#!/usr/bin/env python3
import fileinput
# from collections import defaultdict


def build_history(history, curr_number, curr_pos):
	if curr_number in history:
		# Remember only last 2 numbers
		prev_numbers = history[curr_number]
		history[curr_number][0] = prev_numbers[-1]
		history[curr_number][1] = curr_pos
	else:
		# Store our only value as second/last number, then we only
		# need to remember the last number in the future
		history[curr_number] = [None, curr_pos]
	return history


def first_in_history(history, curr_number):
	assert curr_number in history
	return history[curr_number][0] is None


def diffs_in_history_pos(history, curr_number):
	prev_numbers = history[curr_number]
	return prev_numbers[-1] - prev_numbers[-2]


def play_game(first_numbers, end_count):
	times_spoken = {}
	for idx, number in enumerate(first_numbers):
		pos = idx + 1
		history = build_history(times_spoken, number, pos)
	# print(times_spoken)

	count = len(first_numbers) + 1
	last_number = first_numbers[-1]
	while count < end_count+1:
		speak_number = None
		if first_in_history(times_spoken, last_number):
			speak_number = 0
		else:
			speak_number = diffs_in_history_pos(history, last_number)

		# print('last:', last_number, times_spoken[last_number])
		# print(count, speak_number) #, times_spoken)
		history = build_history(times_spoken, speak_number, count)
		last_number = speak_number
		count += 1
	# print(count-1, speak_number) #, times_spoken)
	return speak_number


def run_tests(lines):
	end_count = int(lines[0])
	print('Running tests till {}...'.format(end_count))
	lines = lines[1:]
	for idx, line in enumerate(lines):
		ans, input = line.split('\t')
		ans = int(ans)
		numbers = [int(n) for n in input.split(',')]
		print(ans, input)
		res = play_game(numbers, end_count)
		assert res == ans, 'Test {} failed with {} instead of {}'.format(idx, res, ans)


if __name__ == '__main__':
	lines = [line.strip() for line in fileinput.input()]
	# lines = ['0,3,6']
	print('Lines: {}'.format(len(lines)))

	if len(lines) > 1:
		run_tests(lines)
		exit()

	numbers = [int(n) for n in lines[0].split(',')]
	print(play_game(numbers, 2020))
	print(play_game(numbers, 30000000))

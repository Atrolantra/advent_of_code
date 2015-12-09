#!/usr/bin/python

with open('day1input.txt') as directions:
	floor = 0
	instruction = 0
	while True:
		direction = directions.read(1)
		if not direction:
			print "Reached end. Doesn't get to basement."
			break
		instruction += 1
		if direction == '(':
			floor += 1
		elif direction == ')':
			floor -= 1
		if floor < 0:
			print instruction
			break
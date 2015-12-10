#!/usr/bin/python
# Location as a 2d coordinate (x, y).
location = [0, 0]
houses_delivered = [[0, 0]]
with open('day3input.txt') as directions:
	while True:
		direction = directions.read(1)
		if not direction:
			print "Delivered to %i" %len(houses_delivered) 
			break
		if direction == '^':
			location[1] += 1
		elif direction == 'v':
			location[1] -= 1
		elif direction == '<':
			location[0] -= 1
		elif direction == '>':
			location[0] += 1
		if (location not in houses_delivered):

			houses_delivered.append(location[:])

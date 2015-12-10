#!/usr/bin/python

# Location as a 2d coordinate (x, y).
santa_location = [0, 0]
robo_santa_location = [0, 0]

houses_delivered = [[0, 0]]

turn_counter = 1
with open('day3input.txt') as directions:
	while True:
		direction = directions.read(1)
		if not direction:
			print "Delivered to %i" %len(houses_delivered) 
			break
			
		if turn_counter % 2 == 0:
			location = santa_location
		else:
			location = robo_santa_location

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
		turn_counter += 1

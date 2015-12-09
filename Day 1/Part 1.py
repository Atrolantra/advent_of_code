#!/usr/bin/python

with open('day1input.txt') as directions:
	floor = 0
	while True:
	    direction = directions.read(1)
	    if not direction:
	    	print "Floor is %s" % floor
	    	break
	    if direction == '(':
	    	floor += 1
	    elif direction == ')':
			floor -= 1


    


#!/usr/bin/python
data = open('day5input.txt').read().splitlines()
nice = 0

def checkDubbsPair(string):
	pairs = [string[index] + string[index + 1] for index in range(len(string) - 1)]
	for pair in pairs:
		if pairs.count(pair) >= 2:
			temp_replaced = string[:]
			temp_replaced = temp_replaced.replace(pair, '--', 1)
			if temp_replaced.count(pair) >= 1:
				return True
	return False

def checkDubbsGap(string):
	for index in range(len(string) - 2):
		if string[index] == string[index + 2]:
			return True
	return False

for string in data:

	# Check for double letters with one letter gap.
	if not checkDubbsPair(string):
		continue

	# Check if double pair requirements are met.
	if not checkDubbsGap(string):
		continue

	# Finally, if it got to here it passed the tests. 
	# Increase the nice string list.
	nice += 1

print nice

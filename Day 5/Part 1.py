#!/usr/bin/python
data = open('day5input.txt').read().splitlines()
nice = 0
vowels = 'aeiou'
bad_strings = ["ab", "cd", "pq", "xy"]

def checkVowels(string, vowels):
	vowel_count = 0
	for letter in string:
		if letter in vowels:
			vowel_count += 1
		# As soon as we get at least 3 vowels continue on to not waste time.
		if vowel_count >= 3:
			return True
	return False

def checkDubbs(string):
	for index in range(len(string) - 1):
		if string[index] == string[index + 1]:
			return True
	return False

def checkIsBad(string, bad_strings):
	for bad in bad_strings:
		if bad in string:
			return True

	return False

for string in data:
	
	# Check for vowel requirements.
	if not checkVowels(string, vowels):
		continue

	# Check for double letters.
	if not checkDubbs(string):
		continue
	
	# Check for bad substrings.
	if checkIsBad(string, bad_strings):
		continue

	# Finally, if it got to here it passed the tests. 
	# Increase the nice string list.
	nice += 1

print nice
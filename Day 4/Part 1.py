#!/usr/bin/python
# Lowest number that can combine with bgvyzdsv and has an MD5 hash starting with 5 0s in hex
import hashlib

mystring = "bgvyzdsv"
number = 0



while (hashlib.md5(mystring + str(number)).hexdigest()[:5] != "00000"):
	number += 1
print number

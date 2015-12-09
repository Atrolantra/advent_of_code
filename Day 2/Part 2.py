#!/usr/bin/python
import itertools
import operator

paper_total = 0
data = open('day2input.txt').read().splitlines()


def getdim(rectangle):
	l, w, h = rectangle.split('x')
	return (int(l), int(w), int(h))

def getSurfaceAreas(dimensions):
	# Calculate and return a list of all three face areas.
	face_area = [pair[0] * pair[1] for pair in itertools.combinations(dimensions, 2)]
	return face_area

def prod(iterable):
    return reduce(operator.mul, iterable, 1)

for present in data:
	dimensions = getdim(present)
	face_areas = getSurfaceAreas(dimensions)
	volume = prod(dimensions)
	perimeter = sum(2 * sorted(dimensions)[x] for x in range(2))
	# perimeter = 2 * sorted(dimensions)[0] + 2 * sorted(dimensions)[0]
	paper_total += (perimeter + volume)
print paper_total

	
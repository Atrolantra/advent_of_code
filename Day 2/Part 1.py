#!/usr/bin/python
import itertools

paper_total = 0
data = open('day2input.txt').read().splitlines()


def getdim(rectangle):
	l, w, h = rectangle.split('x')
	return (int(l), int(w), int(h))

def getSurfaceAreas(dimensions):
	# Calculate and return a list of all three face areas.
	face_area = [pair[0] * pair[1] for pair in itertools.combinations(dimensions, 2)]
	return face_area


for present in data:
	dimensions = getdim(present)
	face_areas = getSurfaceAreas(dimensions)
	surface_area = sum(2*face for face in face_areas)
	surface_area += min(face_areas)
	paper_total += surface_area
print paper_total

	
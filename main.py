import random

cmaj = ["C", "D", "E", "F", "G", "A", "B", "rest"]

def melodize(key,bars):
	c = 0
	length = bars
	if key == "cmaj":
		scale = cmaj

	while(c <= bars):
		x = random.randrange(0,7)
		note = scale[x]
		y = random.randrange(0, 3)
		print(str(note))
		c += 1/4

		if bars % 4 == 0:
			print("\n")

melodize("cmaj", 4)

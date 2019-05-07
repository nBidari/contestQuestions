t = 1
h = int(input(""))
m = int(input(""))

altitude = 0

while t != m:
	altitude = (-6 * (t*t*t*t)) + (h * (t*t*t)) + (2 * (t*t)) + t

	print(altitude)
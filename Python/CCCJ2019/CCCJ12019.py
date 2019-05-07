a3 = int(input(""))
a2 = int(input(""))
a = int(input(""))

b3 = int(input(""))
b2 = int(input(""))
b = int(input(""))

aTotal = (a3*3) + (a2*2) + a
bTotal = (b3*3) + (b2*2) + b

if aTotal > bTotal:
	print("A")
elif bTotal > aTotal:
	print("B")
else:
	print("T")
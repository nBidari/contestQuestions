a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a - b < 0 and b - c < 0 and c - d < 0:
	print("Fish Rising")
elif a - b > 0 and b - c > 0 and c - d > 0:
	print("Fish Diving")
elif a == b and b == c and c == d:
	print("Fish At Constant Depth")
else:
	print("No Fish")
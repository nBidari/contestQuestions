y1 = input("")
y2 = int(y1)

distNums = False
yChar = ""

while distNums == False:
	y2 += 1

	for i in range(len(y1)):
		yChar = y1[i]

		for m in range(len(y1)):
		 	if i == m:
		 		distNums = False
		 	elif yChar == y1[i]:
		 		distNums = False
		 	else:
		 		distNums = True

print(str(y2))
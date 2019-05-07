numQ = int(input(""))
outputList = []

for i in range(0,numQ):
	encodeStr = input("")

	if (encodeStr[1] == " "):
		outputList.append(encodeStr[2] * int(encodeStr[0]))
	else:
		outputList.append(encodeStr[3] * int(encodeStr[0:2]))

for k in range(0,numQ):
	print(outputList[k])
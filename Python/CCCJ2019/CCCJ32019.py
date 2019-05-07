numQ = int(input(""))
outputList = []



for i in range(0,numQ):
	encodeStr = input("")

	#Seperate Substring and Count them
	count = 0
	subStrings = []
	subString = ""

	for l in range(len(encodeStr)):
		if l != len(encodeStr)-1:
			if l != 0:
				if encodeStr[l] == encodeStr[l-1]:
					subString += encodeStr[l]
					count += 1
				else:
					subStrings.append([subString,count])

					subString = ""
					count = 0

					subString += encodeStr[l]
					count += 1
					#print(encodeStr[l] + " " + str(count) + " " + str(subStrings))
			else:
				subString += encodeStr[l]
				count += 1
		else:
			if encodeStr[l] == encodeStr[l-1]:
				subString += encodeStr[l]
				count += 1

				subStrings.append([subString,count])
			else:
				subStrings.append([subString,count])

				subStrings.append([encodeStr[l],1])
	outputList.append(subStrings)

for m in range(len(outputList)):
	outputStr = ""
	for n in range(len(outputList[m])):
		outputStr += str(outputList[m][n][1]) + " " + str(outputList[m][n][0][0]) + " "
	print(outputStr)


#for k in range(0,numQ):
#	print(outputList[k])
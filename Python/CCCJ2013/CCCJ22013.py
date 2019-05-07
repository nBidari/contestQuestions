inputStr = input("")

usableChars = ["I","O","S","H","Z","X","N"]
nonoLetters = False

for i in range(len(inputStr)):
	if inputStr[i] == "I" or inputStr[i] == "O" or inputStr[i] == "S" or inputStr[i] == "H" or inputStr[i] == "Z" or inputStr[i] == "X" or inputStr[i] == "N":
		pass
	else:
		nonoLetters = True

if nonoLetters == True:
	print("NO")
else:
	print("YES")
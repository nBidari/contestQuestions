voteNum = int(input(""))
votes = input("")

aCnt = 0
bCnt = 0

for i in range(len(votes)):
	if votes[i] == "A":
		aCnt += 1
	else:
		bCnt += 1
if aCnt > bCnt :
	print("A")
elif bCnt > aCnt:
	print("B")
else:
	print("Tie")
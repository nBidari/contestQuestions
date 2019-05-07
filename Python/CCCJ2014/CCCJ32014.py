n = int(input(""))
nCnt = 0

antScore = 100
davScore = 100

while nCnt != n:
	nCnt += 1

	roundScore = input("")

	ant = int(roundScore[0])
	dav = int(roundScore[2])

	if ant > dav:
		davScore -= ant
	elif dav > ant:
		antScore -= dav


print(antScore)
print(davScore)
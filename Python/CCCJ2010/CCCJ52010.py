board=[
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],
	]

atEnd = False
minMoves = 0

pos1 = input("")
kPos = [int(pos1[0]),int(pos1[2])]
pos2 = input("")
endPos = [int(pos2[0]),int(pos2[2])]

def lMove(x,y):

#while atEnd == False:
board[-kPos[1]][kPos[0]-1] = 1

for i in range(len(board)):
	print(board[i])

if kPos == endPos:
	atEnd == True

	
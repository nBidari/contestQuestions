grid = [["1","2"],
		["3","4"]
	]

def hFlip():
	newGrid = [[0,0],[0,0]]

	newGrid[0][0] = grid[1][0]
	newGrid[0][1] = grid[1][1]
	newGrid[1][0] = grid[0][0]
	newGrid[1][1] = grid[0][1]

	return newGrid

def vFlip():
	newGrid = [[0,0],[0,0]]

	newGrid[0][0] = grid[0][1]
	newGrid[0][1] = grid[0][0]
	newGrid[1][0] = grid[1][1]
	newGrid[1][1] = grid[1][0]

	return newGrid


instructions = input("")

for i in range(len(instructions)):
	if instructions[i] == "V":
		grid = vFlip()
	else:
		grid = hFlip()


print(grid[0][0] + " " + grid[0][1])
print(grid[1][0] + " " + grid[1][1])
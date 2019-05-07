sub1 = input("").split()
sub2 = input("").split()
sub3 = input("").split()

subs = [[sub1[0],sub1[1]],
		[sub2[0],sub2[1]],
		[sub3[0],sub3[1]],
]

insts = input("").split()

steps = int(insts[0])
initial = insts[1]
final = insts[2]

outputStr = ""
outputList = []

count = len(outputStr)

while outputStr != initial:
	outputStr = final
	for i in range(0,steps):
		
		for l in range(len(outputStr)):
			if outputStr[l:l+2] == subs[0][1]:
				outputStr = outputStr[:l] + subs[0][0] + outputStr[l+2:]
			elif outputStr[l:l+2] == subs[1][1]:
				outputStr = outputStr[:l] + subs[1][0] + outputStr[l+2:]
			elif outputStr[l:l+2] == subs[2][1]:
				outputStr = outputStr[:l] + subs[2][0] + outputStr[l+2:]

	print(outputStr)
	outputStr = initial
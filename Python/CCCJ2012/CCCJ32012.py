icon =  [["*","x","*"],
		 [" " ,"x","x"],
		 ["*"," " ,"*"],
		]

k = int(input(""))

iLen = len(icon)

for i in range(iLen):
	for j in range(len(icon[i])):
		icon[i][j] = icon[i][j] * k

#print(icon)

for m in range(iLen):
	for n in range(0,k):
		print(icon[m])
#a>b and c>d means that they both always move forward

counter = 0

#NIKKY
a = int(input())
b = int(input())
nDist = 0
nSteps = 0

#BYRON
c = int(input())
d = int(input())
bDist = 0
bSteps = 0

#STEPS
s = int(input())


#Nikky Solution
while nSteps < s:
	nDist += a-b

	nSteps += a+b

while bSteps < s:
	bDist += c-d

	bSteps += c+d

print(nDist)
print(bDist)


if nDist > bDist:
	print("Nikky")
elif nDist < bDist:
	print("Byron")
else:
	print("Tied")

n = input("")
n = int(n)

x = input("")

t = input("")

mothMemes = 0

for i in n:
	if x[i] == t[i] and x == ".":
		mothMemes += 1

print(str(mothMemes))

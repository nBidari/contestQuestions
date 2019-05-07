cities = input().split()

for j in range(len(cities)):
	cities[j] = int(cities[j])

output = [
			["","","","",""],
			["","","","",""],
			["","","","",""],
			["","","","",""],
			["","","","",""]
		  ]

for i in range(0,6):
	output[i[0]] = cities[i] 


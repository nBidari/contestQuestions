
result = [0,0]
pointer = 0

sevenSaid = False



while sevenSaid == False:
	instruction = input("")

	
	

	if instruction[0] == "7":
		sevenSaid = True
	else:

		if (instruction[2] == "A"):
			pointer = 0;
		else:
			pointer = 1;

		if instruction[0] == "1":
			result[pointer] = instruction[4]
		elif instruction[0] == "2":
			print(x)
		else:
			if instruction[0] == "3":
				x = x+y
			elif instruction[0] == "4":
				x = x*y
			elif instruction[0] == "5":
				x = x-y
			elif instruction[0] == "6":
				x = x/y

	printer = [a,b,x,y]

	print(printer)


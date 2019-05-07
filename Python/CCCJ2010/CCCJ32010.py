
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
			result[pointer] = int(instruction[4])
		elif instruction[0] == "2":
			print(result[pointer])
		else:

			if instruction[2] == instruction[4]:
				if pointer == 0:
					if instruction[0] == "3":
						result[0] = result[0] + result[0]
					elif instruction[0] == "4":
						result[0] = result[0] * result[0]
					elif instruction[0] == "5":
						result[0] = result[0] - result[0]
					elif instruction[0] == "6":
						result[0] = result[0] / result[0]
				else:
					if instruction[0] == "3":
						result[1] = result[1] + result[1]
					elif instruction[0] == "4":
						result[1] = result[1] * result[1]
					elif instruction[0] == "5":
						result[1] = result[1] - result[1]
					elif instruction[0] == "6":
						result[1] = result[1] / result[1]
			else:
				if pointer == 0:
					if instruction[0] == "3":
						result[0] = result[0] + result[1]
					elif instruction[0] == "4":
						result[0] = result[0] * result[1]
					elif instruction[0] == "5":
						result[0] = result[0] - result[1]
					elif instruction[0] == "6":
						result[0] = result[0] / result[1]
				else:
					if instruction[0] == "3":
						result[1] = result[1] + result[0]
					elif instruction[0] == "4":
						result[1] = result[1] * result[0]
					elif instruction[0] == "5":
						result[1] = result[1] - result[0]
					elif instruction[0] == "6":
						result[1] = result[1] / result[0]

	print(result)


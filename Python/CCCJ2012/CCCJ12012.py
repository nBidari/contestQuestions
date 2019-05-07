speedlimit = int(input("Enter the speed limit: "))
speed = int(input("Enter the recorded speed of the car: "))

overLimit = speed-speedlimit

if overLimit <= 0:
	print("Congratulations, you are within the speed limit!")
elif overLimit <= 20 and overLimit >= 1:
	print("You are speeding and your fine is $100.")
elif overLimit <= 30 and overLimit >= 21:
	print("You are speeding and your fine is $270.")
elif overLimit >= 31:
	print("You are speeding and your fine is $500.")
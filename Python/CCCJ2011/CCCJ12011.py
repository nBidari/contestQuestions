print("How many antennas?")
antennas = int(input(""))

print("How many eyes?")
eyes = int(input(""))

if antennas >= 3 and eyes <= 4:
	print("TroyMartian")
elif antennas <= 6 and eyes >= 2:
	print("VladSaturnian")
elif antennas <= 2 and eyes <= 2:
	print("GraemeMercurian")
else:
	pass

from enum import Enum
import sys
import random

VERSION = "1.1"

keepGoing = True
addStyles = False

class Weapons(Enum):

	GreatSword = 1
	LongSword = 2
	SwordAndShield = 3
	DualBlades = 4
	Hammer	= 5
	HuntingHorn = 6
	Lance = 7
	GunLance = 8
	SwitchAxe = 9
	ChargeBlade = 10
	InsectGlaive = 11
	LightBowGun = 12
	HeavyBowGun = 13
	Bow = 14

class Styles(Enum):

	Striker = 1
	Guild = 2
	Adept = 3
	Aerial = 4

if len(sys.argv) < 2:

	sys.stderr.write("Error: Too few arguments, looking for player names!\n\n")
	keepGoing = False

elif sys.argv[1] == "--help":

	print("This application chooses a random weapon and style for each hunter whose name is given as arguments.\n  --help      Displays this message\n  --version   Displays the version number of this application.\n  -s          Adds hunter styles to the roll.\n")
	keepGoing = False

elif sys.argv[1] == "--version":

	print("MHG Weapon Roller version ", end="")
	print(VERSION, end="\n\n")
	keepGoing = False

elif sys.argv[1] == "-s":

	addStyles = True
	sys.argv = sys.argv[1:]

elif sys.argv[1][0] == '-':

	sys.stderr.write("Error: Unrecognized flag!\n")
	keepGoing = False

while keepGoing:

	answer = ' '

	for i in range(1, len(sys.argv)):

		print(sys.argv[i], end=": ")

		if addStyles:

			print(Styles(random.randint(1,4)).name, end=" style ")

		print(Weapons(random.randint(1, 14)).name)

	while answer != 'Y' and answer != 'y' and answer != 'n' and answer != 'N':

		answer = input("\nRoll again? ")

		if answer != 'Y' and answer != 'y' and answer != 'n' and answer != 'N':

			sys.stderr.write("Error: Enter Y or N only\n")

	if answer == 'n' or answer == 'N':

		keepGoing = False

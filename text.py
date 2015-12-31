"""Text file for all string functions to be printed in the game."""

import string

def printIntro():
	"""Prints the introduction to the game and allows the player to skip it."""
	print "Welcome to The Arena!"
	print "A game by Will Owens\n\n"
	print "Would you like to read the introduction?\n"

	while True:
		try:
			yes = ['yes','y','ye']
			no = ['no','n']
			inp = string.lower(raw_input("Type 'Y' or 'N' >>  "))
			if inp in yes:
				printStory()
				break
			elif inp in no:
				break
			else:
				print "\n%s is not a valid input.\n" % inp
				continue

		except ValueError:
			print "\n%s is not a valid input.\n" % inp
			continue

def printStory():
	print "\n\nA magnificent day has dawned in Rome. You have collected your family in your arms and weekly pay in your purse for a day of entertainment at the Colosseum.\n\nYou will have the opportunity to bet on Rome's finest gladiators! Make sure to pay attention to their equipment and the predictions of the bookmakers to get the best chances.\n\nJust remember: Luck can be a fickle woman and turn her eye on a dime.\n"
	raw_input("Press <Enter> to continue.")

def announceWarriors(warrior1,odds1,warrior2,odds2):
	print "\n\nThis battle is between %s and %s!\n" % (warrior1.getName(),warrior2.getName())
	strength, dexterity = _judgeWarrior(warrior1)
	print "\n%s looks %s and %s." % (warrior1.getName(),strength,dexterity)
	warrior1.getEquipped()
	print "\nThe bookmakers give %s %d to 1 odds.\n" % (warrior1.getName(),odds1)

	print "\n==================================================================\n"
	strength,dexterity = _judgeWarrior(warrior2)
	print "\n%s looks %s and %s." % (warrior2.getName(),strength,dexterity)
	warrior2.getEquipped()
	print "\nThe bookmakers give %s %d to 1 odds.\n" % (warrior2.getName(),odds2)

def _judgeWarrior(warrior):
	strength = warrior.getStr()
	dexterity = warrior.getDex()
	if strength < 6:
		strength = "thin"
	elif strength > 5 and strength < 14:
		strength = "average"
	elif strength > 13:
		strength = "very muscular"
	if dexterity < 6:
		dexterity = "very clumsy"
	elif dexterity > 5 and dexterity < 14:
		dexterity = "sure footed"
	elif dexterity > 13:
		dexterity = "extremely nimble"
	return strength, dexterity

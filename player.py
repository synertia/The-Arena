"""Player.py will generate a player object allowing the purse to be tracked
as well as any further record keeping to be installed later."""

from string import lower

class Player:
	def __init__(self):
		self.purse = 1000
		self.pick =""
		self.bet = 0

	def getPurse(self):
		return self.purse

	def getPick(self):
		return self.pick

	def getBet(self):
		return self.bet

	def updatePurse(self,result,bet,odds):
		if result == "win":
			self.purse += (odds * bet)
			print "\nYou won %d coins!\n" % (odds*bet)
		else:
			self.purse -= bet
			print "\nYou lost your bet of %d coins." % bet

	def getChoice(self,warrior1,warrior2):
		yes = ['yes','y','ye']
		no = ['no','n']
		print "Enter 'yes' to bet or 'no' to skip this battle."
		while True:
			try:
				choice = lower(raw_input(">> "))
				if choice in yes:
					self.pick = "yes"
					break
				elif choice in no:
					self.pick = "no"
					break
				else:
					print "\nInvalid Choice\n"
					continue
			except ValueError:
				print "\nInvalid Choice\n"
				continue

		if self.pick == "yes":
			print "Would you like to bet on %s or %s?\n" % (warrior1.getName(),warrior2.getName())
			while True:
				try:
					choice = int(raw_input("Enter '1' for %s or '2' for %s. >> " % (warrior1.getName(),warrior2.getName())))
					if choice == 1:
						self.pick = warrior1.getName()
						break
					elif choice == 2:
						self.pick = warrior2.getName()
						break
					else:
						print "\nInvalid choice. Select '1' or '2'.\n"
						continue

				except ValueError:
					print "\nInvalid choice. Select '1' or '2'.\n"
					continue


			print "\nHow much would you like to bet? (You have %d coins.)\n" % self.purse
			running = True
			while running:
				try:
					bet = int(raw_input(">> "))
					if bet < self.purse:
						print "\nBet %d coins on %s?\n" % (bet,self.pick)
						while running:
							try:
								ans = str(raw_input(">> "))
								if ans in yes:
									self.bet = bet
									running = False
								elif ans in no:
									print "\nThen bet how much?\n"
									break
								else:
									print "\nPlease answer yes or no.\n"
									continue
							except ValueError:
								print "\nPlease answer yes or no.\n"
								continue


					elif bet == self.purse:
						print "\nBet it ALL on %s?!\n" % self.pick
						while running:
							try:
								ans = str(raw_input(">> "))
								if ans in yes:
									self.bet = bet
									running = False
								elif ans in no:
									print "\nThen bet how much?\n"
									break
								else:
									print "\nPlease answer yes or no.\n"
									continue
							except ValueError:
								print "\nPlease answer yes or no.\n"
								continue

					elif bet > self.purse:
						print "\nYou don't have that many coins!\n"
						continue

				except ValueError:
					print "\nPlease enter the number of coins to bet.\n"
					continue

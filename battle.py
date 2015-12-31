"""battle.py creates a battle object using two warriors and then proceeds
round by round until one warrior is dead. It will return the winning
warrior to the main program for win comparison."""

from warrior import Warrior
from random import randrange
from announcer import Announcer

class Battle:
	def __init__(self):
		self.warrior1 = Warrior()
		self.warrior2 = Warrior()
		self.odds1, self.odds2 = self._genOdds(self.warrior1,self.warrior2)
		self.announcer = Announcer()

	def _genOdds(self,warrior1,warrior2):
		"""This helper function will determine the odds of each warrior winning based
		on the stats and equipment value of each warrior."""
		war1val = warrior1.getStats() + warrior1.getDamStat() + warrior1.getDefValue()
		war2val = warrior2.getStats() + warrior2.getDamStat() + warrior2.getDefValue()
		totodds = war1val + war2val
		return int((float(war1val)/totodds)*10), 10 - int((float(war2val)/totodds)*10)

	def getOdds(self, warrior):
		if warrior == self.warrior1:
			return self.odds1

		else:
			return self.odds2

	def battle(self):
		"""This method sets up the battle then calls the turn method to determine
		the outcome of each round and then update the warriors."""
		while self.warrior1.getHP() > 0 and self.warrior2.getHP() > 0:
			self.fightRound(self.warrior1,self.warrior2)

			if self.warrior1.getHP() <= 0:
				return self.warrior2.getName(), self.odds2
			elif self.warrior2.getHP() <= 0:
				return self.warrior2.getName(), self.odds1

	def fightRound(self,warrior1,warrior2):
		"""This method will simulate one round of combat by checking which warrior
		has higher dexterity, then seeing who got damaged how much."""
		if warrior1.getDex() > warrior2.getDex():
			self._simHit(warrior1,warrior2)
			if warrior2.getHP() <= 0:
				print
				print self.announcer.getDead(warrior2)
				return warrior1.getName(),self.odds1
				raw_input("\nPush <Enter> to continue.")
			else:
				self._simHit(warrior2,warrior1)
				if warrior1.getHP() <= 0:
					print
					print self.announcer.getDead(warrior1)
					return warrior2.getName(),self.odds2
					raw_input("\nPush <Enter> to continue.")

		else:
			self._simHit(warrior2,warrior1)
			if warrior1.getHP() <= 0:
				print
				print self.announcer.getDead(warrior1)
				return warrior2.getName(),self.odds2
				raw_input("\nPush <Enter> to continue.")
			else:
				self._simHit(warrior1,warrior2)
				if warrior2.getHP() <= 0:
					print
					print self.announcer.getDead(warrior2)
					return warrior1.getName(), self.odds1
					raw_input("\nPush <Enter> to continue.")


	def _simHit(self,warrior1,warrior2):
		"""Helper function to determine who hits first and how much damage they do.
		Critical hits and dodges occur when a 20 is rolled."""
		aroll, droll = randrange(1,21) + (warrior1.getDex() * .5), randrange(1,21) + (warrior2.getDex() * .5)

		if aroll >= 20 or droll >= 20:
			if aroll >= 20 and droll != 20:
				if warrior1.getDex() > warrior1.getStr():
					try:
						warrior2.updateHP(warrior1.getDamStat() * randrange(2,(int(warrior1.getDex()*.4))))
					except ValueError:
						warrior2.updateHP(warrior1.getDamStat()*2)
					print
					print self.announcer.getCriticalHit(warrior1,warrior2)
					raw_input("\nPush <Enter> to continue.")
				else:
					try:
						warrior2.updateHP(warrior1.getDamStat() * randrange(2,(int(warrior1.getDex()*.4))))
					except ValueError:
						warrior2.updateHP(warrior1.getDamStat()*2)
						print
						print self.announcer.getCriticalHit(warrior1,warrior2)
						raw_input("\nPush <Enter> to continue.")
			elif droll >= 20 and aroll != 20:
				warrior2.updateHP(0)
				print
				print self.announcer.getCriticalDodge(warrior1,warrior2)
				raw_input("\nPush <Enter> to continue.")
			else:
				warrior1.updateHP(int(warrior2.getDamStat()*.2))
				warrior2.updateHP(int(warrior1.getDamStat()*.2))
				print
				print self.announcer.getCriticalBoth()
				raw_input("\nPush <Enter> to continue.")

		elif aroll > droll:
			if warrior1.getDex() > warrior1.getStr():
				try:
					warrior2.updateHP(warrior1.getDamStat() * randrange(0,int(warrior1.getDex()*.2)) - randrange(0,int(warrior2.getDefValue())))
				except ValueError:
					warrior2.updateHP(warrior1.getDamStat() - randrange(0,1 + int(warrior2.getDefValue())))
				print
				print self.announcer.getHit(warrior1,warrior2)
				raw_input("\nPush <Enter> to continue.")
			else:
				try:
					warrior2.updateHP(warrior1.getDamStat() * randrange(0,int(warrior1.getStr()*.2 - randrange(0,int(warrior2.getDefValue())))))
				except ValueError:
					warrior2.updateHP(warrior1.getDamStat() - randrange(0,1 + int(warrior2.getDefValue())))
				print
				print self.announcer.getHit(warrior1,warrior2)
				raw_input("\nPush <Enter> to continue.")

		else:
			print
			print self.announcer.getDodge(warrior1,warrior2)
			raw_input("\nPush <Enter> to continue.")

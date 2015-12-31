"""warrior.py will design an individual warrior by generating his stats
and equipment based on those stats."""

from random import randrange
import string
from equipment import Weapon, Armor

class Warrior:
	def __init__(self):
		"""Establishes the two stats using the helper function _statGen"""
		stattot = 0
		self.str = self._statGen(stattot)
		self.dex = self._statGen(stattot)
		self.HP = self.getStr() * randrange(2,6)
		self.weapon = self._genWeap()
		self.armor = self._genArm()
		self.name = self._genName()
		self.damstat = self.weapon.getDam()
		self.defvalue = self._getArmor()

	def _genName(self):
		"""This helper function simply generates a name from a large list of names for the
		warrior to have."""
		namelst = []
		file = open("names.txt","r")
		for line in file:
			namelst.append(line[:-1])
		file.close()
		return namelst[randrange(1,len(namelst))]

	def _statGen(self,stattot):
		"""Helper module generates the required stat from a random range
		between 1 and 18. The likelihood of a high roll is reduced if the
		previous stat roll was very high."""
		if stattot < 15:
			stat = randrange(1,19)
			stattot += stat
			return stat

		elif stattot > 8 and stattot < 15:
			stat = randrange(1,10) + randrange(0,3)
			stattot += stat
			return stat

		elif stattot > 15:
			stat = randrange(1,8) + randrange(0,3)
			stattot += stat
			return stat

		else:
			stat = randrange(8,15) + randrange(0,3)
			stattot += stat
			return stat

	def _genWeap(self):
		"""Helper function that will create a list of weapons based on the character's
		best stat (Strength or Dexterity) allowing the warrior to have a better chance
		at winning. They may still get a crappy weapon, anyway."""
		if self.str > self.dex:
			weaplist = []
			file = open("sweapons.txt","r")
			for line in file:
				name,dam,value,desc = string.split(line,"\t")
				weaplist.append(Weapon(name,dam,value,desc))
			file.close()

			if self.str < 5:
				return weaplist[randrange(0,4)]

			elif self.str >= 5 and self.str < 12:
				return weaplist[randrange(0,7)]

			else:
				return weaplist[randrange(0,10)]

		elif self.str == self.dex:
			weaplist = []
			file = open("sweapons.txt","r")
			for line in file:
				name,dam,value,desc = string.split(line,"\t")
				weaplist.append(Weapon(name,dam,value,desc))
			file.close()

			if self.str < 5:
				return weaplist[randrange(0,4)]

			elif self.str >= 5 and self.str < 12:
				return weaplist[randrange(0,7)]

			else:
				return weaplist[randrange(0,10)]

		else:
			weaplist = []
			file = open("dweapons.txt","r")
			for line in file:
				name,dam,value,desc = string.split(line,"\t")
				weaplist.append(Weapon(name,dam,value,desc))
			file.close()

			if self.dex < 5:
				return weaplist[randrange(0,5)]

			elif self.dex >= 5 and self.dex < 12:
				return weaplist[randrange(0,8)]

			else:
				return weaplist[randrange(0,9)]

	def _genArm(self):
		"""Helper function that will create a list of armor, then randomly choose 0 to three
		pieces for the fighter to wear."""
		roll = randrange(0,8)
		armlist = []
		file = open("armor.txt","r")
		for line in file:
			name,defense,value,desc = string.split(line,"\t")
			armlist.append(Armor(name,defense,value,desc))
		file.close()

		wararm = []
		if roll == 0:
			roll = randrange(0,10)
			if roll == 0:
				wararm.append(armlist[0])
				return wararm

			else:
				return self._rollArm(armlist)

		else:
			return self._rollArm(armlist)

	def _getArmor(self):
		defvalue = 0
		for i in range(len(self.armor)):
			defvalue += eval(self.armor[i].getDef())
		return defvalue

	def _rollArm(self,list):
		feet, head, chest = randrange(1,5), randrange(5,10), randrange(10,14)
		wararm = []
		if feet == 1 and head == 5 and chest == 10:
			wararm.append(list[0])
			return wararm

		else:
			wararm.append(list[feet])
			wararm.append(list[head])
			wararm.append(list[chest])
			return wararm

	def updateHP(self,damage):
		if damage >= 0:
			self.HP -= damage
		else:
			self.HP -= 0

	def getStr(self):
		"""Returns the strength of the warrior."""
		return self.str

	def getDex(self):
		"""Returns the dexterity of the character."""
		return self.dex

	def getHP(self):
		"""Returns the HP level of the Warrior"""
		return self.HP

	def getWeapon(self):
		return self.weapon.getName()

	def getDefValue(self):
		"""Returns the raw defense value of the equipped items for calculations."""
		return self.defvalue

	def getEquipped(self):
		"""Prints the items equipped by the warrior."""
		for i in range(len(self.armor)):
			print self.armor[i].getDesc()

	def getStats(self):
		"""Returns thet total of the warrior's stats for odds calculation."""
		return self.str + self.dex + self.HP

	def getName(self):
		"""Returns the name of the warrior."""
		return self.name

	def getDamStat(self):
		"""Returns the raw damage stat of the warrior's weapons for calculations."""
		return eval(self.damstat)

	def getFull(self):
		print "Name: ",self.name
		print "HP: ", self.HP
		print "Str: ", self.str
		print "Dex: ", self.dex
		print "Weapon: ", self.getWeapon()
		print self.getEquipped()

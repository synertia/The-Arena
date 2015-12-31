"""Equipment will create manufacture the objects to be plased in the list
for choosing in the warrior module."""

class Weapon:
	"""Generates a weapon for placement in the weapon list."""
	def __init__(self,name,dam,value,desc):
		self.name = name
		self.dam = dam
		self.value = value
		self.desc = desc
		
	def getName(self):
		"""Returns the name of the weapon for descriptions."""
		return self.name
		
	def getDam(self):
		"""Returns the damage of the weapon for use in calculation."""
		return self.dam
		
	def getValue(self):
		"""Returns the attack value for odds calculation."""
		return self.value
		
	def getDesc(self):
		"""Returns a string of the description for the player."""
		return self.desc
		
class Armor:
	"""Generates armor for placement into the selection list."""
	def __init__(self,name,defense,value,desc):
		self.name = name
		self.defense = defense
		self.value = value
		self.desc = desc
		
	def getName(self):
		"""Returns the name of the armor piece for descriptions."""
		return self.name
		
	def getDef(self):
		"""Returns the defense value of the armor piece for use in calculations."""
		return self.defense
		
	def getValue(self):
		"""Returns the defense value used in odds calculation."""
		return self.value
		
	def getDesc(self):
		"""Returns the description of the armor piece for the player."""
		return self.desc
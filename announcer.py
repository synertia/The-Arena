"""Announcer.py is an announcer object to be called during combat that will
display the appropriate result of the round and each action for the player."""

import string

class Announcer:
    def __init__(self):
        self.hitCS = self._buildDict("sweaphitc.txt")
        self.hitCD = self._buildDict("dweaphitc.txt")
        self.dodgeC = self._buildDict("weapdodgec.txt")
        self.critHits = self._buildDict("crithit.txt")
        self.critDodge = self._buildDict("critdodge.txt")

    def _buildDict(self,source):
        """Helper module builds commentary dictionary from the appropriate file."""
        cdict = {}
        stuff = open(source,"r")
        for line in stuff:
            weap,comment = string.split(line,"\t")
            cdict[weap] = comment[:-1]
        stuff.close()
        return cdict

    def getHit(self,warrior1, warrior2):
        """Comments for the warrior hitting with his weapon."""
        if warrior1.getDex() > warrior1.getStr():
            return self.hitCD[warrior1.getWeapon()] % (warrior1.getName(),warrior2.getName())
        else:
            return self.hitCS[warrior1.getWeapon()] % (warrior1.getName(),warrior2.getName())

    def getDodge(self,warrior1, warrior2):
        """Comments for the warrior dodging the weapon."""
        return self.dodgeC[warrior1.getWeapon()] % warrior2.getName()

    def getCriticalHit(self,warrior1, warrior2):
        """Comments for critical hits."""
        return self.critHits[warrior1.getWeapon()] % (warrior1.getName(),warrior2.getName())

    def getCriticalDodge(self,warrior1,warrior2):
        """Comments for critical dodges."""
        return self.critDodge[warrior1.getWeapon()] % warrior2.getName()

    def getCriticalBoth(self):
        return "In a blinding flurry of dodging and blows both warriors lightly damage each other."

    def getDead(self,warrior):
        """Announce the warrior has died."""
        return "%s crumples as the last blow is struck." % warrior.getName()

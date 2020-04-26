import random

class Magic:
    def __init__(self, name, mp_cost, dmg,):
        self.name = name
        self.mp_cost = mp_cost
        self.dmg = dmg
        self.type= ["Dark","Light"]

    def magenerate(self):
        dmg_h = self.dmg + 15
        dmg_l = self.dmg - 15
        mdamage = random.randrange(dmg_l,dmg_h)
        return mdamage





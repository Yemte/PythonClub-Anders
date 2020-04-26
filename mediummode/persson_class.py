import random

class person:
    def __init__(self, name, hp, mp, attack,magic):
        self.name = name
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.magic = magic
        self.attack = attack
        self.action = ["Attack","Magic"]
    def generate_damage(self):
        attack_h = self.attack + 10
        attack_l = self.attack - 10
        damage = random.randrange(attack_l,attack_h)
        return damage
    def take_damage(self,damage):
        self.hp = (self.hp)-damage
        if self.hp < 0 :
            self.hp = 0
        else:
            self.hp = self.hp
        return self.hp

    def reduce_mp(self,cost):
        self.mp = self.mp-cost
        if self.mp < 0:
            self.mp = 0
        else:
            self.mp = self.mp
        return self.mp

    def choose_action(self):
        number = 1
        print(self.name.upper(), ":")
        print("\t ACTION: ")
        for item in self.action:
            print("\t",number,end=(':'))
            print(item)
            number=number + 1
    # Create new method to choose what magic to use
    def choose_magic(self):
        number = 1
        print("\t Magic: ")
        for magic in self.magic:
            print("\t", number, end=(':'))
            print(magic.name, ", cost : ",magic.mp_cost)
            number = number + 1
    def get_status(self):
        """
                This method will print out the current stats of all player and enemy
                NAME:HP/MaxHP
                    MP/MaxMP
                """
        print(self.name.upper(), end=(':'))
        print(self.hp,"/",self.maxhp)
        print("\t", self.mp,"/",self.maxmp)

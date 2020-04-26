import random

class person:
    def __init__(self, name, hp, mp,attack):
# Health is usually measured in hit points or health points,
# shortened to HP which lowers by set amounts when the entity is attacked or injured
# which indicates their continued ability to function.

# Magic or mana is an attribute assigned to characters within a role-playing or video game that indicates
# their power to use special abilities or "spells".
# Magic is usually measured in magic points or mana points, shortened as MP
        self.name = name
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.attack_h = attack + 10
        self.attack_l = attack -10
        self.action = ["Attack"]


    def generate_damage(self):
        damage = random.randrange(self.attack_l,self.attack_h)
        return damage
    def take_damage(self,damage):
        self.hp = (self.hp)-damage
        if self.hp < 0:
            self.hp = 0
        else:
            self.hp = self.hp
        return self.hp
    def choose_action(self):
        number = 1
        for item in self.action:
            print(self.name.upper(),":")
            print("\t ACTION: ")
            print("\t",number,end=(':'))
            print(item)
            number=number + 1
    def get_status(self):
        """
                This method will print out the current stats of all player and enemy
                NAME:HP/MaxHP
                    MP/MaxMP
                """
        print("\t\t", self.name.upper(), end=(':'))
        print(self.hp,"/",self.maxhp)
        print("\t\t\t ", self.mp,"/",self.maxmp)

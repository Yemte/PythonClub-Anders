# The game starts with a instruction printed out, says "This game is ....."
# After that is the stats of the player and enemy
# Player plays first, start choosing action
# At this point, only attack, after choose attack, enemy will take damage
# Recalculate HP
# Print out the result of this turn, how many damages has been caused by player to enemy
# Enemy's turn
# Call generate damage from enemy, player will take damage
# Recalculate HP
# Print out the result of this turn, how many damages has been caused by enemy to player
# Print out the new stats of player and enemy
# Check hp of player and enemy, whose hp == 0, lost
# If hp != 0, start the loop again
from easymode.person_class import  person
print("Welcom , you are about to start the Game")
print("\t ---- HOW TO PLAY ----")
print("************************************")
print("\t\t1: Give the player a name")
print("\t\t2: Choose an action")
print("\t\t3: at the beginning the hp and mp are at maximum point.")
print("\t\t4: hp deacreases when attacked.")
print("\t\t5: game will end when hp equals zero")
print("\t ---- HAVE FUN ----")
print("************************************")

player_name= input("what is your name:")
player = person(player_name,200,50,15)
enemy = person('enemy',100,30,11)
# print(player.name.upper(),end=(':'))
# print(player.maxhp)
# print("\t ",player.maxmp)
# print(enemy.name.upper(),end=(':'))
# print(enemy.hp/enemy.maxhp)
# print("\t ",enemy.maxmp)
player.get_status()
enemy.get_status()

print("************************************* ")
print("************************************* ")

player.choose_action()

player_action = int(input("chose an action:"))
try:
    if player_action==1:
        player.action[0]
        damage= enemy.generate_damage()
        tak_damage = enemy.take_damage(damage)
        print(tak_damage," damages has been caused to the player")
    elif player_action >1:
        print("Sorry you have only one action to choose,choose number 1")
except:
    print(player_action,"is not a number please enter a valid number")


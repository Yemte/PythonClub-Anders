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
print("\t\t6: You can end quit the game by typinng upper case Q ")
print("\t ---- HAVE FUN ----")

print("************************************")

player_name= input("what is your name:")
player = person(player_name,200,50,15)
enemy = person('enemy',100,30,11)
player.get_status()
enemy.get_status()

print("************************************* ")
print("************************************* ")

player.choose_action()
playing = True
while playing:
    try:
        player_action = int(input("chose an action:"))
        if player_action == 1:
                player.action[0]
                damage = player.generate_damage()
                tak_damage = enemy.take_damage(damage)
                print(damage, " damages has been caused to the enemy")

                print("****** NOW IT\'S  THE ENEMY'S TURN ******")
                dam = enemy.generate_damage()
                tak_dam = player.take_damage(dam)
                print(dam , " damages has been caused to the player")

        elif player_action > 1:
            print("Sorry you have only one action to choose,choose number 1")
            player_action = int(input("chose an action:"))
            if player_action == 1:
                player.action[0]
                damage = player.generate_damage()
                tak_damage = enemy.take_damage(damage)
                print(damage, " damages has been caused to the enemy")
                print("****** NOW IT\'S  THE ENEMY'S TURN ******")
                dam = enemy.generate_damage()
                tak_dam = player.take_damage(dam)
                print(dam, " damages has been caused to the player")

    except ValueError:
        print(" please enter a valid number")
        player_action = int(input("chose an action:"))
        if player_action == 1:
            player.action[0]
            damage = enemy.generate_damage()
            tak_damage = enemy.take_damage(damage)
            print(damage, " damages has been caused to the enemy")
            print("****** NOW IT\'S  THE ENEMY'S TURN ******")
            dam = player.generate_damage()
            tak_dam = player.take_damage(dam)
            print(dam, " damages has been caused to the player")

        elif player_action > 1:
            print("Sorry you have only one action to choose,choose number 1")
            player_action = int(input("chose an action:"))
            if player_action == 1:
                player.action[0]
                damage = enemy.generate_damage()
                tak_damage = enemy.take_damage(damage)
                print(damage, " damages has been caused to the enemy")
                print("****** NOW IT\'S  THE ENEMY'S TURN ******")
                dam = player.generate_damage()
                tak_dam = player.take_damage(dam)
                print(dam, " damages has been caused to the player")
    except :
        print(" opss Something went wrong")
    print("****** BELOW IS THE CURRENT STATUS FOR BOTH ******")
    player.get_status()
    enemy.get_status()
    # print("****** NOW IT\'S  YOUR TURN  PRESS ENETER******")
    X = input()
    if player.hp==0:
        playing = False
        print("YOU LOST!!")

    elif enemy.hp==0:
        playing = False
        print("YOU WINNNNNNNN")

    elif X=='Q':
        playing = False
        print("YOU QUIT")

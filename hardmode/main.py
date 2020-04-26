
from mediummode.persson_class import person
from mediummode.magic_class import Magic
print("Welcom , you are about to start the Game")
# print("\t ---- HOW TO PLAY ----")
# print("================================================")
# print("\t\t1: Give the player a name")
# print("\t\t2: Choose an action")
# print("\t\t3: at the beginning the hp and mp are at maximum point.")
# print("\t\t4: hp deacreases when attacked.")
# print("\t\t5: game will end when hp equals zero")
# print("\t\t6: You can end  the game by typing upper case Q ")
print("\t ---- HAVE FUN ----")


print("====================================================")
i=0
m=0
player_name= input("Give the player a name :")
magic_L = [Magic('Thunder',20,40),Magic('Fire',15,35),Magic('poison',10,30),Magic('stick',5,20)]
player = person(player_name,200,200,15,magic_L)
enemy = person('enemy',200,200,15,magic_L)
player.get_status()
enemy.get_status()

print("===================================================")
print("")

player.choose_action()

playing = True

while playing:
    try:
        player_action = int(input("chose an action:"))
        if player_action == 1:
             # player.action[0]
            damage = player.generate_damage()
            tak_damage = enemy.take_damage(damage)
            print(damage, " damages has been caused to the enemy")
            print("")
            print("****** NOW IT\'S  THE ENEMY'S TURN ******")
            print("")
            dam = enemy.generate_damage()
            tak_dam = player.take_damage(dam)
            print(dam , " damages has been caused to the player")
            print("")
        elif player_action == 2:
             num = 1
             print("\t Magic_type: ")
             for magic_L[i].type[i]in magic_L[i].type:
                 print("\t", num, end=(':'))
                 print(magic_L[i].type[i])
                 num = num + 1
             while(player.mp>0):
                type_choice = int(input("choose a magic type:"))
                if type_choice==2:
                    player.choose_magic()
                    magic_choice = int(input("choose a magic:"))
                    if magic_choice==1:
                        m= magic_L[0].magenerate()
                        tak_damage = enemy.take_damage(m)
                        print( m, " damages has been caused to the enemy hp")
                        mpp=player.reduce_mp(magic_L[0].mp_cost)
                        print(magic_L[0].mp_cost, " cost has been occured to the player mp")
                        print("****** NOW IT\'S  THE ENEMY'S TURN ******")
                        print("")
                        dam = enemy.generate_damage()
                        tak_dam = player.take_damage(dam)
                        print(dam, " damages has been caused to the player")
                        print("")
                    elif magic_choice==2:
                        m= magic_L[1].magenerate()
                        tak_damage = enemy.take_damage(m)
                        print( m , " damages has been caused to the enemy hp")
                        mpp=player.reduce_mp(magic_L[1].mp_cost)
                        print(magic_L[1].mp_cost, " cost has been occured to the player mp")
                        print("****** NOW IT\'S  THE ENEMY'S TURN ******")
                        print("")
                        dam = enemy.generate_damage()
                        tak_dam = player.take_damage(dam)
                        print(dam, " damages has been caused to the player")
                        print("")
                    elif magic_choice==3:
                        m= magic_L[2].magenerate()
                        tak_damage = enemy.take_damage(m)
                        print(m, " damages has been caused to the enemy hp")
                        mpp=player.reduce_mp(magic_L[2].mp_cost)
                        print(magic_L[2].mp_cost, " cost has been occured to the player mp")
                        print("****** NOW IT\'S  THE ENEMY'S TURN ******")
                        print("")
                        dam = enemy.generate_damage()
                        tak_dam = player.take_damage(dam)
                        print(dam, " damages has been caused to the player")
                        print("")
                    elif magic_choice==4:
                        m= magic_L[3].magenerate()
                        tak_damage = enemy.take_damage(m)
                        print( m , " damages has been caused to the enemy hp")
                        mpp=player.reduce_mp(magic_L[3].mp_cost)
                        print(magic_L[3].mp_cost, " cost has been occured to the player mp")
                        print("****** NOW IT\'S  THE ENEMY'S TURN ******")
                        print("")
                        dam = enemy.generate_damage()
                        tak_dam = player.take_damage(dam)
                        print(dam, " damages has been caused to the player")
                        print("")
                    else:
                        print(" give a number from 1 to 4")
                else:
                    print("choose only number 2")
                    continue
             if player.mp == 0:
                print("you have no magic point,u can't use magic")
                continue
        else:
            print("chose a number from the action list above")
            continue
    except (ValueError, IndexError, TypeError):
        print(" wrong number, give a valid number")

        continue
    except:
        print(" opss Something went wrong")
        playing = False
    print("")
    print("****** BELOW IS THE CURRENT STATUS FOR BOTH ******")
    print("")
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

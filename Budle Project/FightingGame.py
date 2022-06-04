import random
from time import sleep


user1_name = input("Player 1 Name :  ")
user2_name = input("Player 2 Name :  ")


def fight():
    try:
        words = ['fuck', 'go to hell', 'fuck off', 'boom']
        active_player = True
        player_1_health = 100
        player_2_health = 100
        cpu_health = 100
        print("""
                  ***********  WELCOME TO  *******************
                  ******** MY GAME APPLICATION ***************

                         Press 1 to Play with Your Friend
                         Press 2 to Play with the CPU

                  ********************************************
                  ********************************************

          """)
        player = int(input("Enter Your Choice"))

        while True:
            try:
                global user1_name, user2_name
                if player == 1:
                    if active_player:
                        user_input = input(f"{user1_name} > ").lower()

                        if player_1_health == 10 or player_1_health < 10:
                            print("WARNING PLAYER 1 YOU ARE DIEING :) ")
                            print(f"life remain for PLAYER 2 {player_2_health}%")
                            active_player = False
                        else:
                            if user_input == "fuck":
                                if player_2_health > 15:
                                    player_2_health -= 15
                                    print(f"life remain for {user2_name} {player_2_health}%")
                                    active_player = False
                                else:
                                    print()
                                    print(f"{user1_name} won !!")
                                    break

                            elif user_input == "go to hell":
                                if player_2_health > 35:
                                    player_2_health -= 35
                                    print(f"life remain for {user2_name} {player_2_health}%")
                                    active_player = False
                                else:
                                    print()
                                    print(f"{user1_name} won !!")
                                    break

                            elif user_input == "fuck off":
                                if player_2_health > 20:
                                    player_2_health -= 20
                                    active_player = False
                                    print(f"life remain for {user2_name} {player_2_health}%")
                                else:
                                    print()
                                    print(f"{user1_name} won !!")
                                    break

                            elif user_input == "boom":
                                if player_2_health > 30:
                                    player_2_health -= 30
                                    active_player = False
                                    print(f"life remain for {user2_name} {player_2_health}%")
                                else:
                                    print()
                                    print(f"{user1_name} won !!")
                                    break
                            elif user_input == "health":
                                print(f"Your Life remain is {player_1_health}%")
                            elif user_input == "help":
                                print("""
                                *************** WELCOME TO ******************
                                ********* FIGHT GAME APPLICATION ************
                                         Use Words to Fight like :
        
                                          ==> Fuck ------------ 25%
                                          ==> Go To Hell ------ 35%
                                          ==> Fuck Off -------- 20%
                                          ==> Boom ------------ 50%
                                          
                                **********************************************
                                **********************************************
                                                         """)
                            else:
                                print("Unknown Input Use Help Command for HELP !")

                    elif not active_player:

                        if player_2_health == 10 or player_2_health < 10:
                            print(f"WARNING {user2_name} YOU ARE DIEING :) ")
                            print(f"life remain for {user1_name}  {player_1_health}%")
                            active_player = True
                        else:
                            user_input = input(f"{user2_name} > ").lower()
                            if user_input == "fuck":
                                if player_1_health > 15:
                                    player_1_health -= 15
                                    print(f"life remain for {user1_name}  {player_1_health}%")
                                    active_player = True
                                else:
                                    print()
                                    print(f"{user2_name} won !!")
                                    break

                            elif user_input == "go to hell":
                                if player_1_health > 35:
                                    player_1_health -= 35
                                    print(f"life remain for {user1_name} {player_1_health}%")
                                    active_player = True
                                else:
                                    print()
                                    print(f"{user2_name} won !!")
                                    break

                            elif user_input == "fuck off":
                                if player_1_health > 20:
                                    player_1_health -= 20
                                    print(f"life remain for {user1_name} {player_1_health}%")
                                    active_player = True
                                else:
                                    print()
                                    print(f"{user2_name} won !!")
                                    break

                            elif user_input == "boom":
                                if player_1_health > 30:
                                    player_1_health -= 30
                                    print(f"life remain for {user1_name} {player_1_health}%")
                                    active_player = True
                                else:
                                    print()
                                    print(f"{user2_name} won !!")
                                    break

                            elif user_input == "health":
                                print(f"Your Life remain is {player_2_health}%")
                            elif user_input == "help":
                                print("""
                                *************** WELCOME TO ******************
                                ********* FIGHT GAME APPLICATION ************
                                        Use Words to Fight like :
                                
                                         ==> Fuck ------------ 15%
                                         ==> Fuck Off -------- 20%
                                         ==> Go To Hell ------ 35%
                                         ==> Boom ------------ 50%
                                         
                                **********************************************
                                **********************************************
                                 """)
                            else:
                                print("Unknown Input Use Help Command for HELP !")
                elif player == 2:
                    if active_player:
                        user_input = input(f"{user1_name} >").lower()
                        if user_input == "fuck":
                            if cpu_health > 15:
                                cpu_health -= 15
                                print(f"life remain for CPU {cpu_health}%")
                                active_player = False
                            else:
                                print()
                                print(f"{user1_name} Won !!")
                                break
                        elif user_input == "go to hell":
                            if cpu_health > 35:
                                cpu_health -= 35
                                print(f"life remain for CPU {cpu_health}%")
                                active_player = False
                            else:
                                print()
                                print(f"{user1_name} Won !!")
                                break
                        elif user_input == "fuck off":
                            if cpu_health > 20:
                                cpu_health -= 20
                                print(f"life remain for CPU {cpu_health}%")
                                active_player = False
                            else:
                                print()
                                print(f"{user1_name} Won !!")
                                break
                        elif user_input == "boom":
                            if cpu_health > 30:
                                cpu_health -= 30
                                print(f"life remain for CPU {cpu_health}%")
                                active_player = False
                            else:
                                print()
                                print(f"{user1_name} Won !!")
                                break
                        elif user_input == "help":
                            print("""
                                    *************** WELCOME TO ******************
                                    ********* FIGHT GAME APPLICATION ************
                                             Use Words to Fight like :
    
                                             ==> Fuck ------------ 15%
                                             ==> Fuck Off -------- 20%
                                             ==> Go To Hell ------ 35%
                                             ==> Boom ------------ 50%
    
                                    **********************************************
                                    **********************************************
                                                         """)
                        else:
                            print("Unknown Input Use Help Command for HELP !")
                    elif not active_player:
                        cpu = random.choice(words)
                        print(f"CPU > {cpu}")
                        if cpu == words[0]:
                            if player_1_health > 15:
                                player_1_health -= 15
                                print(f"life remain for {user1_name} {player_1_health}%")
                                active_player = True
                            else:
                                print()
                                print(f"CPU Won !!")
                                break
                        elif cpu == words[1]:
                            if player_1_health > 35:
                                player_1_health -= 35
                                print(f"life remain for {user1_name} {player_1_health}%")
                                active_player = True
                            else:
                                print()
                                print(f"CPU Won !!")
                                break
                        elif cpu == words[2]:
                            if player_1_health > 20:
                                player_1_health -= 20
                                print(f"life remain for {user1_name} {player_1_health}%")
                                active_player = True
                            else:
                                print()
                                print(f"CPU Won !!")
                                break
                        elif cpu == words[3]:
                            if player_1_health > 30:
                                player_1_health -= 30
                                print(f"life remain for {user1_name} {player_1_health}%")
                                active_player
                            else:
                                print()
                                print(f"CPU Won !!")
                                break
                else:
                    print("Unknown Input Use Help Command for HELP !")
            except Exception as e:
                print(e)
    except Exception as e:
        print("Unknown Input Use Help Command for HELP !")


def play_again(user_name1 , user_name2):

    print("""
                *************** WELCOME TO ******************
                ********* FIGHT GAME APPLICATION ************
                *************** GOOD LUCK ******************* 

                        ==> USE HELP TO GET HELP

                **********************************************
                **********************************************       
     """)
    cho = input("Do You want to play again with the player ? (Y/N)").upper()
    if cho == 'Y':
        fight()
    elif cho == 'N':
        user_name1 = input("Player 1 Name :  ")
        user_name2 = input("Player 2 Name :  ")
        globals()['user1_name'] = user_name1
        globals()['user2_name'] = user_name2
        fight()
    else:
        print("Unknown Input")


print("""
            *************** WELCOME TO ******************
            ********* FIGHT GAME APPLICATION ************
            *************** GOOD LUCK ******************* 
                    
                    ==> USE HELP TO GET HELP
                    
            **********************************************
            **********************************************       
 """)

fight()
print()

while True:
    cho = input("Do You wanna play again ? (Y/N)").upper()[0]
    if cho == 'Y':
        play_again(user1_name,user2_name)
    elif cho == 'N':
        print("Have a nice a day")
        break
    else:
        print("Unknown Input")

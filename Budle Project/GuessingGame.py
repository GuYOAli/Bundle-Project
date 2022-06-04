import random


def random_generator():
    try:
        print("""
                         ***********  WELCOME TO  *******************
                         ******** MY GAME APPLICATION ***************

                                Press 1 to Play with Friends
                                Press 2 to Play with CPU

                         ********************************************
                         ********************************************

                 """)
        player = int(input(" Enter Ur choice > "))
        active_player = True
        count = 0
        limit = 5
        num = random.randint(1, 10 + 1)
        global user1_name, user2_name
        while count < limit:
            if player == 1:
                if active_player:
                    number = int(input(f"{user1_name} > "))
                    if number == 0 or number < 0 or number > 10:
                        print("Out of Range 1 - 10")
                    else:
                        count += 1
                        active_player = False
                        if number == num:
                            print(f"{user1_name} Won !!! :) ")
                            break
                elif not active_player:
                    number = int(input(f"{user2_name} > "))
                    if number == 0 or number < 0 or number > 10:
                        print("Out of Range 1 - 10")
                    else:
                        count += 1
                        active_player = True
                        if number == num:
                            print(f"{user2_name} Won !!! :) ")
                            break
            elif player == 2:
                if active_player:
                    number = int(input(f"{user1_name} > "))
                    if number == 0 or number < 0 or number > 10:
                        print("Out of Range 1 - 10")
                    else:
                        count += 1
                        active_player = False
                        if number == num:
                            print(f"{user1_name} Won !!! :) ")
                            break
                elif not active_player:
                    cpu = random.randint(1 , 10+1)
                    print(f"CPU  > {cpu}")
                    count += 1
                    active_player = True
                    if cpu == num:
                        print("Computer Won !!! :) ")
                        break
            else:
                print("Unknown input pleas Enter a valid input")
                break
        else:
            print("Oh!! Both You Failed ..")

    except Exception as e:
        print(e)


user1_name = input("Player 1 Name : ")
user2_name = input("Player 2 Name : ")


def play_again(user_name1,user_name2):

    print("""
        **********************************************
        **********************************************
        *********** WELCOME TO GUSS GAME   ***********
        ********** GUSS THE NUMBER BETWEEN ***********
        **********        1 - 10           ***********
        **********      GOOD LUCK          ***********
        **********************************************
        **********************************************
        """)
    cho = input("Do You want to play again with the player ? (Y/N)").upper()[0]
    if cho == 'Y':
        random_generator()
    elif cho == 'N':
        user_name1 = input("Player 1 Name : ")
        user_name2 = input("Player 2 Name : ")
        globals() ['user1_name'] = user_name1
        globals() ['user2_name'] = user_name2
        random_generator()
    else:
        print("Unknown Input ....")


print("""
        **********************************************
        **********************************************
        *********** WELCOME TO GUSS GAME   ***********
        ********** GUSS THE NUMBER BETWEEN ***********
        **********        1 - 10           ***********
        **********      GOOD LUCK          ***********
        **********************************************
        **********************************************
""")


random_generator()


def again():
    while True:

        cho = input("Do You wanna play again ? (Y/N)").upper()[0]
        if cho == 'Y':
            play_again(user1_name,user2_name)
        elif cho == 'N':
            print("Have a nice a day! ")
            break
        else:
            print("Unknown Input Please Enter a valid Input")


again()


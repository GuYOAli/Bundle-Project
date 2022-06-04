
def play_again():
    complex_project()


def complex_project():

    while True:
        print("""
                ***********  WELCOME TO  *******************
                ****** MY COMPLEX APPLICATION **************
        
                       Press 1 to Play a Game
                       Press 2  to Use Scientific Calculator
        
                ********************************************
                ********************************************
        
        """)
        user_input = int(input(" Enter Ur Choise > "))

        if user_input == 1:
            print("""
                         ************* WELCOME TO ******************
                         ******** MY GAME APPLICATION **************
    
                               Press 1 to Play Guessing Game
                               Press 2 to Play Car Game
                               Press 3 to Play Fighting Game
    
                         *******************************************
                         *******************************************
    
                """)
            cho = int(input("Which Game You Want to Play ?   >  "))
            if cho == 1:
                import GussingGame
                cho2 = input("Do You Want to Continue Using this App  ? (Y/N)").upper()[0]
                if cho2 == 'Y':
                    play_again()
                elif cho2 == 'N':
                    print()
                    print("Have a nice a day! ")
                    print()
                    break
                else:
                    print("Unknown Input Please Enter a valid Input")
            elif cho == 2:
                import CarGame
                cho2 = input("Do You Want to Continue Using this App  ? (Y/N)").upper()[0]
                if cho2 == 'Y':
                    play_again()
                elif cho2 == 'N':
                    print()
                    print("Have a nice a day! ")
                    print()
                    break
            elif cho == 3:
                import FightingGame
                cho2 = input("Do You Want to Continue Using this App  ? (Y/N)").upper()[0]
                if cho2 == 'Y':
                    play_again()
                elif cho2 == 'N':
                    print()
                    print("Have a nice a day! ")
                    print()
                    break
            else:
                print("Unknown Input Please Enter a valid Input")
        elif user_input == 2:
            import Calculator
            cho2 = input("Do You Want to Continue Using this App  ? (Y/N)").upper()[0]
            if cho2 == 'Y':
                play_again()
            elif cho2 == 'N':
                print()
                print("Have a nice a day! ")
                print()
                break
        else:
            print("Unknown Input Please Enter a valid Input")


complex_project()

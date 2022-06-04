
def car_game():
    try:
        is_started = False

        while True:
            user_input = input(">").upper()
            if user_input == "START":
                if not is_started:
                    print("Car is Started")
                    is_started = True
                elif is_started:
                    print("Car is already Started")

            elif user_input == "STOP":
                if is_started:
                    print("Car is Stopped")
                    is_started = False
                elif not is_started:
                    print("Car is already  Stopped")
            elif user_input == "HELP":
                print("""

                    Start - to start the Car
                    Stop - to Stop the Car
                    Help - to get Help
                    Quit - to Exit 

                    """)
            elif user_input == "QUIT":
                break

            else:
                print("I don't Understand it ...")
    except Exception as e:
        print(e)


car_game()

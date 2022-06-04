from math import *
from time import sleep


class Calculator:

    def __init__(self):
        pass

    try:
        def add(self, a, b):
            try:
                c = a + b
                print("The Sum of {} and {} is = {}".format(a, b, c))
            except Exception as e:
                print(e)

        def sub(self, a, b):
            try:
                c = a - b
                print("The subtraction of {} and {} is = {}".format(a, b, c))
            except Exception as e:
                print(e)

        def mul(self, a, b):
            try:
                c = a * b
                print("The Multiplication of {} and {} is = {}".format(a, b, c))
            except Exception as e:
                print(e)

        def dev(self, a, b):
            try:
                c = a / b
                print("The Division of {} and {} is = {} ".format(a, b, c))
            except Exception as e:
                print(e)

        def eva(self):
            try:
                a = input("Enter the Expression ")
                b = eval(a)
                print("The Expression of {} is = {}".format(a,b))
            except Exception as e:
                print(e)

        def sinn(self, a):
            try:
                print('The sin of {} is = {}'.format(a, round(sin(a))))
            except Exception as e:
                print(e)

    except Exception as e:
        print(e)


def cal():
    calc = Calculator()
    while True:

        print("""
             **************************************************
             **************************************************
             *************** WELCOME TO MY ********************
             *********** CALCULATOR APPLICATION ***************     
             **        Enter  + for Addition                 **
             **        Enter - for Subtraction               **
             **        Enter  * for Multiplication           **
             **        Enter  / for Division                 **
             **        Enter  @ for Expression               **
             **        Enter  s for Sin                      **
             **        Enter  Q for exit                     **
             **************************************************
             **************************************************        

        """)
        x = input("Enter Your Option ..\n")[0]

        if x == '+':
            a = float(input("Enter the first Number"))
            b = float(input("Enter the Second Number"))
            calc.add(a, b)
            sleep(3)
        elif x == '-':
            a = float(input("Enter the first Number"))
            b = float(input("Enter the Second Number"))
            calc.sub(a, b)
            sleep(3)
        elif x == '*':
            a = float(input("Enter the first Number"))
            b = float(input("Enter the Second Number"))
            calc.mul(a, b)
            sleep(3)
        elif x == '/':
            a = float(input("Enter the first Number"))
            b = float(input("Enter the Second Number"))
            if a < b:
                cho = input("do u want to swap cause {} is less than {} Enter (Y/y) "
                            "for Yes and Enter (N/n) for No ".format(a, b))[0]
                if cho == 'Y' or cho == 'y':
                    a, b = b, a
                    calc.dev(a, b)
                    sleep(3)
                elif cho == 'N' or cho == 'n':
                    a, b = a, b
                    calc.dev(a, b)
                    sleep(3)
            else:
                calc.dev(a, b)
                sleep(3)
        elif x == '@':
            calc.eva()
            sleep(3)
        elif x == 's':
            a = float(input("Enter the  Number"))
            calc.sinn(a)
            sleep(3)
        elif x == 'Q' or x == 'q':
            break
        else:
            print(" Unknown Input :) ")
            sleep(3)


cal()

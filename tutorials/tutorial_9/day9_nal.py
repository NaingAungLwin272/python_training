#    1
import math


def calculate():
    while True:

        print("""Select Operation
                1.Add
                2.Subtract
                3.Multiply
                4.Divide
                5.Power
                6.Modulo
                7.Square_Root
                8.Cube
                -----------------------------------------------------------""")

        user_input = str(input("Enter User Input : "))

        try:
            if user_input.lower() == "squareroot" or user_input == "7":
                num1 = float(input('Enter Number : '))

            elif user_input.lower() == "cube" or user_input == "8":
                num1 = float(input('Enter Number : '))

            else:
                num1 = float(input('Enter First Number : '))
                num2 = float(input('Enter Second Number : '))
        except ValueError:
            print("Check your Input Again")
        else:
            if user_input.lower() == "add" or user_input == "1":

                result = num1 + num2
                print(" {} + {} ".format(num1, num2), "= ", result)
            elif user_input.lower() == "subtract" or user_input == "2":
                result = num1 - num2
                print(" {} - {} ".format(num1, num2), "= ", result)
            elif user_input.lower() == "multiply" or user_input == "3":

                result = num1 * num2
                print(" {} * {} ".format(num1, num2), "= ", result)
            elif user_input.lower() == "divided" or user_input == "4":

                result = num1 / num2
                print(" {} / {} ".format(num1, num2), "= ", result)
            elif user_input.lower() == "power" or user_input == "5":

                result = math.pow(num1, num2)
                print(" {} ** {} ".format(num1, num2), "= ", result)
            elif user_input.lower() == "modulo" or user_input == "6":
                result = num1 % num2
                print(" {} % {} ".format(num1, num2), "= ", result)
            elif user_input.lower() == "squareroot" or user_input == "7":

                result = math.sqrt(num1)
                print(" Square root of {} ".format(num1), "= ", result)
            elif user_input.lower() == "cube" or user_input == "8":

                result = num1 ** 3
                print("Cube of {} ".format(num1), "= ", result)
            else:
                print("Check your Input Again")
                continue

            again()
            break


def again():

    user_choice = input("Let`s do next calculation?(yes/no): ")

    if user_choice.lower() == "yes":
        calculate()
    elif user_choice.lower() == "no":
        print("Bye Bye")

    else:
        print("Invalid Input")
        again()


calculate()

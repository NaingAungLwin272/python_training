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

        if user_input.lower() == "add" or user_input == "1":

            while True:
                try:
                    num1 = float(input("Enter First Number : "))
                    while True:
                        try:
                            num2 = float(input("Enter Second Number : "))
                            break
                        except ValueError:
                            print("Check your Number Input again")
                            print("---------------------------------------")

                    result = num1 + num2
                    print(" {} + {} ".format(num1, num2), "= ", result)
                    break
                except ValueError:
                    print("Check your Number again")
                    print("---------------------------------------")

        elif user_input.lower() == "subtract" or user_input == "2":
            while True:
                try:
                    num1 = float(input("Enter First Number : "))
                    while True:
                        try:
                            num2 = float(input("Enter Second Number : "))
                            break
                        except ValueError:
                            print("Check your Number Input again")
                            print("---------------------------------------")

                    result = num1 - num2
                    print(" {} + {} ".format(num1, num2), "= ", result)
                    break
                except ValueError:
                    print("Check your Number Input again")
                    print("---------------------------------------")

        elif user_input.lower() == "multiply" or user_input == "3":
            while True:
                try:
                    num1 = float(input("Enter First Number : "))
                    while True:
                        try:
                            num2 = float(input("Enter Second Number : "))
                            break
                        except ValueError:
                            print("Check your Number Input again")
                            print("---------------------------------------")

                    result = num1 * num2
                    print(" {} + {} ".format(num1, num2), "= ", result)
                    break
                except ValueError:
                    print("Check your Number  Input again")
                    print("---------------------------------------")
        elif user_input.lower() == "divided" or user_input == "4":

            while True:
                try:
                    num1 = float(input("Enter First Number : "))
                    while True:
                        try:
                            num2 = float(input("Enter Second Number : "))
                            break
                        except ValueError:
                            print("Check your Number  Input again")
                            print("---------------------------------------")

                    result = num1 / num2
                    print(" {} / {} ".format(num1, num2), "= ", result)
                    break
                except ValueError:
                    print("Check your Number Input again")
                    print("---------------------------------------")

        elif user_input.lower() == "power" or user_input == "5":

            while True:
                try:
                    num1 = float(input("Enter First number:"))

                    while True:
                        try:
                            num2 = float(input("Enter Second number:"))
                            break
                        except ValueError:

                            print("Check your Number Input Again")
                            print("---------------------------------------")

                    result = math.pow(num1, num2)
                    print(" {} ** {} ".format(num1, num2), "= ", result)
                    break
                except ValueError:

                    print("Check your Number Input again")
                    print("---------------------------------------")

        elif user_input.lower() == "modulo" or user_input == "6":

            while True:
                try:
                    num1 = float(input("Enter First number:"))

                    while True:
                        try:
                            num2 = float(input("Enter Second number:"))
                            break
                        except ValueError:

                            print("Check your Number Input Again")
                            print("---------------------------------------")

                    result = num1 % num2
                    print(" {} % {} ".format(num1, num2), "= ", result)
                    break
                except ValueError:

                    print("Check your Number Input again")
                    print("---------------------------------------")

        elif user_input.lower() == "squareroot" or user_input == "7":
            while True:
                try:

                    num1 = float(input('Enter Number : '))
                    break

                except ValueError:
                    print("Check your Number Input again")
                    print("---------------------------------------")

            result = math.sqrt(num1)
            print(" Square root of {} ".format(num1), "= ", result)

        elif user_input.lower() == "cube" or user_input == "8":

            while True:
                try:

                    num1 = float(input('Enter Number : '))
                    break

                except ValueError:
                    print("Check your Number Input again")
                    print("---------------------------------------")

            result = num1 ** 3
            print("Cube of {} ".format(num1), "= ", result)
        else:
            print("Check your Operation Input again")
            print("---------------------------------------")
            continue

        again()
        break


def again():

    user_choice = input("Let`s do next calculation?(yes/no): ")

    if user_choice.lower() == "yes":
        calculate()
    elif user_choice.lower() == "no":
        print("Bye Bye")
        print("---------------------------------------")

    else:
        print("Choose only yes or no")
        print("---------------------------------------")
        again()


calculate()

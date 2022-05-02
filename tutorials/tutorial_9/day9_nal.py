#    1
import math

while True:

    print("""Select Operation
  1.Add
  2.Subtract
  3.Multiply
  4.Divide
  5.Power
  6.Modulo
  7.Square_Root
  8.Cube""")
    user_input = str(input("Enter Choice : "))

    if user_input.lower() in "add" or user_input == "1":
        num1 = float(input("Enter First Number : "))
        num2 = float(input("Enter Second Number: "))
        result = num1 + num2
        print(" {} + {} ".format(num1, num2), "= ", result)
    elif user_input.lower() in "subtract" or user_input == "2":
        num1 = float(input("Enter First Number : "))
        num2 = float(input("Enter Second Number: "))
        result = num1 - num2
        print(" {} - {} ".format(num1, num2), "= ", result)
    elif user_input.lower() in "multiply" or user_input == "3":
        num1 = float(input("Enter First Number : "))
        num2 = float(input("Enter Second Number: "))
        result = num1 * num2
        print(" {} * {} ".format(num1, num2), "= ", result)
    elif user_input.lower() in "divided" or user_input == "4":
        num1 = float(input("Enter First Number : "))
        num2 = float(input("Enter Second Number: "))
        result = num1 / num2
        print(" {} / {} ".format(num1, num2), "= ", result)
    elif user_input.lower() in "power" or user_input == "5":
        num1 = float(input("Enter First Number : "))
        num2 = float(input("Enter Second Number: "))
        result = math.pow(num1, num2)
        print(" {} ** {} ".format(num1, num2), "= ", result)
    elif user_input.lower() in "modulo" or user_input == "6":
        num1 = float(input("Enter First Number : "))
        num2 = float(input("Enter Second Number: "))
        result = num1 % num2
        print(" {} % {} ".format(num1, num2), "= ", result)
    elif user_input.lower() in "squareroot" or user_input == "7":
        num1 = float(input("Enter Number : "))
        result = math.sqrt(num1)
        print(" Square root of {} ".format(num1), "= ", result)
    elif user_input.lower() in "cube" or user_input == "8":
        num1 = float(input("Enter Number : "))
        result = num1 ** 3
        print("Cube of {} ".format(num1), "= ", result)
    else:
        print("Invalid Input")

    user_choice = input("Let`s do next calculation?(yes/no): ")

    if user_choice == "yes":
        continue
    elif user_choice == "no":
        break
    else:
        print("Invalid Input")
        break

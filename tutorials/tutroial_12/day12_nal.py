#    1
from time import sleep


def count_time():

    while True:
        user_choice = str(input(
            "Enter 1 for Count Up Timer and Enter 2 for Count Down Timer : "))

        while user_choice != '1' and user_choice != '2':
            print(" ")
            user_choice = input("Choose only 1 or 2.Input Again Please : ")
            print(" ")

        if user_choice == '1':
            while True:
                try:
                    start = int(input("Enter Start Time :"))
                    print(" ")
                    while True:
                        try:
                            end = int(input("Enter End time : "))
                            print(" ")
                            break
                        except ValueError:

                            print("Check your EndTime Input Again")
                            print("---------------------------------------")

                    for x in range(start, end):
                        timer = '{:02d}:{:02d}:{:02d}'.format(0, 0, x)
                        print(timer)
                        sleep(1)
                    print("Time Up")
                    print(" ")
                    break
                except ValueError:

                    print("Check your StartTime Input again")
                    print("---------------------------------------")

        elif user_choice == '2':
            while True:
                try:
                    start = int(input("Enter Start Time :"))
                    print(" ")
                    while True:
                        try:
                            end = int(input("Enter End time : "))
                            print(" ")
                            break
                        except ValueError:

                            print("Check your EndTime Input Again")
                            print("---------------------------------------")

                    for x in range(start, end, -1):
                        timer = '{:02d}:{:02d}:{:02d}'.format(0, 0, x)
                        print(timer)
                        sleep(1)
                    print("Time Up")
                    print(" ")
                    break
                except ValueError:

                    print("Check your StartTime Input again")
                    print("---------------------------------------")

        again = input("Restart again?(Y or N) : ")
        while again.lower() != 'y' and again.lower() != 'n':
            again = input("Chosse only Y or N.Input again Please : ")
            print(" ")
            continue

        if again == 'n':
            print("Bye Bye")
            print("--------------------------------")
            break


count_time()

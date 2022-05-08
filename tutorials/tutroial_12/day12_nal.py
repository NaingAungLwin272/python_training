#    1
from time import sleep


def count_time():

    while True:
        user_choice = str(input(
            "Enter 1 for Count Up Timer and Enter 2 for Count Down Timer : "))

        while user_choice != '1' and user_choice != '2':
            print(" ")
            user_choice = input(" 1 For CountUp or 2 For CountDown : ")
            print(" ")

        if user_choice == '1':
            while True:
                try:
                    start = int(input("Enter Start Time(sec) :"))
                    print(" ")
                    while True:
                        try:
                            end = int(input("Enter End Time(sec) : "))
                            print(" ")
                            break
                        except ValueError:

                            print("Invalid Time Input.Please Enter A Valid One.")
                            print("---------------------------------------")

                    if end < start:
                        print("End Time must be Greater than Start time")
                    else:
                        for x in range(start, end):

                            hour = x // 3600
                            x %= 3600
                            mins = x // 60
                            secs = x % 60
                            timer = '{:02d}:{:02d}:{:02d}'.format(
                                hour, mins, secs)
                            print(timer)
                            sleep(1)
                        print("Time Up")
                        print(" ")
                        break
                except ValueError:

                    print("Invalid Time Input.Please Enter A Valid One.")
                    print("---------------------------------------")

        elif user_choice == '2':
            while True:
                try:
                    start = int(input("Enter Start Time(sec) :"))
                    print(" ")
                    while True:
                        try:
                            end = int(input("Enter End time(sec) : "))
                            print(" ")
                            break
                        except ValueError:

                            print("Invalid Time Input.Please Enter A Valid One.")
                            print("---------------------------------------")

                    if end > start:
                        print("End time must be Less than Start time")
                    else:
                        for x in range(start, end, -1):
                            hour = x // 3600
                            x %= 3600
                            mins = x // 60
                            secs = x % 60
                            timer = '{:02d}:{:02d}:{:02d}'.format(
                                hour, mins, secs)
                            print(timer)
                            sleep(1)
                        print("Time Up")
                        print(" ")
                        break
                except ValueError:

                    print("Invalid Time Input.Please Enter A Valid One.")
                    print("---------------------------------------")

        again = input("Restart again?(Y or N) : ")
        while again.lower() != 'y' and again.lower() != 'n':
            again = input("Invalid Input.Input Y or N only : ")
            print(" ")
            continue

        if again == 'n':
            print("Bye Bye")
            print("--------------------------------")
            break


count_time()

#   1
f = open("meeting.txt", "w")
f.write("Nice to meet you. I'm Tendo Soji. I'm from Japan.")
f.close()

f = open("meeting.txt", "r")
print(f.read())


#   2
def word_count():

    file = open("meeting.txt", "r")

    file_data = file.read()

    file_words = file_data.split()
    print("Total number of words : ", len(file_words))


word_count()


#   3
number = input("Enter a number:: ")
try:
    value = int(number)
    if value < 0:
        print("Number must be positive integer")

except ValueError:
    print("This was not a number, please try again.")

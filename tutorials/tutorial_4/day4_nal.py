#   1
L = [*range(0, 11)]
print(L)
square_list = map(lambda x: x ** 2, L)
print(list(square_list))
cube_list = map(lambda x: x ** 3, L)
print(list(cube_list))


#   2
def star_function(x):
    n = 5
    for i in range(0, n):
        for j in range(0, i+1):
            print(x, end="")

        print("\r")


star_function("* ")
star_function("? ")

# 1
number1 = 10
number2 = 40
product = number1 * number2
result = number1 + number2
if product > 500:
    syntax = "The expected output is : {}"
    print(syntax.format(product))
else:
    syntax = "The result is {}"
    print(syntax.format(result))

print("#####################################")

number1 = 50
number2 = 40
product = number1 * number2
result = number1 + number2
if product > 500:
    syntax = "The expected output is : {}"
    print(syntax.format(product))
else:
    syntax = "The result is {}"
    print(syntax.format(result))


# 2
arr1 = [1, 2, 3, 4, 5]
arr2 = [4, 5, 7, 9, 10]

if list(set(arr1) & set(arr2)):
    print("Two lists are duplicated.")
else:
    print("Two lists are not duplicated.")

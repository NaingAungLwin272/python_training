#   1
import datetime
from datetime import timedelta
from datetime import date

given_date = datetime.datetime(
    2022, 4, 27, 10, 0, 0) + timedelta(days=2, hours=2)

print(given_date)


#   2
date1 = datetime.datetime(2022, 4, 27)
date2 = datetime.datetime(2047, 3, 21)
number_of_days = date2 - date1
print(number_of_days)


#   3
three_months = date.today() + timedelta(3 * 30)
print(three_months)


#   4
input = int(input("Enter an interger: "))
divisor = 0

for i in range(1, input+1):
    if(input % i) == 0:
        divisor += i
        print(i)
print("The sum of the divisors is:", divisor)

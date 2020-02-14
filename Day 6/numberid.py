num = int(input("input a number: "))

if num % 2 == 0:
    even = "even"
    even2 = "is"
else:
    even = "odd"
    even2 = "is not"

if num % 3 == 0:
    three = "is"
else:
    three = "is not"

if num % 4 == 0:
    four = "is"
else:
    four = "is not"

if num % 5 == 0:
    five = "is"
else:
    five = "is not"

print(
    "your number is " + even + ".\nit " + even2 + " a multiple of 2.\nit " + three + " a multiple of 3.\nit " + four +
    " a multiple of 4.\nit " + five + " a multiple of five.")

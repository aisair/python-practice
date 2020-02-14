import math

value = float(input("input a dollar amount: "))

hundreds = int(value // 100)
value = value - 100 * hundreds
fifties = int(value // 50)
value = value - 50 * fifties
twenties = int(value // 20)
value = value - 20 * twenties
tens = int(value // 10)
value = value - 10 * tens
fives = int(value // 5)
value = value - 5 * fives
twos = int(value // 2)
value = value - 2 * twos
ones = math.floor(value)
value = value - ones
halves = int(value // 0.5)
value = value - halves * 0.5
quarters = int(value // 0.25)
value = value - quarters * 0.25
dimes = int(value // 0.1)
value = value - dimes * 0.1
nickels = int(value // 0.05)
value = value - nickels * 0.05
pennies = math.ceil(value*100)

print(value)

print("how to pay:\n" + str(hundreds) + " 100 dollar bill(s),\n" + str(fifties) + " 50 dollar bill(s),\n" +
      str(twenties) + " 20 dollar bill(s),\n" + str(tens) + " 10 dollar bill(s),\n" + str(fives) +
      " 5 dollar bill(s),\n" + str(twos) + " 2 dollar bill(s),\n" + str(ones) + " 1 dollar bill(s),\n" + str(halves) +
      " half-dollar coin(s),\n" + str(quarters) + " quarter(s),\n" + str(dimes) + " dime(s),\n" + str(nickels) +
      " nickel(s),\nand " + str(pennies) + " penny(ies)")


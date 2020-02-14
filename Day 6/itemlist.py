# part 1
"""
ask = 5
i = 0
list = []

print(str(ask) + " item(s): ")

while i < ask:
    list.append(input("input item: "))
    i += 1

print(list)
"""
# part 2
ask = 5
i = 0
j = 0
inputs = []
threes = []

print(str(ask) + " item(s): ")

while i < ask:
    inputs.append(input("input item: "))
    i += 1

for j in inputs:
    if int(j) % 3 == 0:
        threes.append(j)

print(threes)

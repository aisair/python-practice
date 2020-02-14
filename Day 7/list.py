import random

random_list = []
even_list = []
to_remove = []
i = 0

while i < 5:
    add_number = random.randint(0, 100)
    random_list.append(add_number)
    i += 1

"""for test in random_list:
    if test % 2 == 0:
        to_remove.append(test)
        even_list.append(test)

for rem in to_remove:
    random_list.remove(rem)

print("randoms: " + str(random_list))
print("evens: " + str(even_list))"""

random_list.sort()
lower = int(input("lower bound?: "))
upper = int(input("upper bound?: "))

for lower_item in random_list:
    if lower_item > lower:
        break
    else:
        lower_item = -1

for upper_item in random_list:
    if upper_item < upper:
        break
    else:
        upper_item = -1

for first_less_upper_index in random_list:
    if first_less_upper_index < upper:
        if random_list.index(first_less_upper_index) == len(random_list) - 1:
            break
    else:
        first_less_upper_index = -1

lower_index = ""
upper_index = ""

if lower_item == -1:

    lower_index = "none found."
else:
    lower_index = random_list.index(lower_item)

if upper_item == -1:
    upper_index = "none found."
else:
    upper_index = random_list.index(upper_item)

print("original set: {list}\ngreater than lower index: {lprint}\nless than upper index: {uprint}\ngreater that lower: "
      "{i}\nless than upper: {j}".format(list=random_list, lprint=lower_index, uprint=upper_index, i=random_list[lower_index:],
                                         j=random_list[:upper_index + 1]))

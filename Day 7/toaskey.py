def convert(char):  # this is redundant but its part of the assignment
    return ord(char)
"""
char = str(input("input character: "))
print("your character in ascii is " + str(convert(char)))
"""

before = input("input string: ")
length = len(before)
out = []
for char in before:
    out.append(convert(char))

print(out)
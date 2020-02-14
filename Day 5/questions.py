score = 0

answer1 = str.lower(input("how many digits are in the constant pi? "))
if answer1 == "infinity":
    print("correct!")
    score = score + 1
else:
    print("incorrect.")

answer2 = str.lower(input("what is 43 to the 0th power? "))
if answer2 == "1":
    print("correct!")
    score = score + 1
else:
    print("incorrect.")

answer3 = str.lower(input("how many letters are in the english alphabet? "))
if answer3 == "26":
    print("correct!")
    score = score + 1
else:
    print("incorrect.")


def give_grade(test):
    if test >= 90:
        grade = "A"
    elif test >= 80:
        grade = "B"
    elif test >= 70:
        grade = "C"
    elif test >= 60:
        grade = "D"
    else:
        grade = "F"

    if grade == "A":
        word = "an"
    else:
        word = "a"

    return word + " " + grade


print("you got " + str(score) + " out of 3 correct. you got " + str(3 - score) + " incorrect. you got " + str(
    int((score / 3) * 100)) + "%. your letter grade is " + str(
    give_grade(int((score / 3) * 100)) + " \nthanks for playing!"))

name1 = input("what is your name? ")
test1 = float(input("what is your 1st test score? "))
test2 = float(input("second? "))
test3 = float(input("third? "))


def give_grade(test, name):
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

    print(name + ", your grade is " + word + " " + grade + ". (" + str(avg) + "%)")


avg = (test1 + test2 + test3) / 3
give_grade(avg, name1)

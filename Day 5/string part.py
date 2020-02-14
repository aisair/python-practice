string = input("input string: ")
start_num = int(input("input start num: "))
end_num = int(input("input end num: "))


def calculate_string(str, start, end):
    if start >= len(str) or end >= len(str) + 1:
        result = "not possible"
    else:
        result = str[start:end]
    return result


print(calculate_string(string, start_num, end_num))

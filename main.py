# Напиши программу, которая принимает список оценок студентов по предмету (целые числа от 2 до 5). Нужно определить:
# Средний балл группы.
# Количество отличников (оценка 5).
# Есть ли в списке хотя бы одна двойка.

string = input("enter grades one by one and divide by spacebar: ")
string = string.split()
string = list(map(int, string))


def average(lst: list):
    return sum(lst) / len(lst)


def aces(lst: list):
    return lst.count(5)


def anyFs(lst: list):
    if lst.count(2) == 0:
        return "No Fs"
    else:
        return "There is an F"


print(average(string))
print(aces(string))
print(anyFs(string))

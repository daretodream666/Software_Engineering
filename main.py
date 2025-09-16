even_array = [2, 4, 6, 8, 9]
flag = False

for value in even_array:
    if value % 2 == 1:
        flag = True

if flag:
    print("есть нечётное")
else:
    print("все числа чётные")

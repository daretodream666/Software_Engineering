list_1 = [1, 1, 3, 3, 1]
list_2 = [5, 5, 5, 5, 5, 5, 5]
list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]


def change_list(lst: list):
    lst_set = set(lst)  # {1,3} = [1,1,3,3,1]
    cool_set = set()  # {}, пустой сет
    for item in lst_set:  # проходим по каждому в {1,3}
        iterator = lst.count(item)  # считаем сколько раз встречается 1(3); 3(2)
        for i in range(
            1, iterator + 1
        ):  # господи кто придумал начинать range с 0 И ПРИ ЭТОМ СТОП НАДО ПРОПИСЫВАТЬ +1
            if i == 1:
                cool_set.add(item)
            else:
                cool_set.add(f"{item}" * i)
    return cool_set


print(change_list(list_1))
print(change_list(list_2))
print(change_list(list_3))

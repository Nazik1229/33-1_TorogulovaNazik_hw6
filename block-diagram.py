def binary_search(list1, val):
    n = len(list1)
    result_ok = False
    first = 0
    last = n - 1
    pos = -1

    while first < last:
        middle = (first + last) // 2

        if val == list1[middle]:
            first = middle
            last = first
            result_ok = True
            pos = middle
        elif val > list1[middle]:
            first = middle + 1
        else:
            last = middle - 1

    if result_ok:
        print("Элемент найден", val, "на позиции", pos)
    else:
        print("Элемент не найден")


list1 = list(range(0, 5001))
value_find = 789

binary_search(list1, value_find)
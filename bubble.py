def bubble_search(list1):
    n = len(list1)
    for i in range(n):
        for j in range(0, n - 1 - i):
            if list1[j] > list1[j + 1]:
                list1[j], list1[j + 1] = list1[j + 1], list1[j]


unsort_list = [8, 34, 2, 56, 32, 95, 4, 1]

bubble_search(unsort_list)
print(unsort_list)

list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 6, 8, 10]
res_list = []
for i in range (0, len(list1)):
    res_list.append(list1[i] + list2[i])
    print(res_list)
list1 = [10, 20, 23,11,17]
list2 = [13,43,24,36,12]
list_3 = [i for i in list1 if not i%2==0]+[j for j in list2 if j%2==0]
print(list_3)
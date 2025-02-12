def common_elements(list1, list2):
    return list(set(list1) & set(list2))

list1 = [1,2,3,4,5,6]
list2 = [4,5,6,7,8,]

result = common_elements(list1, list2)
print(result)
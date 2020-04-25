task_list = [(1,1,1), (1,2,3), (-1,-1,7), (-3,-2,8), (0,0,0), (3,-4,-5)]
sorted_list1 = sorted(task_list, key = sum)
print(sorted_list1)
sorted_list2 = sorted(task_list, key = lambda x: x[2])
print(sorted_list2)
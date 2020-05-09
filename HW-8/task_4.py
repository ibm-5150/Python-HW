task_dict = {'b':3, 'c':2, 'a':4, 'd':1}

alphabet_sort = sorted(task_dict, key=lambda x: x[0])
print(alphabet_sort)

numeric_sort = {k: v for k, v in sorted(task_dict.items(), key=lambda item: item[1])}
print(numeric_sort)
#https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
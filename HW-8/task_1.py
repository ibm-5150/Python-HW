import random
#---------------------------------------------
list_with_numbers = list(range(10))
new_list = []

for i in list_with_numbers:
    if not i%2:
        new_list.append(i + random.random())
  
print(new_list)
#---------------------------------------------
#task_1
list_with_numbers = list(range(10))
new_list = [int(x) + random.random() for x in list_with_numbers if not x%2]
print(new_list)




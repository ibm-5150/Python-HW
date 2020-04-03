n = 0

border_dict = dict()
while True:
	print("\nPerson who crosses the border: ")
	name = input("\n>>>")
	n = n + 1
	if name == 'end':
		break
	else:
		border_dict.update({name : n})
for x in border_dict:
	y = border_dict.count(x)
	print(f"{x} - {y}") 

#https://stackoverflow.com/questions/6416131/add-a-new-item-to-a-dictionary-in-python
#https://stackoverflow.com/questions/5904969/how-to-print-a-dictionarys-key
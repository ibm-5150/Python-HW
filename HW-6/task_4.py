with open('base_6.txt', encoding='utf-8') as data_base:
	data_list = [lines.strip('\n').split('|') for lines in data_base.readlines()]

print('All products with apple aroma: ')

for x in data_list:
	for y in x:
		if 'яблок' in y:
			print(f'\n{y}')





















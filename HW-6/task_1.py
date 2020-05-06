#data dictionary

data_dict = dict()
with open('base_6.txt', encoding='utf-8') as data_base:
	for lines in data_base:
		data_lines = lines.strip('\n').split('|')
		data_dict[data_lines[0]] = data_lines[1:]
del data_dict['Артикул']

#data list

with open('base_6.txt', encoding='utf-8') as data_base:
	data_list = [lines.strip('\n').split('|') for lines in data_base.readlines()]
#--------------------------------------------------------------------------------------

#Task 1

#1.1 (amount of products)
product_amount = len(data_list) - 1
print(f"Total amount of products: {product_amount}")

#1.2 (amount of available products)
available_tmp = []
for x in data_list:
	for y in x:
		if 'В наличии' in y:
			available_tmp.append(y)
available_products = len(available_tmp)
print(f"Total amount of available products: {available_products}")

#1.3 (product with the maximum price)
max_dict = dict()
for key, value in data_dict.items():
	tmp_price = value[-1].split()
	product_price = tmp_price[0]
	value[-1] = int(product_price)
	
max_price = max(data_dict.items(), key = lambda price_list: price_list[1][-1] )
print(f"A product with the maximum price is: {max_price}")

#--------------------------------------------------------------------------------------
import pickle
import json

#Task 2

#2.1 (dict; key = vendor code, value = list: name, availability, price)
data_dict = dict()
with open('base_6.txt', encoding='utf-8') as data_base:
	for lines in data_base:
		data_lines = lines.strip('\n').split('|')
		data_dict[data_lines[0]] = data_lines[1:]
del data_dict['Артикул']

#2.2 (pickle serialization)
with open('data_base.pickle', 'wb') as pickle_data:
	pickle.dump(data_dict, pickle_data)

with open('data_base.pickle', 'rb') as pickle_test:
	pickle_test = pickle.load(pickle_test)
#print(test_read)	

#2.3 (json serialization)
with open('data_base.json', 'w') as json_data:
	json.dump(data_dict, json_data)

with open('data_base.json', 'r') as json_data:
	json_test = json.load(json_data)
#print(json_test)


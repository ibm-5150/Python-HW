import json

with open('data_base.json') as json_data:
	data = json.load(json_data)
	prompt = input("Insert vendor code: ")
	prompt_result = json.dumps(data[prompt],  ensure_ascii=False).encode('utf-8')	#https://stackoverflow.com/questions/18337407/saving-utf-8-texts-in-json-dumps-as-utf8-not-as-u-escape-sequence
	prompt_print = prompt_result.decode()
print(prompt_print)




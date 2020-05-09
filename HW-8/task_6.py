import json

#NOT FINISHED

def hello_function():
	hello = 'Hello, World!'
	return print(hello)

hello_function()


#def json_modifier:
#	def wrapper:

with open('modifier.json', 'w') as modifier:
	json.dump(hello_function(), modifier)
with open('modifier.json', 'r') as modified:
	data = json.load(modified)
	result = json.dumps(data)
print(result)


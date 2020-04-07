#\ / : * ? " < > |

try:
	file_name = input()
	file = open(file_name, "w")
	file.close()
except PermissionError:
	print("A file name can't contain any of the following characters:" + '\n\\ / : * ? " < > |')
except OSError:
	print("A file name can't contain any of the following characters: " + '\n\\ / : * ? " < > |')




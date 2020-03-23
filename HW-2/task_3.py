# a = str(input())
# b = ord(a) - 1
# c = chr(b)
#print(c)

char = str(input())
prev_c = chr(ord(char) - 1)
next_c = chr(ord(char) + 1)
print("Previous character: " + str(prev_c) + " Next character: " + str(next_c))
string = "two words"
#or string = str(input())...
s = string.find(" ")
w_1 = string[s:]
w_2 = string[:s]
#r = ''.join(reversed(w_1))
#print(r)

w_1_l = len(w_1)
w_1_r = w_1[w_1_l::-1]

w_2_l = len(w_2)
w_2_r = w_2[w_2_l::-1]

print(w_1_r + " " + w_2_r)

password = str(input())

passowrd_strength = bool(len(password) >= 8 and password.count('@') >= 1 or password.count('#') >= 1)
print("Password is strong: " + str(passowrd_strength))

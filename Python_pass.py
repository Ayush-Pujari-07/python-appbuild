password = input("enter the password: ")

result = []


if len(password) >= 8:
    result.append(True)
else:
    result.append(False)
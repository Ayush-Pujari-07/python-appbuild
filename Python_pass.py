def check_passord():
    password = input("Enter the password: ")

    result = []

    if len(password) >= 8:
        result.append(True)
    else:
        result.append(False)

    # Check if it has digit
    digit = False
    for i in password:
        if i.isdigit():
            digit = True

    result.append(digit)

    # Check if it has uppercase
    uppercase = False
    for i in password:
        if i.isupper():
            uppercase = True

    result.append(uppercase)

    # Check if it has all
    if all(result):
        print("Strong Password!!")
    else:
        print("Weak Password!!")


disct = {"apple": "tstu", "car": "asda", "asdf": "asdaweq", "asdooaf": 112, "open": 123, "pass": 1243, "pole": "pipe"}

for i in disct:
    print(disct[i])

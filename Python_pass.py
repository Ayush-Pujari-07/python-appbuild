def check_passord():
    password = input("Enter the password: ")

    result = {}

    if len(password) >= 8:
        result["length"] = True
    else:
        result["length"] = False

    # Check if it has digit
    digit = False
    for i in password:
        if i.isdigit():
            digit = True

    result["digit"] = digit

    # Check if it has uppercase
    uppercase = False
    for i in password:
        if i.isupper():
            uppercase = True

    result["Upper-case"] = uppercase

    # Check if it has all
    if all(result.values()):
        print("Strong Password!!")
    else:
        print("Weak Password!!")


# check_passord()

ids = ["XF345_89", "XER76849", "XA454_55"]

x = 0

for id in ids:
    if '_' in id:
        x = x + 1
print(x)

length = float(input("Enter length: "))
width = float(input("Enter width: "))

perimeter = (length + width) * 2
area = length * width

print("Perimeter is", perimeter)
print("Area is", area)

if perimeter < 14 and area < 8:
    print("OK")
else:
    print("NOT OK")

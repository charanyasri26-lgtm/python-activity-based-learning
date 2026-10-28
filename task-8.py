password = input("Enter password: ")

upper = False
lower = False
digit = False

for ch in password:
    if ch.isupper():
        upper = True
    elif ch.islower():
        lower = True
    elif ch.isdigit():
        digit = True

if len(password) >= 8 and upper and lower and digit:
    print("Valid Password")
else:
    print("Invalid Password")

    if len(password) < 8:
        print("Password must have 8 characters")
    if not upper:
        print("Add an uppercase letter")
    if not lower:
        print("Add a lowercase letter")
    if not digit:
        print("Add a digit")

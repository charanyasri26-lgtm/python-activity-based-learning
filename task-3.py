attended = int(input("Enter classes attended: "))
total = int(input("Enter total classes: "))

percentage = attended / total * 100

print("Attendance Percentage =", percentage)

if percentage >= 75:
    print("Eligible for Examination")
else:
    print("Not Eligible")

    required = 0
    while (attended + required) / (total + required) * 100 < 75:
        required = required + 1

    print("More classes to attend =", required)

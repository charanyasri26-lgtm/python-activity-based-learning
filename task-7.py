offence = input("Enter offence (helmet/signal): ")
repeat = input("Is it a repeat offence? (yes/no): ")

if offence == "helmet":
    fine = 500
elif offence == "signal":
    fine = 1000
else:
    fine = 0

if repeat == "yes" and fine > 0:
    fine = fine * 2

if fine == 0:
    print("Invalid Offence")
else:
    print("Traffic Fine =", fine)

    if repeat == "yes":
        print("Repeat Offence")
        print("Check for Disqualification")

age = int(input("Enter patient age: "))
consultation = int(input("Enter consultation fee: "))
treatment = int(input("Enter treatment fee: "))

bill = consultation + treatment

if age >= 60:
    bill = bill - bill * 0.10

print("Final Hospital Bill =", bill)

if age >= 60:
    print("Patient Category: Senior Citizen")
else:
    print("Patient Category: Regular")

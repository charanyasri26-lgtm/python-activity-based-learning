prepared = [100, 120, 80]
served = [90, 100, 60]

for i in range(len(prepared)):
    leftover = prepared[i] - served[i]
    percentage = leftover / prepared[i] * 100

    print("\nDay", i + 1)
    print("Prepared Meals:", prepared[i])
    print("Served Meals:", served[i])
    print("Leftover Meals:", leftover)
    print("Wastage Percentage:", percentage)

    if percentage > 20:
        print("High Food Waste")
    else:
        print("Acceptable Food Waste")

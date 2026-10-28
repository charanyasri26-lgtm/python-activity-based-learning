products = ["Rice", "Sugar", "Oil"]
opening = [50, 30, 20]
incoming = [20, 10, 5]
dispatched = [60, 25, 22]

for i in range(len(products)):
    closing = opening[i] + incoming[i] - dispatched[i]

    print("\nProduct:", products[i])
    print("Closing Stock:", closing)

    if closing < 10:
        print("Replenishment Required")
    else:
        print("Stock Available")

name = None
price = None
quantity = None
units = None
i = 1
structure = []
analytics = {"Name": [], "Price": [], "Quantity": [], "Units": []}
while i > 0:
    print("If you want to add new product, enter 'Add'.",
              "If you want to view structure, enter 'Structure'.",
              "If you want to view analytics, enter 'Analytics'.",
              "If you want to finish the work, enter 'Exit': ", sep='\n')
    x = input().title()
    if x == "Add":
        name = input("Enter name of product: ")
        price = input("Enter product price: ")
        quantity = input("Enter product quantity: ")
        units = input("Enter product units: ")
        structure.append((i, {"Name": name, "Price": price, "Quantity": quantity, "Units": units}))
        analytics["Name"].append(name)
        analytics["Price"].append(price)
        analytics["Quantity"].append(quantity)
        analytics["Units"].append(units)
        i += 1
    elif x == "Structure":
        for product in structure:
            print(product)
    elif x == "Analytics":
        for category in analytics:
            print(category + ": " + str(analytics[category]))
    elif x == "Exit":
        break
    else:
        print("Error! Please, try again.")
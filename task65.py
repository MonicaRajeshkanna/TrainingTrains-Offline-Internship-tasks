products = {
    "Laptop":["Mouse","Keyboard"],
    "Phone":["Charger","Earphones"]
}

item = input("Enter Product: ")

print(products.get(item,"No Recommendation"))
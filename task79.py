history = {
    "Laptop":["Laptop Bag","Mouse"],
    "Shoes":["Socks","Shoe Polish"]
}

item = input("Purchased Item: ")

print(history.get(item,"No Suggestions"))
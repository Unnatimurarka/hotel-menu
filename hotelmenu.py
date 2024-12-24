menu = {
    'Pizza': 40,
    'Pasta': 50,
    'Burger': 60,
    'Salad': 70,
    'Coffee': 80,
}

print(menu)
print("WELCOME TO PYTHON RESTAURANT")
print("Pizza: Rs40\nPasta: Rs50\nBurger: Rs60\nSalad: Rs70\nCoffee: Rs80")

order_total = 0

# First item order
item_1 = input("Enter the name of the item you want to order: ")
if item_1 in menu:
    total_order += menu[item_1]
    print(f"Your item {item_1} has been added to your order.")
else:
    print(f"Ordered item {item_1} is not available yet.")

# Ask for another order
another_order = input("Do you want to add another item? (Yes/No): ")
if another_order.lower() == "yes":
    item_2 = input("Enter the name of the second item: ")
    if item_2 in menu:
        total_order += menu[item_2]
        print(f"Item {item_2} has been added to your order.")
    else:
        print(f"Ordered item {item_2} is not available!")

# Print the total amount
print(f"The total amount of the items is Rs{total_order}.") 
import sys

inventory = [
    {"name": "banana", "price": 2, "quantity": 10, "category": "fruit"},
    {"name": "bread", "price": 5, "quantity": 10, "category": "bakery"},
    {"name": "milk", "price": 4, "quantity": 10, "category": "dairy"},
    {"name": "apple", "price": 2, "quantity": 10, "category": "fruit"},
    {"name": "muffin", "price": 3, "quantity": 10, "category": "bakery"},
    {"name": "ice_cream", "price": 5, "quantity": 10, "category": "dairy"}
]

def add_item():
    name = input("Enter item name: ").lower()
    price = float(input("Enter item price: "))
    quantity = int(input("Enter item quantity: "))
    category = input("Enter item category: ")

    item = {"name": name, "price": price, "quantity": quantity, "category": category}
    inventory.append(item)
    print(f"{name} has been added to inventory!\n")

def update_item():
    name = input("Enter the name of the item to update: ").lower()
    for item in inventory:
        if item ["name"] == name:
            item["price"] = float(input("Enter a new price: "))
            item["quantity"] = int(input("Enter a new quantity: "))
            item["category"] = input("Enter a new category: ").lower()
            print(f"{name} updated successfully!\n")
            return
    print("Item not found.\n")

def view_inventory():
    if not inventory:
        print("Inventory is empty. \n")
        return

    print("Inventory: ")
    for item in inventory:
        print(f"Name:{item['name']}, Price: ${item['price']}, Quantity: {item['quantity']}, Category: {item['category']}")
    print()

def remove_item():
    name = input("Enter the name of the item you wish to remove: ").lower()
    for item in inventory:
        if item["name"] == name:
            inventory.remove(item)
            print(f"{name} removed from inventory.\n")
            return
    print("Item not found!")

def search_by_category():
    category = input("Enter a category to search: ").lower()
    found_items = [item for item in inventory if item["category"] == category]

    if not found_items:
        print("No items found in this category.\n")
        return

    print(f"Items in category: '{category}':")
    for item in found_items:
        print(f"Name:{item['name']}, Price: ${item['price']}, Quantity: {item['quantity']}, Category: {item['category']}")
    print()

while True:
    print("1. Add Item")
    print("2. Update Item")
    print("3. View Inventory")
    print("4. Remove Item")
    print("5. Search by category")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_item()
    elif choice == "2":
        update_item()
    elif choice == "3":
        view_inventory()
    elif choice == "4":
        remove_item()
    elif choice == "5":
        search_by_category()
    elif choice == "6":
        print("Exiting program.")
        sys.exit()
    else:
        print("Invalid Choice.\n")


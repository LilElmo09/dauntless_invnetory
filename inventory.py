import index

def view_inventory():
    print("Inventory:")
    for item in index.inventory:
        print(item)

def add_inventory():
    item = input("Enter the item to add: ")
    index.inventory.append(item)
    print(f"Item '{item}' added.")

def edit_inventory():
    item = input("Enter the item to edit: ")
    if item in index.inventory:
        new_item = input("Enter the new value: ")
        index = index.inventory.index(item)
        index.inventory[index] = new_item
        print(f"Item '{item}' updated to '{new_item}'.")
    else:
        print(f"Item '{item}' not found.")

def delete_inventory():
    item = input("Enter the item to delete: ")
    if item in index.inventory:
        index.inventory.remove(item)
        print(f"Item '{item}' deleted.")
    else:
        print(f"Item '{item}' not found.")

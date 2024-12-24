import inventory as inv

def home():
    while True:
        print("What do you want to do?")
        print("1. View inventory")
        print("2. View items")
        print("3. Exit")
        opcion = input("Option: ")

        if opcion == '1':
            inventory()
        elif opcion == '2':
            items()
        elif opcion == '3':
            print("Exiting...")
            break
        else:
            print("Invalid option")

def inventory():
    while True:
        print("Inventory Options:")
        print("1. View inventory")
        print("2. Add item")
        print("3. Edit item")
        print("4. Delete item")
        print("5. Back to main menu")
        opcion = input("Option: ")

        if opcion == '1':
            inv.view_inventory()
        elif opcion == '2':
            inv.add_inventory()
        elif opcion == '3':
            inv.edit_inventory()
        elif opcion == '4':
            inv.delete_inventory()
        elif opcion == '5':
            break
        else:
            print("Invalid option")

def items():
    pass


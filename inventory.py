from tabulate import tabulate
import reader
# Leer el archivo CSV
raw_inventory = reader.read_csv_to_dict('inventario.csv')

# convertir el formato del inventario
inventory = []
keys = raw_inventory.keys()
for i in range(len(next(iter(raw_inventory.values())))):
    item = {key: raw_inventory[key][i] for key in keys}
    inventory.append(item)

def view_inventory():
    if not inventory:
        print("No items in inventory.")
        return
    
    headers = inventory[0].keys() if inventory else []
    table = [item.values() for item in inventory]
    print(tabulate(table, headers=headers, tablefmt='grid'))


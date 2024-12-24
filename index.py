import reader
import manager_modules as mngr

## Read the CSV files
items = reader.read_csv_to_dict('items.csv')
inventory = reader.read_csv_to_dict('inventario.csv')

mngr.home()

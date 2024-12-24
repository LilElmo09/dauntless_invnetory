import csv

def read_csv_to_dict(FILENAME):
    data = {}
    with open(FILENAME, mode='r', newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            for key, value in row.items():
                if key not in data:
                    data[key] = []
                data[key].append(value)
    return data


import csv

def read_csv(file):
    data = []
    with open(file, newline='', encoding="UTF-8") as csvFile:
        reader = csv.DictReader(csvFile)
        data.extend(list(reader))
    return data
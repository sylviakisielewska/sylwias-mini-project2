import csv

file_path = "/Users/sylwia/Documents/my-reps/sylwias-mini-project2/chicken_database.csv"

def extract_from_file(filepath = file_path):
    data = []
    with open(filepath, newline='',encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data

print(extract_from_file())        
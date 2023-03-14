import csv

def get_csv(filename):
    data = []
    
    with open(filename) as file:
        file_reader = csv.reader(file, delimiter = ',')
        for line in file_reader:
            data.append(line)

    return(data)

def remove_duplicates(data):
    seen_user_ids = set()
    new_data = []
    for row in data:
        user_id = row[0]
        if user_id not in seen_user_ids:
            new_data.append(row)
            seen_user_ids.add(user_id)
    return new_data

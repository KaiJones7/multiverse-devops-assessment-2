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


def ignore_empty_lines(data):
    return [row for row in data if any(row)]

def capitalize_names(data):
    for row in data:
        row[1] = row[1].capitalize()
        row[2] = row[2].capitalize()
    return data

def validate_answer_3(data):
    valid_data = []
    for row in data:
        answer_3 = row[5]
        if (answer_3 is not None) and answer_3 and isinstance(answer_3, str) and answer_3.strip().replace('.', '').isdigit():
            answer_3 = float(answer_3)
            if 1 <= answer_3 <= 10:
                valid_data.append(row)
    return valid_data
import csv, os

def get_csv(filename):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, filename)
    data = []
    
    with open(file_path) as file:
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

def write_clean_data_to_file(input_file, output_file):
    csv_data = get_csv(input_file)

    csv_data = remove_duplicates(csv_data)
    csv_data = ignore_empty_lines(csv_data)
    csv_data = capitalize_names(csv_data)
    csv_data = validate_answer_3(csv_data)

    with open(output_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['user_id', 'first_name', 'last_name', 'answer_1', 'answer_2', 'answer_3'])
        for row in csv_data:
            writer.writerow(row)
  


def print_clean_data(file):
    with open(file) as f:
        reader = csv.DictReader(f)
        print(f"{'user_id':<10} {'First Name':<20} {'Last Name':<20} {'Answer 1':<15} {'Answer 2':<15} {'Answer 3':<15}")
        for row in reader:
            print(f"{row['user_id']:<10} {row['first_name']:<20} {row['last_name']:<20} {row['answer_1']:<15} {row['answer_2']:<15} {row['answer_3']:<15}")
  


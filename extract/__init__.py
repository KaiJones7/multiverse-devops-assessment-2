import csv

def get_csv(filename):
    data = []
    
    with open(filename) as file:
        file_reader = csv.reader(file, delimiter = ',')
        for line in file_reader:
            data.append(line)

    return(data)



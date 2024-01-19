import csv
import tempfile, os
from csvhelper import get_csv, remove_duplicates, ignore_empty_lines, capitalize_names, validate_answer_3, write_clean_data_to_file, print_clean_data


def test_input_is_list():
    #Arrange
    filename = "results.csv"
    expected_output = list

    #Act
    output = get_csv(filename)

    #Assert
    assert type(output) == expected_output


def test_input_is_correct():
    #Arrange
    filename = "results.csv"
    expected_columns = ["user_id","first_name","last_name","answer_1","answer_2","answer_3"]
    expected_row_count = 25

    #Act
    output = get_csv(filename)
    actual_columns = output[0]
    actual_rowcount = len(output[1:])

    #Assert
    assert actual_columns == expected_columns
    assert actual_rowcount == expected_row_count




def test_remove_duplicate():
    data = [
        ['1', 'John', 'Doe', 'Yes', 'No', '5'],
        ['2', 'Jane', 'Doe', 'No', 'Yes', '8'],
        ['1', 'John', 'Doe', 'Yes', 'No', '5'],
        ['4', 'Bob', 'Smith', 'Yes', 'Yes', '9']
    ]
    expected_data = [
        ['1', 'John', 'Doe', 'Yes', 'No', '5'],
        ['2', 'Jane', 'Doe', 'No', 'Yes', '8'],
        ['4', 'Bob', 'Smith', 'Yes', 'Yes', '9']
    ]
    assert remove_duplicates(data) == expected_data


def test_ignore_empty_lines():
    data = [
        ['1', 'John', 'Doe', 'Yes', 'No', '5'],
        ['', '', '', '', '', ''],
        ['2', 'Jane', 'Doe', 'No', 'Yes', '8'],
        ['3', 'Bob', 'Smith', 'Yes', 'Yes', '9'],
        ['', '', '', '', '', '']
    ]
    expected_data = [
        ['1', 'John', 'Doe', 'Yes', 'No', '5'],
        ['2', 'Jane', 'Doe', 'No', 'Yes', '8'],
        ['3', 'Bob', 'Smith', 'Yes', 'Yes', '9']
    ]
    assert ignore_empty_lines(data) == expected_data


def test_capitalize_names():
    data= [
        ['1', 'john', 'Doe', 'Yes', 'No', '5'],
        ['2', 'Jane', 'doe', 'No', 'Yes', '8'],
        ['3', 'Bob', 'smith', 'Yes', 'Yes', '9']
    ]
    expected_data = [
        ['1', 'John', 'Doe', 'Yes', 'No', '5'],
        ['2', 'Jane', 'Doe', 'No', 'Yes', '8'],
        ['3', 'Bob', 'Smith', 'Yes', 'Yes', '9']
    ]
    assert capitalize_names(data) == expected_data

def test_validate_answer_3():
    data= [
            ['1', 'john', 'Doe', 'Yes', 'No', '5'],
            ['2', 'Jane', 'doe', 'No', 'Yes', '8'],
            ['3', 'Bob', 'smith', 'Yes', 'Yes', '11'],
            ['4', 'john', 'Doe', 'Yes', 'No', 'invalid'],
            ['5', 'Jane', 'doe', 'No', 'Yes', ''],
            ['6', 'Bob', 'smith', 'Yes', 'Yes', '7.5']
    ]
    expected_data = [
    
            ['1', 'john', 'Doe', 'Yes', 'No', '5'],
            ['2', 'Jane', 'doe', 'No', 'Yes', '8'],
            ['6', 'Bob', 'smith', 'Yes', 'Yes', '7.5']
     ]
    assert validate_answer_3(data) == expected_data


def test_write_clean_data_to_file():
    csv_data = "user_id,first_name,last_name,answer_1,answer_2,answer_3\n1,john,doe,Yes,No,5\n2,jane,doe,No,Yes,8\n"
    expected_output = "user_id,first_name,last_name,answer_1,answer_2,answer_3\n1,John,Doe,Yes,No,5\n2,Jane,Doe,No,Yes,8\n"

    with tempfile.NamedTemporaryFile(mode="w", delete=False) as input_file:
        input_file.write(csv_data)

    with tempfile.NamedTemporaryFile(mode="w", delete=False) as output_file:
        write_clean_data_to_file(input_file.name, output_file.name)

        with open(output_file.name, mode="r") as f:
            output_data = f.read()

            assert output_data == expected_output

def test_print_clean_data(capsys):
    csv_data = "user_id,first_name,last_name,answer_1,answer_2,answer_3\n1,John,Doe,Yes,No,5\n2,Jane,Doe,No,Yes,8\n"
    with tempfile.NamedTemporaryFile(mode="w", delete=False) as f:
        f.write(csv_data)
        csv_file_path = f.name
    expected_output = '''user_id    First Name           Last Name            Answer 1        Answer 2        Answer 3       
1          John                 Doe                  Yes             No              5              
2          Jane                 Doe                  No              Yes             8              
'''
    print_clean_data(csv_file_path)
    captured = capsys.readouterr()
    assert captured.out == expected_output

    data = [
        ['user_id', 'first_name', 'last_name', 'answer_1', 'answer_2', 'answer_3'],
        ['1', 'john', 'Doe', 'Yes', 'No', '5'],
        ['3', 'Bob', 'smith', 'Yes', 'Yes', '11'],
        ['4', 'john', 'Doe', 'Yes', 'No', 'invalid'],
        ['5', 'Jane', 'doe', 'No', 'Yes', '4'],
        ['5', 'Jane', 'doe', 'No', 'Yes', '10'],
        ['', '', '', '', '', '']
    ]

    expected = [
        ['user_id', 'first_name', 'last_name', 'answer_1', 'answer_2', 'answer_3'],
        ['1', 'John', 'Doe', 'Yes', 'No', '5'],
        ['5', 'Jane', 'Doe', 'No', 'Yes', '4']
    ]

    with tempfile.NamedTemporaryFile(mode='w', delete=False, newline='') as temp_file_input:
        writer = csv.writer(temp_file_input)
        writer.writerows(data)

    with tempfile.NamedTemporaryFile(mode='w', delete=False, newline='') as temp_file_expected:
        writer = csv.writer(temp_file_expected)
        writer.writerows(expected)

    with tempfile.NamedTemporaryFile(mode='w', delete=False, newline='') as temp_file_output:

        write_clean_data_to_file(temp_file_input.name,temp_file_output.name)

    with open(temp_file_output.name) as f:
        output_data = list(csv.reader(f))

    with open(temp_file_expected.name) as f:
        expected_data = list(csv.reader(f))

    assert output_data == expected_data

    os.remove(temp_file_input.name)
    os.remove(temp_file_output.name)
    os.remove(temp_file_expected.name)
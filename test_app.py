from extract import get_csv, remove_duplicates, ignore_empty_lines, capitalize_names, validate_answer_3

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

import os

def count_lines(file):
    list_of_lines = file.readlines()
    return len(list_of_lines) 

def count_chars(file):
    file_into_string = file.read()
    return len(file_into_string)


def test(name):
    try:
        with open(name, 'r') as file:
            lines_number =count_lines(file)
            file.seek(0)
            chars_number = count_chars(file)
    except FileNotFoundError:
        name = os.path.abspath(name)
        with open(name, 'r') as file:
            lines_number =count_lines(file)
            file.seek(0)
            chars_number = count_chars(file)

    print(f'In this file {lines_number} lines.')
    print(f'In this file {chars_number} chars.')


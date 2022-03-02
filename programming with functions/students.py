from cgitb import text
import csv
def read_dict(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    text_dict = {}

    with open(filename, "rt") as csv_file:
        reader = csv.reader(filename)

        next(reader)
        for row_list in reader:
            key = row_list[key_column_index]
            text_dict[key] = row_list

        return text_dict

def main():
    I_num_index = 0

    dictionary = read_dict('students.csv', I_num_index)

    
        






if __name__ == "__main__":
    main()
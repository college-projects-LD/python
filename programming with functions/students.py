import csv
 
def main():
 
    # Create variable to hold the key index of the dictionary.
    KEY_COLUMN_INDEX = 0
 
    # Call the read_dict function to read the contents of
    # a CSV file and add values to a compound dictionary.
    compound_dict = read_dict("programming with functions\students.csv", KEY_COLUMN_INDEX)
 
    i_number = input("Enter your I-Number: ")
 
    # Check if student is in the student_dict dictionary with
    # an IF/ELSE statement.
    if i_number in compound_dict:
        print(compound_dict[i_number])
    else:
        print("No such student.")
 
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
    # Create an empty dictionary to hold the contents of the
    # CSV file.
    students_dict = {}
 
    # Open the text file to read its contents.
    with open(filename, "rt") as csv_file:
 
        # Use the csv module to create a reader object
        # that will read from the opened CSV file.
        csv_reader = csv.reader(csv_file)
 
        # The first row of the CSV file contains column
        # headings and not data, so this statement skips
        # the first row of the CSV file.
        next(csv_reader)
 
        # Read through the contents of the file in a
        # for loop and add each row to the dictionary.
        for line in csv_reader:
 
            # Retrieve the key of the dictionary for each row.
            key = line[key_column_index]
 
            # Retrieve the value of the dictionary for each key.
            students_dict[key] = line[1]
        
        # Return the new dictionary.
        return students_dict
 
# Call main to start this program.
if __name__ == "__main__":
    main()






        






# if __name__ == "__main__":
#     main()
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
    product_dict = {}
 
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
            product_dict[key] = line[1]
        
        # Return the new dictionary.
        return product_dict

def main():
 
    # Create variable to hold the key index of the dictionary.
    KEY_COLUMN_INDEX = 0
    PRODUCT_COLUMN_INDEX = 0
    QUANTITY_COLUMN_INDEX =1
    # Call the read_dict function to read the contents of
    # a CSV file and add values to a compound dictionary.
    productsDict = read_dict("programming with functions\products.csv", KEY_COLUMN_INDEX)
 
    print(productsDict)
    # Check if student is in the student_dict dictionary with
    # an IF/ELSE statement.
    with open("programming with functions\\request.csv", "rt") as request_file:
        reader = csv.reader(request_file)

        next(reader)
        W112_num = 0
        D083_num = 0
        W231_num = 0
        C013_num = 0
        D083_num = 0
        for row_list in reader:
            Product = row_list[PRODUCT_COLUMN_INDEX]
            Quantity= int(row_list[QUANTITY_COLUMN_INDEX])
            if Product in productsDict:
                print(productsDict[1] , Quantity , productsDict[2])




if __name__ == "__main__":
    main()
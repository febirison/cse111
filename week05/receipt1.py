# receipt.py
# This assignment was done by Anderson Okai

import csv

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.
    
    Parameters:
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    products_dict = {}
    
    # Open the CSV file for reading
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header line
        for row in reader:
            # Use the specified column as the key
            key = row[key_column_index]
            # Store the entire row as the value
            products_dict[key] = row
    
    return products_dict

def main():
    """Main function to execute the program."""
    filename = "products.csv"
    products_dict = read_dictionary(filename, 0)
    
    # Print the products dictionary
    print("All Products")
    print(products_dict)
    
    # Open the request.csv file for reading
    with open("request.csv", 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header line
        
        print("Requested Items")
        for row in reader:
            product_number = row[0]
            quantity = int(row[1])
            
            # Find the corresponding item in the products_dict
            product_info = products_dict[product_number]
            product_name = product_info[1]
            product_price = float(product_info[2])
            
            # Print the product name, requested quantity, and product price
            print(f"{product_name}: {quantity} @ {product_price:.2f}")

# Protect the call to main
if __name__ == "__main__":
    main()

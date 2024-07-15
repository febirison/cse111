##
# Date: 2024-07-12
# File: receipt.py
# Author: Anderson Okai
# Class: CSE 111
# Purpose: 10 Prove Milestone: Handling Exceptions
# Prove that you can write a Python program that 
# handles exceptions, including FileNotFoundError, 
# PermissionError, and KeyError.
# Bold ANSI sequences for formatting output text
# Store name formatted with bold and centered text
# Header for receipt columns
# Footer message indicating customer copy
# Generate and print a random coupon for the next purchase
##


import csv
from datetime import datetime
import random

# Bold ANSI codes for styling
bold_s = '\033[1m'
bold_e = '\033[0m'

# Store name and receipt headers
store_name = (f''' 
{"*":*^50}
{bold_s}*{"Welcome to Anderson Groups Of Company":^48}*{bold_e}
{"*":*^50}\n''')

header = (f'''{bold_s}{"Item":<18}{"Quantity":<10}{"Price":<10}{"Subtotal"}{bold_e}''')

thank_you_message = (f'''{"":<8}{"Thank You for Shopping With Us!"}''')

footer_message = (f'''\n{"":<13}{"*** CUSTOMER COPY ***"}\n''')

# Get the current date and time
current_date_and_time = datetime.now()
time_stamp = (f'''{"":<12}{current_date_and_time:%a %b %d %H:%M:%S %Y}\n''')
day_of_week = current_date_and_time.weekday()
current_time = current_date_and_time.strftime("%H:%M:%S")

def main():
    try:
        PRODUCT_INDEX = 0
        NAME_INDEX = 1
        PRICE_INDEX = 2
        QUANTITY_INDEX = 1

        # Read products.csv into a dictionary
        products_dict = read_dict("products.csv", PRODUCT_INDEX)

        # Read request.csv into a list
        request_list = read_list("request.csv")

        print(store_name)
        print(header)

        coupon_list = []
        items_sold = 0
        sub_total = 0

        for pn in request_list:
            product_number = pn[PRODUCT_INDEX]
            quantity = pn[QUANTITY_INDEX]
            
            if product_number in products_dict:
                name = products_dict[product_number][NAME_INDEX]
                price = products_dict[product_number][PRICE_INDEX]

            items_sold += int(quantity)
            quantity_sub_total = (int(quantity) * float(price))
            sub_total += quantity_sub_total

            coupon_list.append(products_dict[product_number][NAME_INDEX])

            # Print product details
            print(f"""{name:<20} {quantity:<5} @ ${price:<8} ${quantity_sub_total:,.2f}""")
        
        # Print subtotal
        print(f'''\n{"":<28}{"SUBTOTAL":<10} ${sub_total:,.2f}''')

        # Apply day of week discount
        if (day_of_week == 1 or day_of_week == 2):
            discount = round(sub_total * 0.10, 2)
            sub_total -= discount
            print(f'''{"":<12}{"Day of the Week Discount":<26} ${discount:,.2f}''')

        # Apply time of day discount
        if ((day_of_week != 1 and day_of_week != 2) and current_time < "11:00:00"):
            discount = round(sub_total * 0.10, 2)
            sub_total -= discount
            print(f'''{"":<12}{"Time of Day Discount":<26} ${discount:,.2f}''')

        # Compute and print sales tax
        tax_rate = .06
        sales_tax_total = sub_total * tax_rate
        print(f'''{"":<18}{"Sales Tax":<12}{"@ 6%":<8} ${sales_tax_total:,.2f}''')

        # Compute and print total amount due
        total = sub_total + sales_tax_total
        print(f'''{"":<28}{"TOTAL":<10} ${total:,.2f}''')

        # Print total items sold
        print(f'''\n{"":<15}{"# ITEMS SOLD":<5} {items_sold}\n''')

        # Generate and print a coupon for a random item
        coupon_item = coupon_code(coupon_list)
        print(f"""\n{"":<5}{"25% Off Next Purchase of "}{coupon_item.title()}\n""")

        print(thank_you_message)
        print(time_stamp)
        print(footer_message)

    except (FileNotFoundError, PermissionError) as error:
        print()
        print(type(error).__name__, error, sep=": ")
        print("Please choose a different file.\n")
        
    except KeyError as error:
        print()
        print(type(error).__name__, error, sep=": ")
        print("Unknown product ID in the request.csv file\n")

def read_dict(filename, key_column_index):
    """Read the contents of a CSV file into a compound dictionary and return the dictionary.
    
    Parameters:
        filename: the name of the CSV file to read.
        key_column_index: the index of the column to use as the keys in the dictionary.
    
    Return: a compound dictionary that contains the contents of the CSV file.
    """
    dictionary = {}

    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        
        for row_list in reader:
            if len(row_list) != 0:
                key = row_list[key_column_index]
                dictionary[key] = row_list

    return dictionary

def read_list(filename):
    """Read the contents of a text file into a list and return the list. Each element in the list will contain one line of text from the text file.
    
    Parameter filename: the name of the text file to read
    Return: a list of strings
    """
    request_list = []

    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        
        for line in reader:
            request_list.append(line)

    return request_list

def coupon_code(list):
    """Get the unique values from request.csv.
    
    Parameter:
        list: a list of all the values from request.csv
    
    Return: a random item from unique_list
    """
    unique_list = []
    
    for x in list:
        if x not in unique_list:
            unique_list.append(x)

    return random.choice(unique_list)

if __name__ == "__main__":
    main()

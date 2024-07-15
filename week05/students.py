# students.py
# This assignment was done by Anderson Okai

def main():
    """Main function to execute the program."""
    filename = "students.csv"
    students_dict = read_dictionary(filename, 0)
    
    # Prompt the user to enter an I-Number
    user_inumber = input("Please enter an I-Number (xxxxxxxxx): ").replace("-", "")
    
    # Validate the I-Number entered by the user
    if not user_inumber.isdigit():
        print("Invalid I-Number")
    elif len(user_inumber) != 9:
        if len(user_inumber) < 9:
            print("Invalid I-Number: too few digits")
        else:
            print("Invalid I-Number: too many digits")
    else:
        # Look up the I-Number in the dictionary and print the student's name
        student_name = students_dict.get(user_inumber, None)
        if student_name:
            print(student_name)
        else:
            print("No such student")

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound dictionary and return the dictionary.
    
    Parameters:
        filename: the name of the CSV file to read.
        key_column_index: the index of the column to use as the keys in the dictionary.
    
    Return: a compound dictionary that contains the contents of the CSV file.
    """
    students_dict = {}
    
    # Open the CSV file for reading
    with open(filename, 'r') as file:
        next(file)  # Skip the header line
        for line in file:
            parts = line.strip().split(',')
            key = parts[key_column_index]
            value = parts[1]
            students_dict[key] = value
    
    return students_dict

if __name__ == "__main__":
    main()

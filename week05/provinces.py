def main():
    # Open the file for reading
    with open("week05\provinces.txt", "rt") as file:
        # Read the contents into a list
        provinces_list = file.readlines()
        
    # Strip newline characters from each element
    provinces_list = [line.strip() for line in provinces_list]

    # Print the entire list
    print(provinces_list)
    
    # Remove the first element
    provinces_list.pop(0)
    
    # Remove the last element
    provinces_list.pop()

    # Replace all occurrences of "AB" with "Alberta"
    provinces_list = ["Alberta" if province == "AB" else province for province in provinces_list]

    # Count occurrences of "Alberta"
    alberta_count = provinces_list.count("Alberta")

    # Print the modified list
    print(provinces_list)
    
    # Print the number of occurrences of "Alberta"
    print(f"Alberta occurs {alberta_count} times in the modified list.")

# Call main to execute the program
if __name__ == "__main__":
    main()

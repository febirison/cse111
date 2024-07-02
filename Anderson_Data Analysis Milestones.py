# Load the data from the CSV file
with open("life-expectancy.csv") as file:
    next(file)  # Skip the header row
    data = [line.strip().split(",") for line in file]

# Function to calculate the average life expectancy for a given year
def average_life_expectancy(year):
    # Filter data for the given year and calculate the average
    filtered_data = [float(row[3]) for row in data if row[2] == year]
    if filtered_data:
        return sum(filtered_data) / len(filtered_data)
    else:
        return None

# Function to find the country with the minimum and maximum life expectancies for a given year
def min_max_life_expectancy(year):
    # Filter data for the given year
    filtered_data = [row for row in data if row[2] == year]
    if filtered_data:
        # Find the country with the minimum and maximum life expectancies
        min_country = min(filtered_data, key=lambda x: float(x[3]))
        max_country = max(filtered_data, key=lambda x: float(x[3]))
        return min_country, max_country
    else:
        return None, None

# Function to find the overall minimum and maximum life expectancies
def overall_min_max_life_expectancy():
    # Find the row with the minimum and maximum life expectancies
    min_row = min(data[1:], key=lambda x: float(x[3]))
    max_row = max(data[1:], key=lambda x: float(x[3]))
    return min_row, max_row

# Main program
if __name__ == "__main__":
    # Overall min and max life expectancies
    overall_min, overall_max = overall_min_max_life_expectancy()
    print(f"The overall min life expectancy is: {overall_min[3]} from {overall_min[0]} in {overall_min[2]}")
    print(f"The overall max life expectancy is: {overall_max[3]} from {overall_max[0]} in {overall_max[2]}")

    # User input for the year of interest
    year = input("Enter the year of interest: ")
    avg_life_exp = average_life_expectancy(year)
    if avg_life_exp is not None:
        print(f"The average life expectancy across all countries for the year {year} was: {avg_life_exp:.2f}")

        # Country with min and max life expectancies for the given year
        min_country, max_country = min_max_life_expectancy(year)
        if min_country and max_country:
            print(f"The min life expectancy for the year {year} was: {min_country[3]} from {min_country[0]}")
            print(f"The max life expectancy for the year {year} was: {max_country[3]} from {max_country[0]}")
        else:
            print("No data available for the specified year.")
    else:
        print("No data available for the specified year.")

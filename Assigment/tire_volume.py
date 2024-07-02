import math
from datetime import datetime

def calculate_tire_volume(width, aspect_ratio, diameter):
    # Calculate volume using the provided formula
    volume = math.pi * width**2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter) / 10000000000
    return volume

def get_tire_price(width, aspect_ratio, diameter):
    # Add your code here to find the tire price based on the tire specifications
    # This is just a placeholder
    # Replace this with your actual logic to find the tire price
    return "$150"  # Placeholder price

def main():
    # Get input from the user
    print("Welcome to the Tire Volume Calculator!")
    print("Please enter the specifications of your tire:")
    width = float(input("Enter the width of the tire in mm (ex 205): "))
    aspect_ratio = float(input("Enter the aspect ratio of the tire (ex 60): "))
    diameter = float(input("Enter the diameter of the wheel in inches (ex 15): "))
    
    # Calculate tire volume
    volume = calculate_tire_volume(width, aspect_ratio, diameter)
    
    # Display the volume for the user to see
    print(f"The approximate volume of air inside your tire is {volume:.2f} liters")
    
    # Get tire price
    tire_price = get_tire_price(width, aspect_ratio, diameter)
    print(f"The price of the tire with these specifications is: {tire_price}")
    
    # Ask the user if they want to buy tires
    buy_tires = input("Would you like to buy tires with these specifications? (yes/no): ").lower()
    if buy_tires == "yes":
        # Get user's phone number
        phone_number = input("Please enter your phone number: ")
        
        # Get current date
        current_date = datetime.now().strftime("%Y-%m-%d")
        
        # Open the file for appending
        with open("volumes.txt", "a") as file:
            # Append the tire information, current date, and phone number to the file
            file.write(f"Date: {current_date}, Width: {width} mm, Aspect Ratio: {aspect_ratio}, Diameter: {diameter} inches, Volume: {volume:.2f} liters, Phone Number: {phone_number}\n")
        
        print("Thank you! Your phone number has been stored for further assistance.")
    elif buy_tires == "no":
        print("No problem! Feel free to reach out to us anytime if you change your mind.")
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    main()

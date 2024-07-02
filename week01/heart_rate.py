"""
This program calculates the target heart rate range for exercise

"""

# Get the user's age
age = int(input("Enter your age: "))

# Calculate the maximum heart rate
max_heart_rate = 220 - age

# Calculate the lower and upper limits of the target heart rate range
lower_limit = 0.65 * max_heart_rate
upper_limit = 0.85 * max_heart_rate

# Display the results
print("Your maximum heart rate is", max_heart_rate, "beats per minute.")
print("To strengthen your heart, maintain a heart rate between", 
      int(lower_limit), "and", int(upper_limit), "beats per minute during exercise.")

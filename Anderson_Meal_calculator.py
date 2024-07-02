# Meal Price Calculator with Extra Feature:
# This program not only calculates the meal subtotal, sales tax, total, and change, 
# but also allows the user to include optional additional charges, such as drinks or desserts. 
# Enter the prices of additional items when prompted, and watch your meal become even more customized!
# It is created by Anderson Okai

# Ask the user for the price of a child's meal and an adult's meal
child_meal_price = float(input("What is the price of a child's meal? "))
adult_meal_price = float(input("What is the price of an adult's meal? "))

# Ask the user for the number of children and adults
num_children = int(input("How many children are there? "))
num_adults = int(input("How many adults are there? "))

# Compute and display the subtotal
subtotal = (num_children * child_meal_price) + (num_adults * adult_meal_price)
print(f"\nSubtotal: ${subtotal:.2f}")

# Ask the user for the sales tax rate (only accept 6 or 6.5)
while True:
    sales_tax_rate = input("What is the sales tax rate? ")
    if sales_tax_rate.replace(".", "").isdigit():  # Check if the input is a digit (integer or float)
        sales_tax_rate = float(sales_tax_rate)
        if sales_tax_rate == int(sales_tax_rate) or sales_tax_rate == round(sales_tax_rate, 1):
            break  # Exit the loop if the input is either an integer or a float with one decimal place
    print("Please enter a valid sales tax rate (e.g., 6 or 6.5)")


# Compute and display the sales tax
sales_tax = (subtotal * sales_tax_rate) / 100
print(f"Sales Tax: ${sales_tax:.2f}")

# Compute and display the total
total = subtotal + sales_tax
print(f"Total: ${total:.2f}")

# Ask the user for the payment amount
payment_amount = float(input("What is the payment amount? "))

# Compute and display the change
change = payment_amount - total
print(f"Change: ${change:.2f}")
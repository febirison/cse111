from datetime import datetime

def calculate_discount(subtotal):
    # Check if today is Tuesday or Wednesday
    day_of_week = datetime.now().weekday()
    if day_of_week == 1 or day_of_week == 2:  # Tuesday is 1, Wednesday is 2
        # Check if subtotal is $50 or greater
        if subtotal >= 50:
            discount = subtotal * 0.1
            subtotal -= discount
            print(f"Discount amount: ${discount:.2f}")
    
    # Calculate sales tax and total amount due
    sales_tax = subtotal * 0.06
    total_due = subtotal + sales_tax
    
    # Print sales tax and total amount due
    print(f"Sales tax amount: ${sales_tax:.2f}")
    print(f"Total: ${total_due:.2f}")

def main():
    # Get subtotal from the user
    subtotal = float(input("Please enter the subtotal: "))
    
    # Calculate discount, sales tax, and total amount due
    calculate_discount(subtotal)

if __name__ == "__main__":
    main()

import math

# Get the number of items from the user
num_items = int(input("Enter the number of items: "))

# Get the number of items per box from the user
items_per_box = int(input("Enter the number of items per box: "))

# Calculate the number of boxes needed (rounded up)
num_boxes = math.ceil(num_items / items_per_box)

# Display the results
print(f"For {num_items} items, packing {items_per_box} items in each box, you will need {num_boxes} boxes.")

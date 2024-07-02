'''
L01 Prove: Milestone (Tire Volume) by Anderson Okai
'''

import math

def main():
  """Gets tire dimensions from user, calculates, and displays volume."""

  # Get user input for tire dimensions
  width_mm = float(input("Enter the width of the tire in mm (ex 205): "))
  aspect_ratio = float(input("Enter the aspect ratio of the tire (ex 60): "))
  diameter_inches = float(input("Enter the diameter of the wheel in inches (ex 15): "))

  # Calculate volume using the formula
  volume_liters = math.pi * width_mm**2 * aspect_ratio * (width_mm * aspect_ratio + 2540 * diameter_inches) / 10**10

  # Display the approximate volume
  print("The approximate volume is", f"{volume_liters:.2f} liters")  # Format output to 2 decimal places

if __name__ == "__main__":
  main()

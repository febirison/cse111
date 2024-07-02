import random

def main():
  """Main function that creates, modifies, and prints a list of numbers and words."""

  # Create a list of numbers
  numbers = [16.2, 75.1, 52.3]

  # Print the initial list of numbers
  print("numbers:", numbers)

  # Append one random number
  append_random_numbers(numbers)
  print("numbers:", numbers)

  # Append three random numbers
  append_random_numbers(numbers, 3)
  print("numbers:", numbers)

  # Create a list of words for the stretch challenge
  words = []

  # Append random words (stretch challenge)
  append_random_words(words, 4)
  print("words:", words)

def append_random_numbers(numbers_list, quantity=1):
  """Appends a specified quantity of random numbers to the list."""

  for _ in range(quantity):
    # Generate a random floating-point number between 0 and 100
    random_number = round(random.uniform(0, 100), 1)
    numbers_list.append(random_number)

def append_random_words(words_list, quantity=1):
  """Appends a specified quantity of random words to the list (stretch challenge)."""

  # Sample words for demonstration (replace with your own list if desired)
  words = ["join", "love", "smile", "dream", "cloud", "head"]

  # Randomly select words and append them to the list
  for _ in range(quantity):
    random_word = random.choice(words)
    words_list.append(random_word)

if __name__ == "__main__":
  main()

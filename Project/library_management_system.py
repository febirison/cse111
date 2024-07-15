import csv
import datetime

# Function to load books from a CSV file
def load_books(filename):
    books = []
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            books.append(row)
    return books

# Function to save books to a CSV file
def save_books(filename, books):
    with open(filename, mode='w', newline='') as file:
        fieldnames = ['id', 'title', 'author', 'genre', 'checked_out', 'due_date', 'patron']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(books)

# Function to add a new book to the inventory
def add_book(books, new_book):
    books.append(new_book)

# Function to update the details of an existing book
def update_book(books, book_id, updated_info):
    for book in books:
        if book['id'] == book_id:
            book.update(updated_info)
            return True
    return False

# Function to check out a book to a patron
def checkout_book(books, book_id, patron):
    for book in books:
        if book['id'] == book_id and book['checked_out'] == 'False':
            book['checked_out'] = 'True'
            book['due_date'] = (datetime.datetime.now() + datetime.timedelta(days=14)).strftime('%Y-%m-%d')
            book['patron'] = patron
            return True
    return False

# Function to return a checked-out book
def return_book(books, book_id):
    for book in books:
        if book['id'] == book_id and book['checked_out'] == 'True':
            book['checked_out'] = 'False'
            book['due_date'] = ''
            book['patron'] = ''
            return True
    return False

# Function to search for books based on various criteria
def search_books(books, search_criteria):
    results = []
    for book in books:
        if any(search_criteria[key].lower() in book[key].lower() for key in search_criteria):
            results.append(book)
    return results

# Function to validate book information
def validate_book_info(book_info):
    required_fields = ['id', 'title', 'author', 'genre']
    for field in required_fields:
        if field not in book_info or not book_info[field].strip():
            return False
    return True

# Function to calculate the due date for a borrowed book
def calculate_due_date(current_date):
    return (current_date + datetime.timedelta(days=14)).strftime('%Y-%m-%d')

# Main function to interact with the Library Book Management System
def main():
    filename = 'library_books.csv'
    books = load_books(filename)

    while True:
        print("\nLibrary Book Management System")
        print("1. Add Book")
        print("2. Update Book")
        print("3. Checkout Book")
        print("4. Return Book")
        print("5. Search Books")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            new_book = {
                'id': input("Enter book ID: "),
                'title': input("Enter book title: "),
                'author': input("Enter book author: "),
                'genre': input("Enter book genre: "),
                'checked_out': 'False',
                'due_date': '',
                'patron': ''
            }
            if validate_book_info(new_book):
                add_book(books, new_book)
                save_books(filename, books)
                print("Book added successfully.")
            else:
                print("Invalid book information. Please try again.")

        elif choice == '2':
            book_id = input("Enter book ID to update: ")
            updated_info = {
                'title': input("Enter new title: "),
                'author': input("Enter new author: "),
                'genre': input("Enter new genre: ")
            }
            if update_book(books, book_id, updated_info):
                save_books(filename, books)
                print("Book updated successfully.")
            else:
                print("Book ID not found.")

        elif choice == '3':
            book_id = input("Enter book ID to checkout: ")
            patron = input("Enter patron name: ")
            if checkout_book(books, book_id, patron):
                save_books(filename, books)
                print("Book checked out successfully.")
            else:
                print("Book ID not found or already checked out.")

        elif choice == '4':
            book_id = input("Enter book ID to return: ")
            if return_book(books, book_id):
                save_books(filename, books)
                print("Book returned successfully.")
            else:
                print("Book ID not found or not checked out.")

        elif choice == '5':
            search_criteria = {
                'title': input("Enter title to search: "),
                'author': input("Enter author to search: "),
                'genre': input("Enter genre to search: ")
            }
            results = search_books(books, search_criteria)
            if results:
                for result in results:
                    print(result)
            else:
                print("No books found matching the criteria.")

        elif choice == '6':
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

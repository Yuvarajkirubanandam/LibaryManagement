import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="YuviK@2329",
  database = "libary"

)
cursor = db.cursor()

def add_book():
    title = input("Enter book title: ")
    author = input("Enter author: ")
    publication_year = int(input("Enter publication year: "))

    query = "INSERT INTO books (title, author, publication_year) VALUES (%s, %s, %s)"
    values = (title, author, publication_year)

    cursor.execute(query, values)
    db.commit()
    print("Book added successfully!")

def add_member():
    name = input("Enter member name: ")
    contact_number = input("Enter contact number: ")

    query = "INSERT INTO members (name, contact_number) VALUES (%s, %s)"
    values = (name, contact_number)

    cursor.execute(query, values)
    db.commit()
    print("Member added successfully!")

def borrow_book():
    member_id = int(input("Enter member ID: "))
    book_id = int(input("Enter book ID: "))
    due_date = input("Enter due date (YYYY-MM-DD): ")

    query = "INSERT INTO loans (member_id, book_id, due_date) VALUES (%s, %s, %s)"
    values = (member_id, book_id, due_date)

    cursor.execute(query, values)
    db.commit()
    print("Book borrowed successfully!")

def list_books():
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()

    for book in books:
        print(book)

def list_members():
    cursor.execute("SELECT * FROM members")
    members = cursor.fetchall()

    for member in members:
        print(member)

def main():
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Add Member")
        print("3. Borrow Book")
        print("4. List Books")
        print("5. List Members")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            add_member()
        elif choice == "3":
            borrow_book()
        elif choice == "4":
            list_books()
        elif choice == "5":
            list_members()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
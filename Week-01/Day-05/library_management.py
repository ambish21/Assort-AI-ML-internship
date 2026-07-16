library = []


def add_book():
    book = input("Enter book name: ")
    library.append(book)
    print("Book added successfully!\n")


def view_books():
    if len(library) == 0:
        print("No books available.\n")
    else:
        print("\nAvailable Books:")
        for i, book in enumerate(library, start=1):
            print(f"{i}. {book}")
        print()


def search_book():
    book = input("Enter book name to search: ")

    if book in library:
        print("Book found!\n")
    else:
        print("Book not found.\n")


def remove_book():
    book = input("Enter book name to remove: ")

    if book in library:
        library.remove(book)
        print("Book removed successfully!\n")
    else:
        print("Book not found.\n")


def menu():
    while True:
        print("===== Library Management System =====")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Remove Book")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book()

        elif choice == "2":
            view_books()

        elif choice == "3":
            search_book()

        elif choice == "4":
            remove_book()

        elif choice == "5":
            print("Thank you for using the Library Management System!")
            break

        else:
            print("Invalid choice. Please try again.\n")


menu()
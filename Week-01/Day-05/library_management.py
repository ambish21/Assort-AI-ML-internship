# -----------------------------------------
# Day 05 Assignment
# Library Management System
# -----------------------------------------


# Add Book Function
def add_book(library):

    title = input("Enter book title: ").strip()
    author = input("Enter author name: ").strip()


    # Input Validation
    if title == "" or author == "":
        print("Book title and author cannot be empty!\n")
        return


    # Duplicate Check
    for book in library:

        if book["title"].lower() == title.lower():
            print("Book already exists!\n")
            return


    # Dictionary for book details
    new_book = {
        "title": title,
        "author": author
    }


    library.append(new_book)

    print("Book added successfully!\n")



# View Books Function
def view_books(library):

    if len(library) == 0:
        print("No books available.\n")
        return


    print("\n===== Available Books =====")


    for index, book in enumerate(library, start=1):

        print(
            f"{index}. {book['title']} "
            f"by {book['author']}"
        )


    print()



# Search Book Function
def search_book(library):

    search = input("Enter book name to search: ").strip()


    if search == "":
        print("Search cannot be empty!\n")
        return


    found = False


    for book in library:

        if book["title"].lower() == search.lower():

            print("\nBook Found!")
            print("Title :", book["title"])
            print("Author:", book["author"])
            
            found = True
            break



    if found == False:
        print("Book not found.\n")



# Remove Book Function
def remove_book(library):

    title = input("Enter book name to remove: ").strip()


    for book in library:

        if book["title"].lower() == title.lower():

            library.remove(book)

            print("Book removed successfully!\n")
            return



    print("Book not found.\n")



# Recursive Function
def count_books(library, index=0):

    # Base Condition
    if index == len(library):
        return 0


    # Recursive Call
    return 1 + count_books(library, index + 1)




# Main Menu Function
def menu():

    # Local variable
    library = []


    while True:


        print("========== Library Management System ==========")

        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Remove Book")
        print("5. Count Books")
        print("6. Exit")


        choice = input("Enter your choice: ")



        # Match Case
        match choice:


            case "1":
                add_book(library)


            case "2":
                view_books(library)


            case "3":
                search_book(library)


            case "4":
                remove_book(library)


            case "5":

                total = count_books(library)

                print(
                    f"\nTotal Books: {total}\n"
                )


            case "6":

                print(
                    "Thank you for using Library System!"
                )

                break


            case _:

                print(
                    "Invalid choice! Try again.\n"
                )



# Program Start
menu()

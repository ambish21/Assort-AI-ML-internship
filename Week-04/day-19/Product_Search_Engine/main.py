from queries import (
    search_products,
    filter_by_category,
    exclude_categories,
    products_with_discount,
    filter_by_price,
    sort_products,
    get_products
)


def display_products(products):

    products = list(products)

    if not products:
        print("\nNo products found.")
        return

    print("\n" + "=" * 80)

    for product in products:
        print(
            f"Name: {product.get('name', 'N/A')} | "
            f"Category: {product.get('category', 'N/A')} | "
            f"Brand: {product.get('brand', 'N/A')} | "
            f"Price: Rs.{product.get('price', 'N/A')} | "
            f"Rating: {product.get('rating', 'N/A')}"
        )

    print("=" * 80)


def menu():

    while True:

        print("\n========== PRODUCT SEARCH ENGINE ==========")
        print("1. Search Products")
        print("2. Filter by Category")
        print("3. Filter by Price")
        print("4. Sort by Price")
        print("5. Pagination")
        print("6. Show Discounted Products")
        print("7. Exclude Categories")
        print("8. Exit")

        choice = input("\nEnter your choice: ")

        match choice:

            case "1":
                keyword = input("Enter product name: ")

                products = search_products(keyword)

                display_products(products)

            case "2":
                categories = input(
                    "Enter categories separated by comma: "
                ).split(",")

                categories = [
                    category.strip()
                    for category in categories
                ]

                products = filter_by_category(categories)

                display_products(products)

            case "3":
                min_price = int(
                    input("Enter minimum price: ")
                )

                max_price = int(
                    input("Enter maximum price: ")
                )

                products = filter_by_price(
                    min_price,
                    max_price
                )

                display_products(products)

            case "4":
                print("\n1. Low to High")
                print("2. High to Low")

                sort_choice = input(
                    "Choose sorting: "
                )

                match sort_choice:

                    case "1":
                        products = sort_products(
                            "price",
                            1
                        )

                        display_products(products)

                    case "2":
                        products = sort_products(
                            "price",
                            -1
                        )

                        display_products(products)

                    case _:
                        print("Invalid sorting choice.")

            case "5":
                page = int(
                    input("Enter page number: ")
                )

                limit = int(
                    input("Products per page: ")
                )

                products = get_products(
                    page,
                    limit
                )

                display_products(products)

            case "6":
                products = products_with_discount()

                display_products(products)

            case "7":
                categories = input(
                    "Enter categories to exclude: "
                ).split(",")

                categories = [
                    category.strip()
                    for category in categories
                ]

                products = exclude_categories(
                    categories
                )

                display_products(products)

            case "8":
                print(
                    "\nThank you for using "
                    "Product Search Engine!"
                )

                break

            case _:
                print("\nInvalid choice. Try again.")


if __name__ == "__main__":
    menu()
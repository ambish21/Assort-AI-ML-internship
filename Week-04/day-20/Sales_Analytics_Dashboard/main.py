from analytics import (
    total_sales,
    monthly_sales,
    top_products,
    revenue_report
)


while True:

    print("\n===== SALES ANALYTICS DASHBOARD =====")
    print("1. Total Sales")
    print("2. Monthly Sales")
    print("3. Top Products")
    print("4. Revenue Report")
    print("5. Exit")

    choice = input("\nEnter your choice: ")


    match choice:

        case "1":
            result = total_sales()

            print("\n--- TOTAL SALES ---")

            for item in result:
                print(item)


        case "2":
            result = monthly_sales()

            print("\n--- MONTHLY SALES ---")

            for item in result:
                print(item)


        case "3":
            result = top_products()

            print("\n--- TOP PRODUCTS ---")

            for item in result:
                print(item)


        case "4":
            result = revenue_report()

            print("\n--- REVENUE REPORT ---")

            for item in result:
                print(item)


        case "5":
            print("\nExiting Dashboard...")
            break


        case _:
            print("\nInvalid choice! Please enter 1 to 5.")
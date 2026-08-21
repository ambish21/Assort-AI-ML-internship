from database import sales_collection, products_collection

# Clear old data
sales_collection.delete_many({})
products_collection.delete_many({})


# ---------------- PRODUCTS ----------------

products = [
    {
        "product_id": 1,
        "name": "Laptop",
        "category": "Electronics",
        "price": 80000
    },
    {
        "product_id": 2,
        "name": "Mouse",
        "category": "Electronics",
        "price": 2000
    },
    {
        "product_id": 3,
        "name": "Keyboard",
        "category": "Electronics",
        "price": 5000
    },
    {
        "product_id": 4,
        "name": "Chair",
        "category": "Furniture",
        "price": 15000
    },
    {
        "product_id": 5,
        "name": "Table",
        "category": "Furniture",
        "price": 25000
    }
]

products_collection.insert_many(products)


# ---------------- SALES ----------------

sales = [
    {
        "product_id": 1,
        "quantity": 2,
        "date": "2026-01-10"
    },
    {
        "product_id": 2,
        "quantity": 5,
        "date": "2026-01-15"
    },
    {
        "product_id": 3,
        "quantity": 3,
        "date": "2026-02-05"
    },
    {
        "product_id": 1,
        "quantity": 1,
        "date": "2026-02-20"
    },
    {
        "product_id": 4,
        "quantity": 4,
        "date": "2026-03-10"
    },
    {
        "product_id": 5,
        "quantity": 2,
        "date": "2026-03-18"
    },
    {
        "product_id": 2,
        "quantity": 10,
        "date": "2026-04-02"
    },
    {
        "product_id": 3,
        "quantity": 6,
        "date": "2026-04-15"
    },
    {
        "product_id": 1,
        "quantity": 3,
        "date": "2026-05-10"
    },
    {
        "product_id": 4,
        "quantity": 2,
        "date": "2026-05-20"
    }
]

sales_collection.insert_many(sales)

print("Products inserted successfully!")
print("Sales inserted successfully!")
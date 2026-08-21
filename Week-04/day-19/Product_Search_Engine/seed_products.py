from database import products_collection


products = [
    {
        "name": "iPhone 15",
        "category": "Mobile",
        "brand": "Apple",
        "price": 250000,
        "stock": 15,
        "discount": 10,
        "rating": 4.8
    },
    {
        "name": "Samsung Galaxy S24",
        "category": "Mobile",
        "brand": "Samsung",
        "price": 220000,
        "stock": 20,
        "discount": 15,
        "rating": 4.7
    },
    {
        "name": "Google Pixel 8",
        "category": "Mobile",
        "brand": "Google",
        "price": 180000,
        "stock": 12,
        "discount": 10,
        "rating": 4.6
    },
    {
        "name": "OnePlus 12",
        "category": "Mobile",
        "brand": "OnePlus",
        "price": 150000,
        "stock": 18,
        "rating": 4.5
    },
    {
        "name": "MacBook Air M3",
        "category": "Laptop",
        "brand": "Apple",
        "price": 350000,
        "stock": 8,
        "discount": 5,
        "rating": 4.9
    },
    {
        "name": "Dell XPS 15",
        "category": "Laptop",
        "brand": "Dell",
        "price": 320000,
        "stock": 10,
        "discount": 8,
        "rating": 4.7
    },
    {
        "name": "HP Pavilion 15",
        "category": "Laptop",
        "brand": "HP",
        "price": 150000,
        "stock": 14,
        "rating": 4.3
    },
    {
        "name": "Lenovo ThinkPad E14",
        "category": "Laptop",
        "brand": "Lenovo",
        "price": 170000,
        "stock": 11,
        "discount": 10,
        "rating": 4.5
    },
    {
        "name": "Sony WH-1000XM5",
        "category": "Headphones",
        "brand": "Sony",
        "price": 85000,
        "stock": 25,
        "discount": 12,
        "rating": 4.8
    },
    {
        "name": "AirPods Pro 2",
        "category": "Headphones",
        "brand": "Apple",
        "price": 65000,
        "stock": 30,
        "discount": 5,
        "rating": 4.7
    },
    {
        "name": "JBL Tune 760NC",
        "category": "Headphones",
        "brand": "JBL",
        "price": 25000,
        "stock": 40,
        "rating": 4.4
    },
    {
        "name": "Logitech MX Master 3S",
        "category": "Accessories",
        "brand": "Logitech",
        "price": 30000,
        "stock": 35,
        "discount": 10,
        "rating": 4.6
    },
    {
        "name": "Mechanical RGB Keyboard",
        "category": "Accessories",
        "brand": "Redragon",
        "price": 12000,
        "stock": 50,
        "rating": 4.2
    },
    {
        "name": "Samsung 27 Inch Monitor",
        "category": "Monitor",
        "brand": "Samsung",
        "price": 55000,
        "stock": 16,
        "discount": 7,
        "rating": 4.5
    },
    {
        "name": "LG UltraGear 24GN",
        "category": "Monitor",
        "brand": "LG",
        "price": 65000,
        "stock": 13,
        "discount": 10,
        "rating": 4.6
    },
    {
        "name": "Canon EOS R10",
        "category": "Camera",
        "brand": "Canon",
        "price": 280000,
        "stock": 6,
        "rating": 4.8
    },
    {
        "name": "Sony Alpha A6400",
        "category": "Camera",
        "brand": "Sony",
        "price": 230000,
        "stock": 7,
        "discount": 5,
        "rating": 4.7
    },
    {
        "name": "Kindle Paperwhite",
        "category": "Tablet",
        "brand": "Amazon",
        "price": 45000,
        "stock": 22,
        "rating": 4.5
    },
    {
        "name": "iPad Air M2",
        "category": "Tablet",
        "brand": "Apple",
        "price": 190000,
        "stock": 9,
        "discount": 8,
        "rating": 4.8
    },
    {
        "name": "Samsung Galaxy Tab S9",
        "category": "Tablet",
        "brand": "Samsung",
        "price": 145000,
        "stock": 12,
        "discount": 10,
        "rating": 4.6
    }
]


# Remove old data from ONLY Day 19 collection
products_collection.delete_many({})


# Insert our product data
result = products_collection.insert_many(products)


print(f"{len(result.inserted_ids)} products inserted successfully!")
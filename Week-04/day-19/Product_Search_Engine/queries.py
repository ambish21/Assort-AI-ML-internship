from database import products_collection


def search_products(keyword):
    query = {
        "name": {
            "$regex": keyword,
            "$options": "i"
        }
    }

    return products_collection.find(
        query,
        {
            "_id": 0,
            "name": 1,
            "category": 1,
            "brand": 1,
            "price": 1,
            "rating": 1
        }
    )

def filter_by_category(categories):
    categories = [
        category.strip().lower()
        for category in categories
    ]

    query = {
        "$expr": {
            "$in": [
                {"$toLower": "$category"},
                categories
            ]
        }
    }

    return products_collection.find(query, {"_id": 0})

def exclude_categories(categories):
    query = {
        "category": {
            "$nin": categories
        }
    }

    return products_collection.find(query, {"_id": 0})


def products_with_discount():
    query = {
        "discount": {
            "$exists": True
        }
    }

    return products_collection.find(query, {"_id": 0})


def filter_by_price(min_price, max_price):
    query = {
        "price": {
            "$gte": min_price,
            "$lte": max_price
        }
    }

    return products_collection.find(query, {"_id": 0})


def sort_products(field, order):
    return products_collection.find(
        {},
        {
            "_id": 0,
            "name": 1,
            "category": 1,
            "brand": 1,
            "price": 1,
            "rating": 1
        }
    ).sort(field, order)


def get_products(page, limit):
    skip = (page - 1) * limit

    return products_collection.find(
        {},
        {
            "_id": 0,
            "name": 1,
            "category": 1,
            "brand": 1,
            "price": 1
        }
    ).skip(skip).limit(limit)
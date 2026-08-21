from database import sales_collection


# 1. TOTAL SALES / TOTAL REVENUE

def total_sales():

    pipeline = [
        {
            "$lookup": {
                "from": "products",
                "localField": "product_id",
                "foreignField": "product_id",
                "as": "product"
            }
        },

        {
            "$unwind": "$product"
        },

        {
            "$group": {
                "_id": None,
                "total_revenue": {
                    "$sum": {
                        "$multiply": [
                            "$quantity",
                            "$product.price"
                        ]
                    }
                },
                "total_items_sold": {
                    "$sum": "$quantity"
                }
            }
        },

        {
            "$project": {
                "_id": 0,
                "total_revenue": 1,
                "total_items_sold": 1
            }
        }
    ]

    return list(sales_collection.aggregate(pipeline))


# 2. MONTHLY SALES

def monthly_sales():

    pipeline = [
        {
            "$lookup": {
                "from": "products",
                "localField": "product_id",
                "foreignField": "product_id",
                "as": "product"
            }
        },

        {
            "$unwind": "$product"
        },

        {
            "$group": {
                "_id": {
                    "$substr": [
                        "$date",
                        0,
                        7
                    ]
                },
                "revenue": {
                    "$sum": {
                        "$multiply": [
                            "$quantity",
                            "$product.price"
                        ]
                    }
                },
                "items_sold": {
                    "$sum": "$quantity"
                }
            }
        },

        {
            "$project": {
                "_id": 0,
                "month": "$_id",
                "revenue": 1,
                "items_sold": 1
            }
        },

        {
            "$sort": {
                "month": 1
            }
        }
    ]

    return list(sales_collection.aggregate(pipeline))


# 3. TOP PRODUCTS

def top_products():

    pipeline = [
        {
            "$lookup": {
                "from": "products",
                "localField": "product_id",
                "foreignField": "product_id",
                "as": "product"
            }
        },

        {
            "$unwind": "$product"
        },

        {
            "$group": {
                "_id": "$product.name",
                "total_quantity": {
                    "$sum": "$quantity"
                },
                "revenue": {
                    "$sum": {
                        "$multiply": [
                            "$quantity",
                            "$product.price"
                        ]
                    }
                }
            }
        },

        {
            "$project": {
                "_id": 0,
                "product": "$_id",
                "total_quantity": 1,
                "revenue": 1
            }
        },

        {
            "$sort": {
                "total_quantity": -1
            }
        }
    ]

    return list(sales_collection.aggregate(pipeline))


# 4. REVENUE REPORT BY CATEGORY

def revenue_report():

    pipeline = [

        # MATCH
        {
            "$match": {
                "quantity": {
                    "$gt": 0
                }
            }
        },

        # LOOKUP
        {
            "$lookup": {
                "from": "products",
                "localField": "product_id",
                "foreignField": "product_id",
                "as": "product"
            }
        },

        # UNWIND
        {
            "$unwind": "$product"
        },

        # GROUP
        {
            "$group": {
                "_id": "$product.category",
                "total_revenue": {
                    "$sum": {
                        "$multiply": [
                            "$quantity",
                            "$product.price"
                        ]
                    }
                }
            }
        },

        # PROJECT
        {
            "$project": {
                "_id": 0,
                "category": "$_id",
                "total_revenue": 1
            }
        },

        # SORT
        {
            "$sort": {
                "total_revenue": -1
            }
        }
    ]

    return list(sales_collection.aggregate(pipeline))
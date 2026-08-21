# Day 19 - Advanced MongoDB Queries

## Topics Covered

### $in
Matches any value from a given list.

Example:
{"category": {"$in": ["Mobile", "Laptop"]}}

### $nin
Excludes values from a given list.

Example:
{"category": {"$nin": ["Mobile", "Laptop"]}}

### $exists
Checks whether a field exists.

Example:
{"discount": {"$exists": True}}

### $regex
Searches text using a pattern.

Example:
{"name": {"$regex": "phone", "$options": "i"}}

### Projection
Controls which fields are returned.

Example:
{"name": 1, "price": 1, "_id": 0}

### Sorting
Sorts documents.

1 = Ascending
-1 = Descending

### Pagination
Used to display data page by page.

skip = (page - 1) * limit
from fastapi import FastAPI

app = FastAPI()

books = []


@app.get("/")
def home():
    return {"message": "Welcome to Book Management API"}


@app.post("/books")
def add_book(book: dict):
    books.append(book)
    return {
        "message": "Book added successfully",
        "book": book
    }
    
@app.get("/books/search")
def search_book(title: str):
    results = []

    for book in books:
        if title.lower() in book["title"].lower():
            results.append(book)

    return {
        "results": results
    }
    
@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return {
                "message": "Book deleted successfully",
                "book": book
            }

    return {"message": "Book not found"}    
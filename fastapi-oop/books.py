from fastapi import FastAPI, Body, Path, Query, HTTPException
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()


class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int
    published_date: int


    def __init__(self, id, title, author, description, rating, published_date):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_date = published_date


# Request model for use in post request
class BookRequest(BaseModel):
    # None required for pydantiv v2
    id: Optional[int] = Field(description='ID is not needed on create', default=None)
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description:str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=0, lt=6)
    published_date: int = Field(gt=1999, lt=2031)

    # Model config to set up more descriptive request within swagger docs
    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "A new book",
                "author": "thefreelancer",
                "description": "A new description of a book",
                "rating": 5,
                "published_date": 2024
            }
        }
    }


BOOKS = [
    Book(1, 'Computer Science Pro', 'thefreelancer', 'A very nice book', 5, 2023),
    Book(2, 'Be Fast with FastAPI', 'thefreelancer', 'This is a great book', 5, 2031),
    Book(3, 'Master Endpoints', 'the freelancer', 'This is an awesome book', 5, 2022),
    Book(4, 'HP1', 'Author 1', 'Book Description', 2, 2020),
    Book(5, 'HP2', 'Author 2', 'Book Description', 3, 2024),
    Book(6, 'HP3', 'Author 3', 'Book Description', 1, 2020),
]


@app.get("/books")
async def read_all_books():
    return BOOKS


@app.get("/books/{book_id}")
async def read_book(book_id: int = Path(gt=0)):
    for book in BOOKS:
        if book.id == book_id:
            return book
        raise HTTPException(status_code=404, detail='Item Not Found')


@app.get("/books/")
async def read_book_by_rating(book_rating: int = Query(gt=0, lt=6)):
    books_to_return = []
    for book in BOOKS:
        if book.rating == book_rating:
            books_to_return.append(book)
    return books_to_return


@app.get("/books/publish/")
async def read_books_by_publish_date(published_date: int = Query(gt=1999, lt=2031)):
    books_to_return = []
    for book in BOOKS:
        if book.published_date == published_date:
            books_to_return.append(book)
    return books_to_return


@app.post("/create-book")
# Body does not allow us to do any form of validation
# So we use pydantic in python
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.dict()) #.model_dump() new fastapi
    BOOKS.append(find_book_id(new_book))


def find_book_id(book: Book):
    if book.id > 0:
        book.id = BOOKS[-1].id + 1
    else:
        book.id = 1
    return book


@app.put("/books/update_book")
async def update_book(book: BookRequest):
    book_changed = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i] = book
            book_changed = True
    if not book_changed:
        raise HTTPException(status_code=404, detail='Items Not Found')


@app.delete("/books/{book_id}")
async def delete_book(book_id: int = Path(gt=0)):
    # Validation for path parameters
    book_changed = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            book_changed = True
            break
    if not book_changed:
        raise HTTPException(status_code=404, detail='Item Not Found')

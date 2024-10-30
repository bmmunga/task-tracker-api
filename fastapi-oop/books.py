from fastapi import FastAPI, Body
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()


class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int

    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating


# Request model for use in post request
class BookRequest(BaseModel):
    # None required for pydantiv v2
    id: Optional[int] = None
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description:str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=0, lt=6)


BOOKS = [
    Book(1, 'Computer Science Pro', 'thefreelancer', 'A very nice book', 5),
    Book(2, 'Be Fast with FastAPI', 'thefreelancer', 'This is a great book', 5),
    Book(3, 'Master Endpoints', 'the freelancer', 'This is an awesome book', 5),
    Book(4, 'HP1', 'Author 1', 'Book Description', 2),
    Book(5, 'HP2', 'Author 2', 'Book Description', 3),
    Book(6, 'HP3', 'Author 3', 'Book Description', 1),
]


@app.get("/books")
async def read_all_books():
    return BOOKS

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

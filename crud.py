from fastapi import FastAPI,HTTPException,Path,Query
from pydantic import BaseModel,Field,computed_field
from typing import Annotated,Optional,Literal
import json

books=[
    {
        'id':1,
        'title':'The Great Gatsby',
        'author':'F. Scott Fitzgerald',
        'published_year':1925,
        'genre':'Novel'
    },
    {
        'id':2,
        'title':'To Kill a Mockin',
        'author':'Harper Lee',
        'published_year':1960,
        'genre':'Novel'
    },
    {
        'id':3,
        'title':'1984',
        'author':'George Orwell',
        'published_year':1949,
        'genre':'Dystopian'
    },
    {
        'id':4,
        'title':'Pride and Prejudice',
        'author':'Jane Austen',
        'published_year':1813,
        'genre':'Romance'
    }
]
app=FastAPI()
@app.get("/")
def Home():
    return {'message':'Welcome to FastAPI In Crud Operation'}

@app.get('/books')
def get_books():
    return books

class Book(BaseModel):
    id:int
    title:str
    author:str
    published_year:int
    genre:Annotated[str,Field(...,description="Genre of the book")]


@app.post('/books')
def create_book(book:Book):
    books.append(book.dict())
    return book
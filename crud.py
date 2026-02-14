from fastapi import FastAPI,HTTPException,Path,Query,status
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


@app.post('/creat_books')
def create_book(book:Book):
    new_book=book.model_dump()
    books.append(new_book)
    return new_book

@app.get('/get_book/{book_id}')
def get_book(book_id:int=Path(...,description="Enter the book id")):
    print(book_id)
    for book in books:
        if book['id']==book_id:
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Book not found")

class UpdateBook(BaseModel):
    title:str
    author:str
    published_year:int
    genre:str


@app.put("/update_book/{book_id}")
def Update_book(book_id:int,Book:UpdateBook):
    for book in books:
        if book['id']==book_id:
            book['title']=Book.title
            book['author']=Book.author
            book['published_year']=Book.published_year
            book['genre']=Book.genre
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Book not found")


@app.delete('/delete_book/{book_id}')
def delete_book(book_id:int):
    for book in books:
        if book['id']==book_id:
            books.remove(book)
            return {'message':"Book deleted successfully"}
    raise

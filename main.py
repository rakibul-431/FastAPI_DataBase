from fastapi import FastAPI,HTTPException,Path,Query
from pydantic import BaseModel,Field
from typing import Annotated,Optional,Literal
import json

app=FastAPI()

class Student(BaseModel):
    name:str
    age:int
    roll:int
@app.get("/")
def Home():
    return {'message':'Welcome to FastAPI'}

@app.get('/items')
def get_items():
    name=['Rakibul','Noyon','Tanvir','Tuhin','Sabit',"Sabbir"]
    return {'names':name}

@app.get('/input/{name}')
def get_name(name:str=Path(...,description="Enter your name")):
    return {'message':f'Hello {name}'}

@app.get('/input2/{name}')
def get_name2(name:str,age:Optional[int]=Query(None,description="Enter your age")):
    if name not in ['Rakibul','Noyon','Tanvir','Tuhin','Sabit',"Sabbir"]:
        raise HTTPException(status_code=404,detail="Name not found")
    if age<15:
        raise HTTPException(status_code=400,detail="Age must be greater than 15")
    return {'message':f'Hello {name}, Your age is {age}'}

@app.post('/Creat_student')
def Creat_student(student:Student):
    return{
        'name':student.name,
        'age':student.age,
        'roll':student.roll
    }
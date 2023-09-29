# print("hello")
# print("hello","world",end='\n')
# print("hello")

# hello='Priyanshu'
# world = 'Goel'
# print(hello,end='\n')

# name= input('Name: ')
# age= input('age: ')
# print("My name is ",name," and my age is ",age)

# x=10
# y=3
# print((x//y))


# hello = 'hello'.upper()
# print(hello)

# hello_lower = 'hello'.lower()
# print(hello_lower)

# hello_capitalize = 'hello'.capitalize()
# print(hello_capitalize)

# hello_count= 'hello'.upper().count('LL')
# print(hello_count)

# x="hello"
# y="hello"

# print(x>=y)
# print("hello")
# print(ord('a'))


# result = 6==6
# print(result)

# x= input("Enter Name: ");
# if x=='Joe':
#     print("Hello Joe")
#     print("Welcome")
# else:
#     print("Bye")

from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
app= FastAPI()

class Item(BaseModel):
    name: str
    capacity: str
    brand: Optional[str]=None

inventory={
    1:{
        "name": "Milk",
        "capacity": "2L",
        "brand": "Regular"
    }
}
@app.get("/")
def home():
    return "Welcome to the Home Page"

@app.get("/fast-api")
def fast(record):
    return "First Fast-Api"+ record

@app.get("/get-item/{item_id}")
def getItem(item_id:int):
    for i in inventory:
      if(i==item_id):
          return inventory[item_id]
    return {"Data":"Not Found"}

@app.post("/post_item/{item_id}")
def createItem(item: Item,item_id: int):
    if item_id in inventory:
        return {"Error: This id already exists"}
    
    inventory[item_id]=item
    return {item_id:item}

@app.put("/update_item/{item_id}")
def update_item(item: Item, item_id: int):
    if item_id in inventory:
        inventory[item_id]= item
        return inventory[item_id]

    return {"Error: item_id not found"}    
   


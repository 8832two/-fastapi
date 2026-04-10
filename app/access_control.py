from fastapi import APIRouter,status
from pydantic import BaseModel
# 创建路由器
access_control_router = APIRouter(tags=["access-control"])

# 临时数据库：字典存储权限
books = [
    {
        "id": 1,
        "author":"Allen",
        "publisher":"reilly media",
        "published_date":"2021-1-01",
        "page_count":1234,
        "language":"English"
    },
    {
        "id": 2,
        "author":"Django",
        "publisher":"BB media",
        "published_date":"2021-1-01",
        "page_count":124,
        "language":"English"
    },
    {
        "id": 3,
        "author":"babiq",
        "publisher":"how to cumpute",
        "published_date":"2021-1-01",
        "page_count":134,
        "language":"English"
    },
    {
        "id": 4,
        "author":"me",
        "publisher":"reilly media",
        "published_date":"2024-1-01",
        "page_count":1233,
        "language":"English"
    }
]

class Book(BaseModel):
    id: int
    author:str
    publisher:str
    published_date:str
    page_count:int
    language:str
    
@access_control_router.get('/books',response_model =list[Book])
async def get_all_books():
    return books

@access_control_router.post('/books',status_code=status.HTTP_201_CREATED)
async def create_a_book(book_data:Book) -> dict:
    new_book = book_data.model_dump()
    books.append(new_book)
    return new_book

@access_control_router.get('/book/{book_id}')
async def get_book(book_id:int) -> dict :
    pass

@access_control_router.patch('/book/{book_id}')
async def update_books(book_id:int) -> dict:
    pass

@access_control_router.delete('/book/{book_id}')
async def delete_books(book_id:int) -> dict:
    pass
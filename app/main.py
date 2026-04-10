from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# In-memory storage for books
books = []
book_id_counter = 1

class Book(BaseModel):
    id: int
    title: str
    author: str

class BookCreateModel(BaseModel):
    title: str
    author: str

@app.get("/")
async def read_root():
    return {"message": "hello fastapi"}

# 路径参数
@app.get("/greet/{name}")
async def greet_name(name: str) -> dict:
    return {"message": f"Hello, {name}!"}

# 查询参数
# fastapi总能是将路径处理函数中存在但在url中未定义的参数是为查询参数
@app.get("/bye/")
async def say_bye(name: str) -> dict:
    return {"message": f"Goodbye, {name}!"}

# 路径参数与查询参数混合
@app.get("/hello/{name}")
async def say_hello(name: str, age: int | None = None) -> dict:
    return {"message": f"hello{name}", "age": age}

# CRUD Operations for Books

@app.post("/books", response_model=Book)
async def create_book(book_data: BookCreateModel):
    global book_id_counter
    new_book = Book(id=book_id_counter, title=book_data.title, author=book_data.author)
    books.append(new_book)
    book_id_counter += 1
    return new_book

@app.get("/books", response_model=List[Book])
async def get_books():
    return books

@app.get("/books/{book_id}", response_model=Book)
async def get_book(book_id: int):
    for book in books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@app.put("/books/{book_id}", response_model=Book)
async def update_book(book_id: int, book_data: BookCreateModel):
    for book in books:
        if book.id == book_id:
            book.title = book_data.title
            book.author = book_data.author
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@app.delete("/books/{book_id}")
async def delete_book(book_id: int):
    for i, book in enumerate(books):
        if book.id == book_id:
            del books[i]
            return {"message": "Book deleted"}
    raise HTTPException(status_code=404, detail="Book not found")

# 请求体的使用 (old create_book, now replaced)
# @app.post("/create_book")
# async def create_book(book_data: BookCreateModel):
#     return {"title": book_data.title, "author": book_data.author}

@app.get('/get_headers', status_code=200)
async def get_headers(
    accept: str = Header(None),
    content_type: str = Header(None),
    user_agent: str = Header(None),
    host=Header(None)
):
    request_headers = {}
    request_headers["Accept"] = accept
    request_headers["Content-Type"] = content_type
    request_headers["user-agent"] = user_agent
    request_headers["Host"] = host
    return request_headers

# 导入第二课的权限路由
from app.access_control import access_control_router
app.include_router(access_control_router)
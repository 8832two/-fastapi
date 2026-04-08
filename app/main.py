from fastapi import FastAPI,Header
from pydantic import BaseModel
app = FastAPI()


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


# 请求体的使用


class BookCreateModel(BaseModel):
    title: str
    author: str


@app.post("/create_book")
async def create_book(book_data: BookCreateModel):
    return {"title": book_data.title, "author": book_data.author}


@app.get('/get_headers',status_code = 200)
async def get_headers(
    accept:str = Header(None),  
    content_type: str = Header(None),
    user_agent:str = Header(None),
    host = Header(None)
    ):
    request_headers = {}
    request_headers["Accept"] = accept
    request_headers["Content-Type"] = content_type
    request_headers["user-agent"] = user_agent
    request_headers["Host"] = host
    return request_headers
这是一个简单的fast api学习demo
并且在不断更新知道成为一个复杂的fastapi项目
构建这个项目的主要目的是为了记录我的学习过程

## 项目结构
- `app/main.py` - 主应用和第一课内容
- `app/access_control.py` - 第二课：访问控制API（使用 access_control_router）

## 启动方式
`fastapi dev`

## API 文档
启动后访问 http://127.0.0.1:8000/docs 查看所有API

## CRUD REST API (书籍管理)
项目包含一个完整的CRUD REST API用于书籍管理：

- **POST /books** - 创建新书籍
  - 请求体: `{"title": "string", "author": "string"}`
  - 返回: 创建的书籍对象，包含自动生成的ID

- **GET /books** - 获取所有书籍
  - 返回: 书籍列表

- **GET /books/{book_id}** - 获取特定书籍
  - 路径参数: `book_id` (整数)
  - 返回: 指定ID的书籍对象

- **PUT /books/{book_id}** - 更新书籍
  - 路径参数: `book_id` (整数)
  - 请求体: `{"title": "string", "author": "string"}`
  - 返回: 更新后的书籍对象

- **DELETE /books/{book_id}** - 删除书籍
  - 路径参数: `book_id` (整数)
  - 返回: 删除确认消息

数据存储在内存中，重启应用后数据会丢失。
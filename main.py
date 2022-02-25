from fastapi import FastAPI
from routes.todos_route import todo_api_router
from routes.courses_routes import courses_api_router
app = FastAPI()

app.include_router(todo_api_router)
app.include_router(courses_api_router)


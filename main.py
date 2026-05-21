# 修改 FastAPI 应用的入口文件
from fastapi import FastAPI
from routers import user_router

app = FastAPI()

app.include_router(user_router.router)

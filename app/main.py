from fastapi import FastAPI
from .routers import cardRouter
from .dependencies import database

app = FastAPI()

# 包含路由模块
app.include_router(cardRouter.router)

# 初始化数据库
@app.on_event("startup")
async def startup_event():

    database.init_db()

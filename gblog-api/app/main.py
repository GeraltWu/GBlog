from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # 导入CORS中间件
from .routers.front import router as front_router  # 导入前台统一路由
from .database.database import Base, engine
from .database.redis_db import init_redis_pool, close_redis

app = FastAPI(
    title="GBlog API",
    description="博客系统后端API",
    version="1.0.0"
)

# 配置CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允许所有来源，也可以指定具体域名如 ["http://localhost:3000"]
    allow_credentials=True,  # 允许携带凭证
    allow_methods=["*"],  # 允许所有方法
    allow_headers=["*"],  # 允许所有请求头
)

# 创建数据库表
Base.metadata.create_all(bind=engine)

# 启动时连接 Redis
@app.on_event("startup")
async def startup_event():
    await init_redis_pool()

# 关闭时断开 Redis 连接
@app.on_event("shutdown")
async def shutdown_event():
    await close_redis()

# 注册路由
app.include_router(front_router)  # 使用统一的前台路由


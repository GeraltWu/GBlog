import aioredis
from app.config.settings import settings

# Redis 连接
redis_connection = None

async def init_redis_pool():
    """初始化 Redis 连接池"""
    global redis_connection
    redis_connection = await aioredis.create_redis_pool(
        f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}",
        db=settings.REDIS_DB,
        password=settings.REDIS_PASSWORD,
        encoding="utf-8"
    )
    return redis_connection

async def get_redis():
    """获取 Redis 连接"""
    if redis_connection is None:
        await init_redis_pool()
    return redis_connection

async def close_redis():
    """关闭 Redis 连接"""
    if redis_connection is not None:
        redis_connection.close()
        await redis_connection.wait_closed()
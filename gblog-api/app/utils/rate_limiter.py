from app.database.redis_db import redis_client
import time
from fastapi import HTTPException, Request

def rate_limit(request: Request, limit: int = 10, period: int = 60):
    """
    接口限流装饰器
    
    Args:
        request: FastAPI请求对象
        limit: 时间段内允许的最大请求次数
        period: 时间段（秒）
    """
    # 获取客户端IP
    client_ip = request.client.host
    
    # 构造Redis键
    key = f"rate_limit:{client_ip}"
    
    # 获取当前时间戳
    current = time.time()
    
    # 使用管道执行原子操作
    with redis_client.pipeline() as pipe:
        # 添加当前时间戳到有序集合
        pipe.zadd(key, {current: current})
        
        # 移除时间段外的记录
        pipe.zremrangebyscore(key, 0, current - period)
        
        # 获取时间段内的请求次数
        pipe.zcard(key)
        
        # 设置键过期时间
        pipe.expire(key, period)
        
        # 执行命令
        _, _, count, _ = pipe.execute()
    
    # 如果请求次数超过限制，抛出异常
    if count > limit:
        raise HTTPException(status_code=429, detail="请求过于频繁，请稍后再试")
from pydantic_settings import BaseSettings
from typing import Optional

class AppSettings(BaseSettings):
    # 数据库配置
    MYSQL_USER: str
    MYSQL_PASSWORD: str
    MYSQL_HOST: str
    MYSQL_PORT: int
    MYSQL_DB: str
    
    # 应用配置
    APP_PORT: int
    
    # JWT配置
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    
    # Redis配置
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379
    REDIS_DB: int = 0
    REDIS_PASSWORD: Optional[str] = None
    
    class Config:
        env_file = ".env"

settings = AppSettings()
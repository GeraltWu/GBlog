from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from app.schemas.common import CamelModel, PageResult

# 用户登录请求模型
class UserLogin(CamelModel):
    username: str
    password: str

# 用户登录响应模型，只包含token
class UserLoginResponse(CamelModel):
    token: str
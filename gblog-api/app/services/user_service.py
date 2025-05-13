from typing import List, Optional
from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserLogin, UserLoginResponse
from app.auth.jwt import create_access_token
from datetime import timedelta
import hashlib

def authenticate_user(db: Session, login_data: UserLogin) -> Optional[UserLoginResponse]:
    """
    验证用户并生成token
    
    Args:
        db: 数据库会话
        login_data: 用户登录数据
        
    Returns:
        Optional[UserLoginResponse]: 如果验证成功，返回包含token的响应；否则返回None
    """
    # 查询用户
    user = db.query(User).filter(User.username == login_data.username).first()
    
    # 验证用户是否存在及密码是否正确
    # 注意：这里假设密码是以某种方式加密存储的，实际实现应根据您的密码存储方式调整
    if not user or not verify_password(login_data.password, user.password):
        return None
    
    # 创建访问令牌
    access_token = create_access_token(
        data={"sub": user.username, "role": user.role},
        expires_delta=timedelta(hours=24)  # 令牌有效期24小时
    )
    
    # 返回只包含token的响应
    return UserLoginResponse(token=access_token)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    验证密码
    
    Args:
        plain_password: 明文密码
        hashed_password: 哈希密码
        
    Returns:
        bool: 密码是否匹配
    """
    # 这里应该实现您的密码验证逻辑
    # 示例：使用MD5哈希（不推荐用于生产环境，仅作示例）
    hashed_input = hashlib.md5(plain_password.encode()).hexdigest()
    # print(hashed_input, hashed_password)
    return hashed_input == hashed_password
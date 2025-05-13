from sqlalchemy.orm import Session
from app.models.user import User
from typing import Optional

def get_user_by_username(db: Session, username: str) -> Optional[User]:
    """
    通过用户名获取用户
    
    Args:
        db: 数据库会话
        username: 用户名
        
    Returns:
        Optional[User]: 用户对象，如果不存在则返回None
    """
    return db.query(User).filter(User.username == username).first()
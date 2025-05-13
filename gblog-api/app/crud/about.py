from sqlalchemy.orm import Session
from app.models.about import About
from typing import List

def get_about_items(db: Session) -> List[About]:
    """
    获取关于我页面的所有配置项
    
    Args:
        db: 数据库会话
        
    Returns:
        List[About]: 关于我页面的所有配置项
    """
    return db.query(About).all()
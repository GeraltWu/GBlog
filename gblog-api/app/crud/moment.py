from sqlalchemy.orm import Session
from app.models.moment import Moment
from typing import List, Optional
from sqlalchemy import desc

def get_moments_count(db: Session, is_published: bool = True) -> int:
    """
    获取动态总数
    
    Args:
        db: 数据库会话
        is_published: 是否已发布
        
    Returns:
        int: 动态总数
    """
    return db.query(Moment).filter(Moment.is_published == is_published).count()

def get_moments(
    db: Session, 
    skip: int = 0, 
    limit: int = 100, 
    is_published: bool = True
) -> List[Moment]:
    """
    获取动态列表
    
    Args:
        db: 数据库会话
        skip: 跳过的记录数
        limit: 限制返回的记录数
        is_published: 是否已发布
        
    Returns:
        List[Moment]: 动态列表
    """
    return db.query(Moment)\
        .filter(Moment.is_published == is_published)\
        .order_by(desc(Moment.create_time))\
        .offset(skip)\
        .limit(limit)\
        .all()


def like_moment(db: Session, moment_id: int) -> bool:
    """
    给动态点赞（增加点赞数）
    
    Args:
        db: 数据库会话
        moment_id: 动态ID
        
    Returns:
        bool: 是否点赞成功
    """
    try:
        # 查询动态是否存在
        moment = db.query(Moment).filter(Moment.id == moment_id).first()
        if not moment:
            return False
        
        # 增加点赞数
        if moment.likes is None:
            moment.likes = 1
        else:
            moment.likes += 1
        
        # 提交到数据库
        db.commit()
        return True
    except Exception as e:
        db.rollback()
        print(f"点赞失败: {str(e)}")
        return False
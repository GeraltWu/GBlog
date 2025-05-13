from sqlalchemy.orm import Session
from app.crud import moment as moment_crud
from app.schemas.moment import MomentList
from typing import List, Tuple
import math
from app.utils.bit_utils import bit_to_bool

def get_moment_list(db: Session, page_num: int, page_size: int) -> Tuple[List[MomentList], int]:
    """
    获取动态列表，包含分页逻辑和数据转换
    
    Args:
        db: 数据库会话
        page_num: 页码，从1开始
        page_size: 每页显示的数量
        
    Returns:
        Tuple[List[MomentList], int]: 动态列表和总页数
    """
    # 计算偏移量
    skip = (page_num - 1) * page_size
    
    # 获取总数和计算总页数
    total = moment_crud.get_moments_count(db, is_published=True)
    total_page = math.ceil(total / page_size) if total > 0 else 1
    
    # 获取动态列表
    moments = moment_crud.get_moments(
        db, 
        skip=skip, 
        limit=page_size, 
        is_published=True
    )
    
    # 使用Pydantic模型进行数据转换
    moment_list = []
    for moment in moments:
        moment_obj = MomentList(
            id=moment.id,
            content=moment.content,
            create_time=moment.create_time,
            likes=moment.likes or 0,  # 处理可能为None的情况
            is_published=bit_to_bool(moment.is_published)
        )
        moment_list.append(moment_obj)
    
    return moment_list, total_page


def like_moment(db: Session, moment_id: int) -> bool:
    """
    给动态点赞
    
    Args:
        db: 数据库会话
        moment_id: 动态ID
        
    Returns:
        bool: 是否点赞成功
    """
    # 调用crud层处理数据库操作
    return moment_crud.like_moment(db, moment_id)
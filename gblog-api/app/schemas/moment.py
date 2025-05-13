from typing import List, Optional
from datetime import datetime
from app.schemas.common import CamelModel, PageResult

class MomentBase(CamelModel):
    """动态基础模型"""
    id: int
    content: str
    create_time: datetime
    likes: int
    is_published: bool

class MomentList(MomentBase):
    """动态列表项模型"""
    pass

class MomentListResponse(CamelModel):
    """动态列表响应模型"""
    total_page: int
    list: List[MomentList]
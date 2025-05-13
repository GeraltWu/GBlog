from pydantic import BaseModel
from app.schemas.common import CamelModel
from typing import List, Optional
from datetime import datetime

class PageComment(CamelModel):
    """评论数据模型"""
    id: int
    nickname: str
    content: str
    avatar: str
    create_time: str
    website: Optional[str] = None
    admin_comment: bool
    parent_comment_id: int  # 改为整数类型
    parent_comment_nickname: str
    root_comment_id: int  # 添加根评论ID字段
    reply_comments: List['PageComment'] = []


class CommentQuery(CamelModel):
    """评论查询参数"""
    page: Optional[int] = None  # 页面分类（0普通文章，1关于我...）
    blog_id: Optional[int] = None  # page==0时，需要提供blogId
    page_num: Optional[int] = 1
    page_size: Optional[int] = 10

class CommentResponse(CamelModel):
    """评论响应数据"""
    all_comment: int
    close_comment: int
    comments: dict


class CommentForm(CamelModel):
    """评论表单数据模型"""
    nickname: str
    email: str
    website: str
    content: str
    page: int
    isNotice: bool
    parentCommentId: int
    blogId: Optional[int] = None
    rootCommentId: int  # 新增字段，由前端直接传入
    avatar: Optional[str] = None  # 新增头像字段，可选
    
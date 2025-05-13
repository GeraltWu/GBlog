from pydantic import ConfigDict
from typing import List, Optional
from datetime import datetime
from app.schemas.common import CamelModel, PageResult

class CategoryBase(CamelModel):
    id: int
    category_name: str

class TagBase(CamelModel):
    id: int
    tag_name: str
    color: str

class BlogList(CamelModel):
    id: int
    title: str
    description: str
    create_time: datetime
    views: int
    words: int
    read_time: int
    is_top: bool
    password: Optional[str] = None
    is_private: bool
    category: Optional[CategoryBase] = None
    tags: List[TagBase] = []


class BlogDetail(CamelModel):
    id: int
    title: str
    content: str
    first_picture: str
    description: str
    create_time: datetime
    update_time: datetime
    views: int
    words: int
    read_time: int
    is_top: bool
    is_appreciation_enabled: bool
    is_comment_enabled: bool
    is_private: bool
    is_published: bool
    is_recommend: bool
    password: Optional[str] = None
    category: Optional[CategoryBase] = None
    tags: List[TagBase] = []
    
class BlogArchive(CamelModel):
    year: int
    month: int
    blogs: List[BlogList]

class ArchiveBlog(CamelModel):
    id: int
    title: str
    day: str
    password: Optional[str] = None
    is_private: bool

class ArchiveBlogMonthly(CamelModel):
    month: str
    list: List[ArchiveBlog]

class ArchiveBlogList(CamelModel):
    total_quantity: int
    list: List[ArchiveBlogMonthly]


class BlogPasswordForm(CamelModel):
    """博客密码表单数据模型"""
    blogId: int
    password: str
    
    
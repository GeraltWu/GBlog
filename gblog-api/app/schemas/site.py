from typing import List, Optional, Dict, Any
from pydantic import ConfigDict, Field
from app.schemas.common import CamelModel

class Copyright(CamelModel):
    """版权信息"""
    title: str
    site_name: str

class Badge(CamelModel):
    """徽标信息"""
    title: str
    url: str
    subject: str
    value: str
    color: str

class SiteInfo(CamelModel):
    """站点基本信息"""
    blog_name: str
    web_title_suffix: str
    footer_img_title: str
    footer_img_url: str
    copyright: Copyright
    beian: str
    reward: str
    comment_admin_flag: str
    playlist_server: str
    playlist_id: str
    badges: List[Badge] = []

class Favorite(CamelModel):
    """自定义收藏/喜好"""
    title: str
    content: str

class Introduction(CamelModel):
    """个人介绍信息"""
    avatar: str
    name: str
    github: str
    bilibili: Optional[str] = None
    email: str
    roll_text: List[str]
    favorites: List[Favorite] = []
    telegram: Optional[str] = None
    qq: Optional[str] = None
    netease: Optional[str] = None

class RandomBlog(CamelModel):
    """随机博客信息"""
    id: int
    is_private: bool
    password: Optional[str] = None
    create_time: str
    first_picture: str
    title: str

class NewBlog(CamelModel):
    """最新博客信息"""
    id: str
    is_private: bool
    password: Optional[str] = None
    title: str

class Tag(CamelModel):
    """标签信息"""
    id: int
    name: str
    color: str

class Category(CamelModel):
    """分类信息"""
    id: int
    name: str

class SiteResponse(CamelModel):
    """站点信息响应"""
    introduction: Introduction
    random_blog_list: List[RandomBlog] = []
    tag_list: List[Tag] = []
    new_blog_list: List[NewBlog] = []
    site_info: SiteInfo
    category_list: List[Category] = []
    

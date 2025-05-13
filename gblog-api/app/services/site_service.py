from typing import Dict, Any, List
import json
import random
from sqlalchemy import desc
from sqlalchemy.orm import Session
from app.models.site_setting import SiteSetting
from app.models.blog import Blog
from app.models.tag import Tag
from app.models.category import Category
from app.schemas.site import SiteResponse, SiteInfo, Introduction, RandomBlog, Tag as TagSchema, NewBlog, Category as CategorySchema, Copyright, Badge, Favorite

def get_site_info(db: Session) -> SiteResponse:
    """
    获取站点信息
    
    Args:
        db: 数据库会话
        
    Returns:
        SiteResponse: 包含站点信息的响应对象
    """
    # 查询所有站点设置
    site_settings = db.query(SiteSetting).all()
    
    # 初始化数据字典
    site_info_data = {}
    introduction_data = {"favorites": []}
    badges = []
    random_blog_list = []
    tag_list = []
    new_blog_list = []
    category_list = []
    
    # 处理基础设置 (type=1)
    basic_settings = [s for s in site_settings if s.type == 1]
    for setting in basic_settings:
        if setting.name_en == 'copyright':
            site_info_data["copyright"] = json.loads(setting.value)
        else:
            site_info_data[setting.name_en] = setting.value
    
    # 处理个人资料卡 (type=2)
    intro_settings = [s for s in site_settings if s.type == 2]
    for setting in intro_settings:
        if setting.name_en == 'rollText':
            # 处理滚动文字，转为列表
            text_value = setting.value.strip('"')
            roll_texts = [text.strip() for text in text_value.split('","')]
            introduction_data["roll_text"] = roll_texts
        elif setting.name_en == 'favorite':
            # 处理收藏/喜好
            favorite = json.loads(setting.value)
            introduction_data["favorites"].append(Favorite(**favorite))
        else:
            introduction_data[setting.name_en] = setting.value
    
    # 处理徽标 (type=3)
    badge_settings = [s for s in site_settings if s.type == 3]
    for setting in badge_settings:
        if setting.name_en == 'badge':
            badge_data = json.loads(setting.value)
            badges.append(Badge(**badge_data))
    
    # 获取随机博客列表（最多5篇）
    blogs = db.query(Blog).all()
    if blogs:
        random_blogs = random.sample(blogs, min(5, len(blogs)))
        for blog in random_blogs:
            random_blog_list.append(RandomBlog(
                id=blog.id,
                is_private=blog.is_private,
                password=blog.password,
                create_time=blog.create_time.strftime("%Y-%m-%d %H:%M:%S"),
                first_picture=blog.first_picture,
                title=blog.title
            ))
    
    # 获取标签列表
    tags = db.query(Tag).all()
    for tag in tags:
        tag_list.append(TagSchema(
            id=tag.id,
            name=tag.tag_name,
            color=tag.color
        ))
    
    # 获取最新博客列表
    new_blogs = db.query(Blog).order_by(desc(Blog.create_time)).limit(1).all()
    for blog in new_blogs:
        new_blog_list.append(NewBlog(
            id=str(blog.id),
            is_private=blog.is_private,
            password=blog.password,
            title=blog.title
        ))
    
    # 获取分类列表
    categories = db.query(Category).all()
    for category in categories:
        category_list.append(CategorySchema(
            id=category.id,
            name=category.category_name
        ))
    
    # 构建版权信息对象
    copyright_obj = Copyright(**site_info_data.pop("copyright", {"title": "", "site_name": ""}))
    
    # 构建站点信息对象
    site_info = SiteInfo(
        **site_info_data,
        copyright=copyright_obj,
        badges=badges
    )
    
    # 构建个人介绍对象
    introduction = Introduction(**introduction_data)
    
    # 构建并返回完整的站点响应对象
    return SiteResponse(
        introduction=introduction,
        random_blog_list=random_blog_list,
        tag_list=tag_list,
        new_blog_list=new_blog_list,
        site_info=site_info,
        category_list=category_list
    )
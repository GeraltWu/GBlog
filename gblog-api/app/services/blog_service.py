from sqlalchemy.orm import Session
from app.crud import blog as blog_crud
from app.models.blog import Blog
from app.schemas.blog import BlogList, CategoryBase, TagBase, BlogDetail, ArchiveBlogList, ArchiveBlogMonthly, ArchiveBlog
from typing import List, Tuple, Optional
import math
from app.utils.bit_utils import bit_to_bool
import json
import pickle

# Redis键前缀
BLOG_LIST_KEY = "blog:list:page:{}"
BLOG_DETAIL_KEY = "blog:detail:{}"
BLOG_CATEGORY_KEY = "blog:category:{}:page:{}"
BLOG_TAG_KEY = "blog:tag:{}:page:{}"
BLOG_ARCHIVE_KEY = "blog:archives"
# Redis缓存过期时间（秒）
CACHE_EXPIRE_TIME = 3600  # 1小时

def get_blog_list(db: Session, page_num: int, page_size: int) -> Tuple[List[BlogList], int]:
    """
    获取博客列表，包含分页逻辑和数据转换
    
    Args:
        db: 数据库会话
        page_num: 页码，从1开始
        page_size: 每页显示的数量
        
    Returns:
        Tuple[List[BlogList], int]: 博客列表和总页数
    """

    # 计算偏移量
    skip = (page_num - 1) * page_size
    
    # 获取总数和计算总页数
    total = blog_crud.get_blogs_count(db, is_published=True)
    total_page = math.ceil(total / page_size) if total > 0 else 1
    
    # 获取博客列表
    blogs = blog_crud.get_blogs_with_relations(
        db, 
        skip=skip, 
        limit=page_size, 
        is_published=True,
        order_by=[Blog.is_top.desc(), Blog.create_time.desc()]
    )
    
    # 使用Pydantic模型进行数据转换
    blog_list = []
    for blog in blogs:
        # 处理分类信息
        category_obj = None
        if blog.category:
            category_obj = CategoryBase(
                id=blog.category.id,
                category_name=blog.category.category_name
            )
        
        # 处理标签信息
        tags_list = [
            TagBase(
                id=tag.id,
                tag_name=tag.tag_name,
                color=tag.color
            ) for tag in blog.tags
        ]
        
        # 创建BlogList对象，转换bit为bool
        blog_obj = BlogList(
            id=blog.id,
            title=blog.title,
            description=blog.description,
            create_time=blog.create_time,
            views=blog.views,
            words=blog.words,
            read_time=blog.read_time,
            is_top=bit_to_bool(blog.is_top),
            password=blog.password,
            is_private=bit_to_bool(blog.is_private),
            category=category_obj,
            tags=tags_list
        )
        blog_list.append(blog_obj)
    
    result = (blog_list, total_page)
    
    return result

def get_blog_list_by_category_name(db: Session, category_name: str, page_num: int, page_size: int) -> Tuple[List[BlogList], int]:
    """
    根据分类名称获取博客列表，包含分页逻辑和数据转换
    
    Args:
        db: 数据库会话
        category_name: 分类名称
        page_num: 页码，从1开始
        page_size: 每页显示的数量
        
    Returns:
        Tuple[List[BlogList], int]: 博客列表和总页数
    """
    # 计算偏移量
    skip = (page_num - 1) * page_size
    
    # 获取博客列表和总数
    blogs, total = blog_crud.get_blogs_by_category_name(
        db, 
        category_name=category_name,
        skip=skip, 
        limit=page_size, 
        is_published=True,
        order_by=[Blog.is_top.desc(), Blog.create_time.desc()]
    )
    
    # 计算总页数
    total_page = math.ceil(total / page_size) if total > 0 else 1
    
    # 使用Pydantic模型进行数据转换
    blog_list = []
    for blog in blogs:
        # 处理分类信息
        category_obj = None
        if blog.category:
            category_obj = CategoryBase(
                id=blog.category.id,
                category_name=blog.category.category_name
            )
        
        # 处理标签信息
        tags_list = [
            TagBase(
                id=tag.id,
                tag_name=tag.tag_name,
                color=tag.color
            ) for tag in blog.tags
        ]
        
        # 创建BlogList对象，转换bit为bool
        blog_obj = BlogList(
            id=blog.id,
            title=blog.title,
            description=blog.description,
            create_time=blog.create_time,
            views=blog.views,
            words=blog.words,
            read_time=blog.read_time,
            is_top=bit_to_bool(blog.is_top),
            password=blog.password,
            is_private=bit_to_bool(blog.is_private),
            category=category_obj,
            tags=tags_list
        )
        blog_list.append(blog_obj)
    
    return blog_list, total_page

def get_blog_list_by_tag_name(db: Session, tag_name: str, page_num: int, page_size: int) -> Tuple[List[BlogList], int]:
    """
    根据标签名称获取博客列表，包含分页逻辑和数据转换
    
    Args:
        db: 数据库会话
        tag_name: 标签名称
        page_num: 页码，从1开始
        page_size: 每页显示的数量
        
    Returns:
        Tuple[List[BlogList], int]: 博客列表和总页数
    """
    # 计算偏移量
    skip = (page_num - 1) * page_size
    
    # 获取博客列表和总数
    blogs, total = blog_crud.get_blogs_by_tag_name(
        db, 
        tag_name=tag_name,
        skip=skip, 
        limit=page_size, 
        is_published=True,
        order_by=[Blog.is_top.desc(), Blog.create_time.desc()]
    )
    
    # 计算总页数
    total_page = math.ceil(total / page_size) if total > 0 else 1
    
    # 使用Pydantic模型进行数据转换
    blog_list = []
    for blog in blogs:
        # 处理分类信息
        category_obj = None
        if blog.category:
            category_obj = CategoryBase(
                id=blog.category.id,
                category_name=blog.category.category_name
            )
        
        # 处理标签信息
        tags_list = [
            TagBase(
                id=tag.id,
                tag_name=tag.tag_name,
                color=tag.color
            ) for tag in blog.tags
        ]
        
        # 创建BlogList对象，转换bit为bool
        blog_obj = BlogList(
            id=blog.id,
            title=blog.title,
            description=blog.description,
            create_time=blog.create_time,
            views=blog.views,
            words=blog.words,
            read_time=blog.read_time,
            is_top=bit_to_bool(blog.is_top),
            password=blog.password,
            is_private=bit_to_bool(blog.is_private),
            category=category_obj,
            tags=tags_list
        )
        blog_list.append(blog_obj)
    
    return blog_list, total_page

def get_blog_by_id(db: Session, blog_id: int, password: Optional[str] = None) -> Optional[BlogDetail]:
    """
    根据ID获取博客详情，包含数据转换
    
    Args:
        db: 数据库会话
        blog_id: 博客ID
        
    Returns:
        Optional[BlogDetail]: 博客详情，如果不存在则返回None
    """
    # 获取博客详情
    blog = blog_crud.get_blog_by_id(db, blog_id=blog_id, is_published=True)
    
    if not blog:
        return None
    
    # 处理分类信息
    category_obj = None
    if blog.category:
        category_obj = CategoryBase(
            id=blog.category.id,
            category_name=blog.category.category_name
        )
    
    # 处理标签信息
    tags_list = [
        TagBase(
            id=tag.id,
            tag_name=tag.tag_name,
            color=tag.color
        ) for tag in blog.tags
    ]    
    # 创建BlogDetail对象，转换bit为bool
    blog_detail = BlogDetail(
        id=blog.id,
        title=blog.title,
        content=blog.content,
        first_picture=blog.first_picture,  # 确保包含first_picture字段
        description=blog.description,
        create_time=blog.create_time,
        update_time=blog.update_time,
        views=blog.views,
        words=blog.words,
        read_time=blog.read_time,
        is_top=bit_to_bool(blog.is_top),
        is_recommend=bit_to_bool(blog.is_recommend),
        is_appreciation_enabled=bit_to_bool(blog.is_appreciation_enabled),
        is_comment_enabled=bit_to_bool(blog.is_comment_enabled),
        is_published=bit_to_bool(blog.is_published),
        is_private=bit_to_bool(blog.is_private),
        password=blog.password,
        category=category_obj,
        tags=tags_list
    )
    
    # 更新浏览量（异步处理或直接更新）
    blog.views += 1
    db.commit()
    
    return blog_detail


def get_blog_archives(db: Session) -> ArchiveBlogList:
    """
    获取博客归档数据，按年月分组
    
    Args:
        db: 数据库会话
        
    Returns:
        ArchiveBlogList: 归档数据，包含总数和按月份分组的博客列表
    """
    # 获取归档数据
    archives_data = blog_crud.get_blog_archives(db, is_published=True)
    
    # 计算博客总数
    total_quantity = sum(len(blogs) for _, _, blogs in archives_data)
    
    # 转换为前端需要的格式
    monthly_list = []
    for year, month, blogs in archives_data:
        # 处理博客列表
        blog_list = []
        for blog in blogs:
            # 创建ArchiveBlog对象
            blog_obj = ArchiveBlog(
                id=blog.id,
                title=blog.title,
                day=blog.create_time.strftime("%d"),  # 日期格式化为"日"
                password=blog.password,
                is_private=blog.is_private
            )
            blog_list.append(blog_obj)
        
        # 添加到月份列表
        month_str = f"{year}-{month:02d}"  # 格式化为"年-月"
        monthly_item = ArchiveBlogMonthly(
            month=month_str,
            list=blog_list
        )
        monthly_list.append(monthly_item)
    
    # 构造最终返回结果
    result = ArchiveBlogList(
        total_quantity=total_quantity,
        list=monthly_list
    )
    
    return result


def check_blog_password(db: Session, blog_id: int, password: str) -> bool:
    """
    检查博客密码是否正确
    
    Args:
        db: 数据库会话
        blog_id: 博客ID
        password: 输入的密码
        
    Returns:
        bool: 密码是否正确
    """
    # 获取博客
    blog = blog_crud.get_blog_by_id(db, blog_id=blog_id)
    
    if not blog:
        return False
    
    # 检查密码是否正确
    return blog.password == password
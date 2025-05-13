from sqlalchemy.orm import Session, joinedload
from app.models.blog import Blog
from app.models.category import Category
from app.models.tag import Tag
from typing import List, Optional, Tuple

def get_blogs_count(db: Session, is_published: bool = True) -> int:
    """
    获取博客总数
    
    Args:
        db: 数据库会话
        is_published: 是否已发布
        
    Returns:
        int: 博客总数
    """
    return db.query(Blog).filter(Blog.is_published == is_published).count()

def get_blogs_with_relations(
    db: Session, 
    skip: int = 0, 
    limit: int = 100, 
    is_published: bool = True,
    order_by = None
) -> List[Blog]:
    """
    获取博客列表，包含关联的分类和标签
    
    Args:
        db: 数据库会话
        skip: 跳过的记录数
        limit: 限制返回的记录数
        is_published: 是否已发布
        order_by: 排序条件
        
    Returns:
        List[Blog]: 博客列表
    """
    query = db.query(Blog).filter(Blog.is_published == is_published)\
        .options(joinedload(Blog.category), joinedload(Blog.tags))
    
    if order_by:
        if isinstance(order_by, list):
            for order in order_by:
                query = query.order_by(order)
        else:
            query = query.order_by(order_by)
    
    return query.offset(skip).limit(limit).all()

def get_blogs_by_category_name(
    db: Session, 
    category_name: str,
    skip: int = 0, 
    limit: int = 100, 
    is_published: bool = True,
    order_by = None
) -> Tuple[List[Blog], int]:
    """
    根据分类名称获取博客列表
    
    Args:
        db: 数据库会话
        category_name: 分类名称
        skip: 跳过的记录数
        limit: 限制返回的记录数
        is_published: 是否已发布
        order_by: 排序条件
        
    Returns:
        Tuple[List[Blog], int]: 博客列表和总数
    """
    # 先查询分类是否存在
    from app.models.category import Category
    
    # 查询符合条件的博客总数
    query = db.query(Blog).join(Category).filter(
        Category.category_name == category_name,
        Blog.is_published == is_published
    )
    
    total = query.count()
    
    # 查询博客列表，包含关联的分类和标签
    query = query.options(joinedload(Blog.category), joinedload(Blog.tags))
    
    if order_by:
        if isinstance(order_by, list):
            for order in order_by:
                query = query.order_by(order)
        else:
            query = query.order_by(order_by)
    
    blogs = query.offset(skip).limit(limit).all()
    
    return blogs, total
def get_blogs_by_tag_name(
    db: Session, 
    tag_name: str,
    skip: int = 0, 
    limit: int = 100, 
    is_published: bool = True,
    order_by = None
) -> Tuple[List[Blog], int]:
    """
    根据标签名称获取博客列表
    
    Args:
        db: 数据库会话
        tag_name: 标签名称
        skip: 跳过的记录数
        limit: 限制返回的记录数
        is_published: 是否已发布
        order_by: 排序条件
        
    Returns:
        Tuple[List[Blog], int]: 博客列表和总数
    """
    # 查询符合条件的博客总数
    query = db.query(Blog).join(Blog.tags).filter(
        Tag.tag_name == tag_name,
        Blog.is_published == is_published
    )
    
    total = query.count()
    
    # 查询博客列表，包含关联的分类和标签
    query = query.options(joinedload(Blog.category), joinedload(Blog.tags))
    
    if order_by:
        if isinstance(order_by, list):
            for order in order_by:
                query = query.order_by(order)
        else:
            query = query.order_by(order_by)
    
    blogs = query.offset(skip).limit(limit).all()
    
    return blogs, total


def get_blog_by_id(db: Session, blog_id: int, is_published: bool = True) -> Optional[Blog]:
    """
    根据ID获取博客详情
    
    Args:
        db: 数据库会话
        blog_id: 博客ID
        is_published: 是否已发布
        
    Returns:
        Optional[Blog]: 博客详情，如果不存在则返回None
    """
    query = db.query(Blog).filter(Blog.id == blog_id)
    
    if is_published:
        query = query.filter(Blog.is_published == is_published)
    
    # 加载关联的分类和标签
    return query.options(joinedload(Blog.category), joinedload(Blog.tags)).first()


def get_blog_archives(db: Session, is_published: bool = True) -> List[Tuple[int, int, List[Blog]]]:
    """
    获取博客归档数据，按年月分组
    
    Args:
        db: 数据库会话
        is_published: 是否已发布
        
    Returns:
        List[Tuple[int, int, List[Blog]]]: 归档数据列表，每项包含年、月和对应的博客列表
    """
    # 获取所有已发布的博客，按创建时间降序排序
    blogs = db.query(Blog).filter(Blog.is_published == is_published)\
        .order_by(Blog.create_time.desc())\
        .options(joinedload(Blog.category), joinedload(Blog.tags))\
        .all()
    
    # 按年月分组
    archives = {}
    for blog in blogs:
        year = blog.create_time.year
        month = blog.create_time.month
        
        if (year, month) not in archives:
            archives[(year, month)] = []
        
        archives[(year, month)].append(blog)
    
    # 转换为列表格式，按年月降序排序
    result = []
    for (year, month), blog_list in sorted(archives.items(), key=lambda x: (x[0][0], x[0][1]), reverse=True):
        result.append((year, month, blog_list))
    
    return result
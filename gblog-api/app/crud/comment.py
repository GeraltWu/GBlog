from sqlalchemy.orm import Session
from app.models.comment import Comment
from app.models.blog import Blog
from typing import List, Tuple, Optional
from sqlalchemy import desc

def get_comments_count(db: Session, page: int, blog_id: Optional[int] = None) -> int:
    """
    获取评论总数
    
    Args:
        db: 数据库会话
        page: 页面分类（0普通文章，1关于我...）
        blog_id: 博客ID（当page=0时需要）
        
    Returns:
        int: 评论总数
    """
    query = db.query(Comment).filter(
        Comment.is_published == True,
        Comment.page == page
    )
    
    if page == 0 and blog_id is not None:
        print("开始筛选")
        query = query.filter(Comment.blog_id == blog_id)
    
    return query.count()

def get_comments_by_page_and_blog_id(
    db: Session,
    page: int,
    blog_id: Optional[int] = None,
    skip: int = 0,
    limit: int = 10
) -> List[Comment]:
    """
    根据页面类型和博客ID获取评论列表
    
    Args:
        db: 数据库会话
        page: 页面分类（0普通文章，1关于我...）
        blog_id: 博客ID（当page=0时需要）
        skip: 跳过的记录数
        limit: 限制返回的记录数
        
    Returns:
        List[Comment]: 评论列表
    """
    # 查询根评论（parent_comment_id = -1）
    query = db.query(Comment).filter(
        Comment.is_published == True,
        Comment.page == page,
        Comment.parent_comment_id == -1
    )
    
    if page == 0 and blog_id is not None:
        query = query.filter(Comment.blog_id == blog_id)
    print("blog_id:", blog_id)
    # 按创建时间降序排序
    root_comments = query.order_by(desc(Comment.create_time)).offset(skip).limit(limit).all()
    
    return root_comments

def get_reply_comments(db: Session, root_comment_id: int) -> List[Comment]:
    """
    获取指定根评论下的所有回复，按创建时间升序排序
    
    Args:
        db: 数据库会话
        root_comment_id: 根评论ID
        
    Returns:
        List[Comment]: 回复评论列表
    """
    return db.query(Comment).filter(
        Comment.is_published == True,
        Comment.root_comment_id == root_comment_id,
        Comment.parent_comment_id != -1
    ).order_by(Comment.create_time).all()

def get_comment_by_id(db: Session, comment_id: int) -> Optional[Comment]:
    """
    根据ID获取评论
    
    Args:
        db: 数据库会话
        comment_id: 评论ID
        
    Returns:
        Optional[Comment]: 评论对象，如果不存在则返回None
    """
    return db.query(Comment).filter(Comment.id == comment_id).first()

def is_comment_enabled_for_blog(db: Session, blog_id: int) -> bool:
    """
    检查博客是否启用评论功能
    
    Args:
        db: 数据库会话
        blog_id: 博客ID
        
    Returns:
        bool: 是否启用评论
    """
    blog = db.query(Blog).filter(Blog.id == blog_id).first()
    return blog is not None and blog.is_comment_enabled


def create_comment(db: Session, comment: Comment) -> Comment:
    """
    创建评论
    
    Args:
        db: 数据库会话
        comment: 评论对象
        
    Returns:
        Comment: 创建后的评论对象
    """
    db.add(comment)
    db.commit()
    db.refresh(comment)
    return comment


def get_unpublished_comments_count(db: Session, page: Optional[int] = None, blog_id: Optional[int] = None) -> int:
    """
    获取未发布（被隐藏）的评论数量
    
    Args:
        db: 数据库会话
        page: 页面分类（0普通文章，1关于我...）
        blog_id: 博客ID（当page=0时需要）
        
    Returns:
        int: 未发布的评论数量
    """
    query = db.query(Comment).filter(Comment.is_published == False)
    
    if page is not None:
        query = query.filter(Comment.page == page)
    
    if page == 0 and blog_id is not None:
        query = query.filter(Comment.blog_id == blog_id)
    
    return query.count()
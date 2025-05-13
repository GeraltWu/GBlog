from fastapi import APIRouter, Depends, Query, Body
from sqlalchemy.orm import Session
from typing import Optional, List

from app.database.database import get_db
from app.services import blog_service
from app.schemas.common import Result, PageResult
from app.schemas.blog import BlogList, BlogDetail, ArchiveBlogList
from app.schemas.blog import BlogPasswordForm

router = APIRouter()

@router.get("/blogs", response_model=Result[PageResult[BlogList]])
def get_blogs(
    db: Session = Depends(get_db),
    page_num: Optional[int] = Query(1, alias="pageNum", ge=1)
):
    """
    获取博客列表
    
    Args:
        db: 数据库会话
        page_num: 页码，从1开始
        
    Returns:
        Result[PageResult[BlogList]]: 统一响应格式
    """
    # 每页显示10条数据
    page_size = 10
    
    # 调用service层处理业务逻辑
    blogs, total_page = blog_service.get_blog_list(db, page_num, page_size)
    
    # 构造分页响应数据
    page_result = PageResult(
        total_page=total_page,
        list=blogs
    )
    
    # 返回统一响应格式
    return Result.success(data=page_result)

@router.get("/category", response_model=Result[PageResult[BlogList]])
def get_blogs_by_category_name(
    category_name: str = Query(..., alias="categoryName", description="分类名称"),
    db: Session = Depends(get_db),
    page_num: Optional[int] = Query(1, alias="pageNum", ge=1)
):
    """
    根据分类名称获取博客列表
    
    Args:
        category_name: 分类名称（查询参数）
        db: 数据库会话
        page_num: 页码，从1开始
        
    Returns:
        Result[PageResult[BlogList]]: 统一响应格式
    """
    # 每页显示10条数据
    page_size = 10
    
    # 调用service层处理业务逻辑
    blogs, total_page = blog_service.get_blog_list_by_category_name(db, category_name, page_num, page_size)
    
    # 构造分页响应数据
    page_result = PageResult(
        total_page=total_page,
        list=blogs
    )
    
    # 返回统一响应格式
    return Result.success(data=page_result)

@router.get("/tag", response_model=Result[PageResult[BlogList]])
def get_blogs_by_tag_name(
    tag_name: str = Query(..., alias="tagName", description="标签名称"),
    db: Session = Depends(get_db),
    page_num: Optional[int] = Query(1, alias="pageNum", ge=1)
):
    """
    根据标签名称获取博客列表
    
    Args:
        tag_name: 标签名称（查询参数）
        db: 数据库会话
        page_num: 页码，从1开始
        
    Returns:
        Result[PageResult[BlogList]]: 统一响应格式
    """
    # 每页显示10条数据
    page_size = 10
    
    # 调用service层处理业务逻辑
    blogs, total_page = blog_service.get_blog_list_by_tag_name(db, tag_name, page_num, page_size)
    
    # 构造分页响应数据
    page_result = PageResult(
        total_page=total_page,
        list=blogs
    )
    
    # 返回统一响应格式
    return Result.success(data=page_result)

@router.get("/blog", response_model=Result[BlogDetail])
def get_blog_by_id(
    id: int = Query(..., description="博客ID"),
    db: Session = Depends(get_db)
):
    """
    根据ID获取博客详情
    
    Args:
        id: 博客ID（查询参数）
        db: 数据库会话
        
    Returns:
        Result[BlogDetail]: 统一响应格式
    """
    # 调用service层处理业务逻辑
    blog = blog_service.get_blog_by_id(db, blog_id=id)
    
    # 如果博客不存在，返回错误信息
    if not blog:
        return Result.fail(message="该博客不存在")
    
    # 返回统一响应格式
    return Result.success(data=blog)

@router.get("/archives", response_model=Result[ArchiveBlogList])
def get_archives(
    db: Session = Depends(get_db)
):
    """
    获取博客归档数据
    
    Args:
        db: 数据库会话
        
    Returns:
        Result[ArchiveBlogList]: 统一响应格式，包含归档数据
    """
    # 调用service层处理业务逻辑
    archives = blog_service.get_blog_archives(db)
    
    # 返回统一响应格式
    return Result.success(data=archives)


@router.post("/check-blog-password", response_model=Result)
def check_blog_password(
    password_form: BlogPasswordForm = Body(...),
    db: Session = Depends(get_db)
):
    """
    检查博客密码
    
    Args:
        password_form: 博客密码表单
        db: 数据库会话
        
    Returns:
        Result: 统一响应格式
    """
    print(password_form)
    print("11")
    # 调用service层处理业务逻辑
    is_correct = blog_service.check_blog_password(db, password_form.blogId, password_form.password)
    
    if not is_correct:
        return Result.fail(msgg="密码错误")
    
    # 返回统一响应格式
    return Result.success(msg="密码正确")
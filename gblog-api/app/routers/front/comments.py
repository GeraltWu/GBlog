from fastapi import APIRouter, Depends, Query, Body
from sqlalchemy.orm import Session
from typing import Optional

from app.database.database import get_db
from app.services import comment_service
from app.schemas.common import Result
from app.schemas.comment import CommentQuery, CommentForm

router = APIRouter()

@router.get("/comments", response_model=Result)
def get_comment_list_by_query(
    query: CommentQuery = Depends(),
    db: Session = Depends(get_db)
):
    """
    根据查询条件获取评论列表
    
    Args:
        query: 评论查询参数
        db: 数据库会话
        
    Returns:
        Result: 统一响应格式
    """
    # 直接传递整个查询对象
    comments_data = comment_service.get_comment_list_by_query(db, query)
    
    # 返回统一响应格式
    return Result.success(data=comments_data)


@router.post("/comment", response_model=Result)
def submit_comment(
    comment_form: CommentForm = Body(...),
    db: Session = Depends(get_db)
):
    """
    提交评论
    
    Args:
        comment_form: 评论表单数据
        db: 数据库会话
        
    Returns:
        Result: 统一响应格式
    """
    # 调用service层处理业务逻辑
    success = comment_service.add_comment(db, comment_form)
    
    if not success:
        return Result.fail(msg="评论提交失败")
    
    # 返回统一响应格式
    return Result.success(msg="评论提交成功")
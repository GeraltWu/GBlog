from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import Optional

from app.database.database import get_db
from app.services import moment_service
from app.schemas.common import Result, PageResult
from app.schemas.moment import MomentList

router = APIRouter()

@router.get("/moments", response_model=Result[PageResult[MomentList]])
def get_moments(
    db: Session = Depends(get_db),
    page_num: Optional[int] = Query(1, alias="pageNum", ge=1)
):
    """
    获取动态列表
    
    Args:
        db: 数据库会话
        page_num: 页码，从1开始
        
    Returns:
        Result[PageResult[MomentList]]: 统一响应格式
    """
    # 每页显示10条数据
    page_size = 10
    
    # 调用service层处理业务逻辑
    moments, total_page = moment_service.get_moment_list(db, page_num, page_size)
    
    # 构造分页响应数据
    page_result = PageResult(
        total_page=total_page,
        list=moments
    )
    
    # 返回统一响应格式
    return Result.success(data=page_result)

@router.post("/moment/like/{id}", response_model=Result)
def like_moment(
    id: int,
    db: Session = Depends(get_db)
):
    """
    给动态点赞
    
    Args:
        id: 动态ID
        db: 数据库会话
        
    Returns:
        Result: 统一响应格式
    """
    # 调用service层处理业务逻辑
    success = moment_service.like_moment(db, moment_id=id)
    
    if not success:
        return Result.fail(msg="点赞失败，该动态可能不存在")
    
    # 返回统一响应格式
    return Result.success(msg="点赞成功")
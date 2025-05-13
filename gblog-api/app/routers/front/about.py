from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.services import about_service
from app.schemas.common import Result
from app.schemas.about import AboutResponse

router = APIRouter()

@router.get("/about", response_model=Result[AboutResponse])
def get_about(db: Session = Depends(get_db)):
    """
    获取关于我页面信息
    
    Args:
        db: 数据库会话
        
    Returns:
        Result[AboutResponse]: 统一响应格式
    """
    # 获取关于我页面信息
    about_info = about_service.get_about_info(db)
    
    # 返回统一响应格式
    return Result.success(data=about_info)
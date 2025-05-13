from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.services import site_service
from app.schemas.common import Result
from app.schemas.site import SiteResponse

router = APIRouter()

@router.get("/site", response_model=Result[SiteResponse])
def get_site(db: Session = Depends(get_db)):
    """
    获取站点信息
    
    Args:
        db: 数据库会话
        
    Returns:
        Result[SiteResponse]: 统一响应格式
    """
    # 调用service层获取站点信息
    site_data = site_service.get_site_info(db)
    
    # 返回统一响应格式
    return Result.success(data=site_data)
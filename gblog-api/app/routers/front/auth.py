from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.schemas.user import UserLogin, UserLoginResponse
from app.services.user_service import authenticate_user
from app.schemas.common import Result

router = APIRouter()

@router.post("/login", response_model=Result[UserLoginResponse])
def login(login_data: UserLogin, db: Session = Depends(get_db)):
    """
    用户登录接口
    
    Args:
        login_data: 用户登录数据
        db: 数据库会话
        
    Returns:
        UserLoginResponse: 包含token的响应
    """
    # 调用服务层进行用户认证
    result = authenticate_user(db, login_data)
    
    # 如果认证失败，返回401错误
    if not result:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="用户名或密码错误",
            headers={"Authenticate": "Bearer"},
        )
    
    # 返回包含token的响应
    return Result.success(data=result)
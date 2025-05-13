from sqlalchemy.orm import Session
from app.crud import about as about_crud
from app.schemas.about import AboutResponse
from typing import Optional

def get_about_info(db: Session) -> Optional[AboutResponse]:
    """
    获取关于我页面信息
    
    Args:
        db: 数据库会话
        
    Returns:
        Optional[AboutResponse]: 关于我页面信息
    """
    about_items = about_crud.get_about_items(db)
    
    # 初始化数据
    title = ""
    music_id = ""
    content = ""
    comment_enabled = False
    
    # 遍历所有配置项，根据 name_en 填充数据
    for item in about_items:
        if item.name_en == "title":
            title = item.value
        elif item.name_en == "musicId":
            music_id = item.value
        elif item.name_en == "content":
            content = item.value
        elif item.name_en == "commentEnabled":
            comment_enabled = item.value.lower() == "true"
    
    # 创建并返回Pydantic对象
    return AboutResponse(
        title=title,
        musicId=music_id,
        content=content,
        commentEnabled=comment_enabled
    )
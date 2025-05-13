from app.schemas.common import CamelModel

class AboutResponse(CamelModel):
    title: str
    music_id: str  # 这里使用下划线命名，会自动转换为驼峰命名 musicId
    content: str
    comment_enabled: bool  # 这里使用下划线命名，会自动转换为驼峰命名 commentEnabled
    
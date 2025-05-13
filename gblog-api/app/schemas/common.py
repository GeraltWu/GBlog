from typing import Generic, TypeVar, Optional, Any, List
from pydantic import BaseModel, ConfigDict

T = TypeVar('T')
P = TypeVar('P')

def to_camel(string: str) -> str:
    """将下划线命名转换为驼峰命名"""
    words = string.split('_')
    return words[0] + ''.join(word.capitalize() for word in words[1:])

class CamelModel(BaseModel):
    """支持驼峰命名的基础模型"""
    model_config = ConfigDict(
        from_attributes=True,
        alias_generator=to_camel,
        populate_by_name=True
    )

class Result(CamelModel, Generic[T]):
    """统一响应实体"""
    code: int = 200
    msg: str = "操作成功"
    data: Optional[T] = None
    
    @classmethod
    def success(cls, data: Any = None, msg: str = "操作成功") -> "Result":
        """成功响应"""
        return cls(code=200, msg=msg, data=data)
    
    @classmethod
    def fail(cls, msg: str = "操作失败", code: int = 400) -> "Result":
        """失败响应"""
        return cls(code=code, msg=msg)
    
    @classmethod
    def error(cls, msg: str = "服务器错误", code: int = 500) -> "Result":
        """错误响应"""
        return cls(code=code, msg=msg)

class PageResult(CamelModel, Generic[P]):
    """统一分页响应实体"""
    total_page: int
    list: List[P]
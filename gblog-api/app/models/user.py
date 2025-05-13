from sqlalchemy import Column, String, DateTime, BigInteger
from datetime import datetime
from app.database.database import Base

class User(Base):
    __tablename__ = "user"
    
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    username = Column(String(255), nullable=False, comment="用户名")
    password = Column(String(255), nullable=False, comment="密码")
    nickname = Column(String(255), nullable=False, comment="昵称")
    avatar = Column(String(255), nullable=False, comment="头像地址")
    email = Column(String(255), nullable=False, comment="邮箱")
    create_time = Column(DateTime, nullable=False, comment="创建时间")
    update_time = Column(DateTime, nullable=False, comment="更新时间")
    role = Column(String(255), nullable=False, comment="角色访问权限")
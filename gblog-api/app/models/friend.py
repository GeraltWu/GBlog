from sqlalchemy import Column, String, DateTime, Integer, BigInteger
from sqlalchemy.dialects.mysql import BIT
from datetime import datetime
from app.database.database import Base

class Friend(Base):
    __tablename__ = "friend"
    
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    nickname = Column(String(255), nullable=False, comment="昵称")
    description = Column(String(255), nullable=False, comment="描述")
    website = Column(String(255), nullable=False, comment="站点")
    avatar = Column(String(255), nullable=False, comment="头像")
    is_published = Column(BIT(1), nullable=False, comment="公开或隐藏")
    views = Column(Integer, nullable=False, comment="点击次数")
    create_time = Column(DateTime, nullable=False, comment="创建时间")
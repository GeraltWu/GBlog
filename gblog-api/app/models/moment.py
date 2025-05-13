from sqlalchemy import Column, Text, DateTime, Integer, BigInteger
from sqlalchemy.dialects.mysql import BIT
from datetime import datetime
from app.database.database import Base

class Moment(Base):
    __tablename__ = "moment"
    
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    content = Column(Text, nullable=False, comment="动态内容")
    create_time = Column(DateTime, nullable=False, comment="创建时间")
    likes = Column(Integer, comment="点赞数量")
    is_published = Column(BIT(1), nullable=False, comment="是否公开")
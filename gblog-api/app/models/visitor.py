from sqlalchemy import Column, String, DateTime, Integer, BigInteger
from datetime import datetime
from app.database.database import Base

class Visitor(Base):
    __tablename__ = "visitor"
    
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    uuid = Column(String(36), nullable=False, unique=True, comment="访客标识码")
    ip = Column(String(255), comment="ip")
    ip_source = Column(String(255), comment="ip来源")
    os = Column(String(255), comment="操作系统")
    browser = Column(String(255), comment="浏览器")
    create_time = Column(DateTime, nullable=False, comment="首次访问时间")
    last_time = Column(DateTime, nullable=False, comment="最后访问时间")
    pv = Column(Integer, comment="访问页数统计")
    user_agent = Column(String(2000), comment="user-agent用户代理")
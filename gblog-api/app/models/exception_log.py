from sqlalchemy import Column, String, Text, DateTime, BigInteger
from datetime import datetime
from app.database.database import Base

class ExceptionLog(Base):
    __tablename__ = "exception_log"
    
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    uri = Column(String(255), nullable=False, comment="请求接口")
    method = Column(String(255), nullable=False, comment="请求方式")
    param = Column(String(2000), comment="请求参数")
    description = Column(String(255), comment="操作描述")
    error = Column(Text, comment="异常信息")
    ip = Column(String(255), comment="ip")
    ip_source = Column(String(255), comment="ip来源")
    os = Column(String(255), comment="操作系统")
    browser = Column(String(255), comment="浏览器")
    create_time = Column(DateTime, nullable=False, comment="操作时间")
    user_agent = Column(String(2000), comment="user-agent用户代理")
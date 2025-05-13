from sqlalchemy import Column, String, DateTime, Boolean, BigInteger
from datetime import datetime
from app.database.database import Base

class LoginLog(Base):
    __tablename__ = "login_log"
    
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    username = Column(String(255), nullable=False, comment="用户名称")
    ip = Column(String(255), comment="ip")
    ip_source = Column(String(255), comment="ip来源")
    os = Column(String(255), comment="操作系统")
    browser = Column(String(255), comment="浏览器")
    status = Column(Boolean, comment="登录状态")
    description = Column(String(255), comment="操作描述")
    create_time = Column(DateTime, nullable=False, comment="登录时间")
    user_agent = Column(String(2000), comment="user-agent用户代理")
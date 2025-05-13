from sqlalchemy import Column, String, DateTime, Integer, BigInteger
from datetime import datetime
from app.database.database import Base

class VisitLog(Base):
    __tablename__ = "visit_log"
    
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    uuid = Column(String(36), comment="访客标识码")
    uri = Column(String(255), nullable=False, comment="请求接口")
    method = Column(String(255), nullable=False, comment="请求方式")
    param = Column(String(2000), nullable=False, comment="请求参数")
    behavior = Column(String(255), comment="访问行为")
    content = Column(String(255), comment="访问内容")
    remark = Column(String(255), comment="备注")
    ip = Column(String(255), comment="ip")
    ip_source = Column(String(255), comment="ip来源")
    os = Column(String(255), comment="操作系统")
    browser = Column(String(255), comment="浏览器")
    times = Column(Integer, nullable=False, comment="请求耗时（毫秒）")
    create_time = Column(DateTime, nullable=False, comment="访问时间")
    user_agent = Column(String(2000), comment="user-agent用户代理")
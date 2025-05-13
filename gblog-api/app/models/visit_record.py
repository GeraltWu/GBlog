from sqlalchemy import Column, String, Integer, BigInteger
from app.database.database import Base

class VisitRecord(Base):
    __tablename__ = "visit_record"
    
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    pv = Column(Integer, nullable=False, comment="访问量")
    uv = Column(Integer, nullable=False, comment="独立用户")
    date = Column(String(255), nullable=False, comment='日期"02-23"')
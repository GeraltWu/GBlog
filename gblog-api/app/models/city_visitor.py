from sqlalchemy import Column, String, Integer
from app.database.database import Base

class CityVisitor(Base):
    __tablename__ = "city_visitor"
    
    city = Column(String(255), primary_key=True, comment="城市名称")
    uv = Column(Integer, nullable=False, comment="独立访客数量")
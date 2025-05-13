from sqlalchemy import Column, String, Text, BigInteger
from app.database.database import Base

class About(Base):
    __tablename__ = "about"
    
    id = Column(BigInteger, primary_key=True)
    name_en = Column(String(255))
    name_zh = Column(String(255))
    value = Column(Text)
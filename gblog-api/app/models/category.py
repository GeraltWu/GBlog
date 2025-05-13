from sqlalchemy import Column, String, BigInteger
from sqlalchemy.orm import relationship
from app.database.database import Base

class Category(Base):
    __tablename__ = "category"
    
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    category_name = Column(String(255), nullable=False)
    
    # 关系
    blogs = relationship("Blog", back_populates="category")
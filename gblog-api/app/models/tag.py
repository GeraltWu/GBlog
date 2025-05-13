from sqlalchemy import Column, String, Table, ForeignKey, BigInteger
from sqlalchemy.orm import relationship
from app.database.database import Base

# 博客-标签关联表
blog_tag = Table(
    'blog_tag',
    Base.metadata,
    Column('blog_id', BigInteger, ForeignKey('blog.id')),
    Column('tag_id', BigInteger, ForeignKey('tag.id'))
)

class Tag(Base):
    __tablename__ = "tag"
    
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    tag_name = Column(String(255), nullable=False)
    color = Column(String(255), comment="标签颜色(可选)")
    
    # 关系
    blogs = relationship("Blog", secondary=blog_tag, back_populates="tags")
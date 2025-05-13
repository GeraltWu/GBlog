from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, BigInteger
from sqlalchemy.dialects.mysql import BIT
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database.database import Base

class Blog(Base):
    __tablename__ = "blog"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False, comment="文章标题")
    first_picture = Column(String(255), nullable=False, comment="文章首图，用于随机文章展示")
    content = Column(Text, nullable=False, comment="文章正文")
    description = Column(Text, nullable=False, comment="描述")
    is_published = Column(BIT(1), nullable=False, comment="公开或私密")
    is_recommend = Column(BIT(1), nullable=False, comment="推荐开关")
    is_appreciation_enabled = Column(BIT(1), nullable=False, comment="赞赏开关")
    is_comment_enabled = Column(BIT(1), nullable=False, comment="评论开关")
    is_private = Column(BIT(1), nullable=False)
    is_top = Column(BIT(1), nullable=False, comment="是否置顶")
    create_time = Column(DateTime, nullable=False, comment="创建时间")
    update_time = Column(DateTime, nullable=False, comment="更新时间")
    views = Column(Integer, nullable=False, comment="浏览次数")
    words = Column(Integer, nullable=False, comment="文章字数")
    read_time = Column(Integer, nullable=False, comment="阅读时长(分钟)")
    category_id = Column(BigInteger, ForeignKey("category.id"), nullable=False, comment="文章分类")
    password = Column(String(255), comment="密码保护")
    
    # 关系
    category = relationship("Category", back_populates="blogs")
    tags = relationship("Tag", secondary="blog_tag", back_populates="blogs")
    # comments = relationship("Comment", back_populates="blog")
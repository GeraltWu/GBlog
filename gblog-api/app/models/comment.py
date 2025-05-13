from sqlalchemy import Column, String, Text, DateTime, Integer, ForeignKey, BigInteger
from sqlalchemy.dialects.mysql import BIT
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database.database import Base

class Comment(Base):
    __tablename__ = "comment"
    
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    nickname = Column(String(255), nullable=False, comment="昵称")
    email = Column(String(255), nullable=False, comment="邮箱")
    qq = Column(String(255), comment="如果评论昵称为QQ号，则将昵称和头像置为QQ昵称和QQ头像，并将此字段置为QQ号备份")
    avatar = Column(String(255), nullable=False, comment="头像(图片路径)")
    ip = Column(String(255), comment="评论者ip地址")
    website = Column(String(255), comment="个人网站")
    content = Column(String(255), nullable=False, comment="评论内容")
    create_time = Column(DateTime, comment="评论时间")
    is_published = Column(BIT(1), nullable=False, comment="公开或回收站")
    is_admin_comment = Column(BIT(1), nullable=False, comment="博主回复")
    page = Column(Integer, nullable=False, comment="0普通文章，1关于我页面，2友链页面")
    is_notice = Column(BIT(1), nullable=False, comment="接收邮件提醒")
    blog_id = Column(BigInteger, ForeignKey("blog.id"), comment="所属的文章")
    root_comment_id = Column(BigInteger, nullable=False, comment="所属根评论id，顶级评论为-1")
    parent_comment_id = Column(BigInteger, nullable=False, comment="父评论id，-1为根评论")
    
    # 关系
    # blog = relationship("Blog", back_populates="comments")
    # replies = relationship("Comment", backref="parent", remote_side=[id])
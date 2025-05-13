from sqlalchemy import Column, String, Text, Integer, BigInteger
from app.database.database import Base

class SiteSetting(Base):
    __tablename__ = "site_setting"
    
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    name_en = Column(String(255))
    name_zh = Column(String(255))
    value = Column(Text)
    type = Column(Integer, comment="1基础设置，2页脚徽标，3资料卡，4友链信息")
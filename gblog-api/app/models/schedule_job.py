from sqlalchemy import Column, String, DateTime, Integer, BigInteger
from datetime import datetime
from app.database.database import Base

class ScheduleJob(Base):
    __tablename__ = "schedule_job"
    
    job_id = Column(BigInteger, primary_key=True, autoincrement=True, comment="任务id")
    bean_name = Column(String(255), comment="spring bean名称")
    method_name = Column(String(255), comment="方法名")
    params = Column(String(255), comment="参数")
    cron = Column(String(255), comment="cron表达式")
    status = Column(Integer, comment="任务状态")
    remark = Column(String(255), comment="备注")
    create_time = Column(DateTime, comment="创建时间")
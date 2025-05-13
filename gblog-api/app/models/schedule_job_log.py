from sqlalchemy import Column, String, Text, DateTime, Integer, BigInteger
from datetime import datetime
from app.database.database import Base

class ScheduleJobLog(Base):
    __tablename__ = "schedule_job_log"
    
    log_id = Column(BigInteger, primary_key=True, autoincrement=True, comment="任务日志id")
    job_id = Column(BigInteger, nullable=False, comment="任务id")
    bean_name = Column(String(255), comment="spring bean名称")
    method_name = Column(String(255), comment="方法名")
    params = Column(String(255), comment="参数")
    status = Column(Integer, nullable=False, comment="任务执行结果")
    error = Column(Text, comment="异常信息")
    times = Column(Integer, nullable=False, comment="耗时（单位：毫秒）")
    create_time = Column(DateTime, comment="创建时间")
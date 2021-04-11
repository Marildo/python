from datetime import datetime

from sqlalchemy import Column, INTEGER, String, DATETIME, BOOLEAN
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Action(Base):
    __tablename__ = 'action'
    id = Column(INTEGER, primary_key=True)
    description = Column(String(510), nullable=False, default='')
    init = Column(DATETIME, default=datetime.now())
    finish = Column(DATETIME, nullable=True)
    finished = Column(BOOLEAN, nullable=False, default=False)

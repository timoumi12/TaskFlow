#!/usr/bin/python3
"""tasks"""
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from datetime import datetime

from models.base import Base, utils
class task(utils, Base):
    __tablename__ = "task"
    id = Column(Integer, autoincrement=True, primary_key=True)
    title = Column(String(128), nullable=False)
    member_id = Column(Integer, ForeignKey("user.id"))
    workspace_id = Column(Integer, ForeignKey("workspace.id"))
    start_date = Column(DateTime, default=datetime.utcnow, nullable=False)
    due_date = Column(DateTime, default=datetime.utcnow, nullable=False)
    priority = Column(String(128), nullable=True)
    description = Column(String(128), nullable=True)
    state = Column(String(128))

#!/usr/bin/python3
"""workspaces"""
import sqlalchemy
from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, MetaData, Table
from datetime import datetime
from sqlalchemy.orm import relationship
import uuid
from sqlalchemy.ext.declarative import declarative_base


from models.base import Base, utils
metadata = MetaData()

user_workspace = Table('members', Base.metadata,
                Column('workspace_id',
                           Integer,
                           ForeignKey('workspace.id', onupdate="CASCADE", ondelete="CASCADE"),  primary_key=True),
                Column('user_id',
                           Integer,
                           ForeignKey('user.id', onupdate="CASCADE", ondelete="CASCADE"),  primary_key=True)
                )

class workspace(utils, Base):
    "Workspace Representation"
    __tablename__ = "workspace"
    id = Column(Integer, autoincrement=True, primary_key=True)
    id_admin = Column(Integer, ForeignKey("user.id"))
    name = Column(String(64), nullable=False)
    date_c = Column(DateTime, default=datetime.utcnow, nullable=False)
    code = Column(String(128), default=lambda : str(uuid.uuid4().hex)[:6])
    members = relationship("user",
                           secondary=user_workspace,
                           viewonly=False)

#!/usr/bin/python3
"""users"""
import sqlalchemy
from sqlalchemy import Column, String, Integer
from datetime import datetime
import uuid
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from models.workspaces import user_workspace
from models.base import Base, utils

class user(utils, Base):
    """User Representation"""
    __tablename__ = "user"
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False, unique=True)
    password = Column(String(128), nullable=False)
    workspaces = relationship("workspace", secondary=user_workspace, back_populates="members", overlaps="members")

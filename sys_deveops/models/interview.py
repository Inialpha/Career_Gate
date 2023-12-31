#!/usr/bin/python3
"""This module contains the Interview class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship


class Interview(BaseModel, Base):
    """definition of an Interview instance"""
    __tablename__ = "interviews"

    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    content = Column(String(1024), nullable=False)
    details = Column(Boolean, default=False)


#!/usr/bin/python3
"""This module contains the Interview class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Boolean, DateTime
from sqlalchemy.orm import relationship


class Interview(BaseModel, Base):
    """definition of an Interview instance"""
    __tablename__ = "interviews"

    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    resume_link = Column(String(1024), nullable=False)
    application_link = Column(String(1024), nullable=False)

    status = Column(String(60), default="Pending" )
    datails = Column(String(1024))
    meeting_password = Column(String(60), nullable=False)
    meeting_date = Column(DateTime)
    meeting_link = Column(String(1024), nullable=False)

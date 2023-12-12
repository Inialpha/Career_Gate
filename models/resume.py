#!/usr/bin/python
""" holds class Review"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, Boolean


class Resume(BaseModel, Base):
    """Representation of Resume """
    if models.storage_t == 'db':
        __tablename__ = 'resumes'
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        resume_link = Column(String(1024), nullable=False)
        status = Column(String(60), default="Pending")
        review = Column(String(1024))
    else:
        place_id = ""
        user_id = ""
        text = ""

    def __init__(self, *args, **kwargs):
        """initializes Review"""
        super().__init__(*args, **kwargs)

from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Category:
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String, primary_key=True)
    is_active = Column(Boolean)

    def __str__(self):
        return self.name


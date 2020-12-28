from sqlalchemy import Column, String, Integer

from base import Base


class Store(Base):
    __tablename__ = 'store'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name

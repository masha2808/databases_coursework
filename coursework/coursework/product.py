from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from base import Base


class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship('Category')
    store_id = Column(Integer, ForeignKey('store.id'))
    store = relationship('Store')
    rating = Column(Integer)
    price = Column(Integer)

    def __init__(self, name, category_id, store_id, price):
        self.name = name
        self.category_id = category_id
        self.store_id = store_id
        self.price = price

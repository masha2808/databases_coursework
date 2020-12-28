from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from base import Base


class Review(Base):
    __tablename__ = 'review'

    id = Column(Integer, primary_key=True)
    rating = Column(Integer)
    product_id = Column(Integer, ForeignKey('product.id'))
    product = relationship('Product')
    customer_email = Column(String, ForeignKey('customer.email'))
    reader = relationship('Customer')

    def __init__(self, rating, product_id, customer_email):
        self.rating = rating
        self.product_id = product_id
        self.customer_email = customer_email

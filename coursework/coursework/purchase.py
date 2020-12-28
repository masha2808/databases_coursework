from sqlalchemy import Column, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship

from base import Base


class Purchase(Base):
    __tablename__ = 'purchase'

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('product.id'))
    product = relationship('Product')
    date_time = Column(Date)

    def __init__(self, product_id, date_time):
        self.product_id = product_id
        self.date_time = date_time

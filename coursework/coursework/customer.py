from sqlalchemy import Column, String

from base import Base


class Customer(Base):
    __tablename__ = 'customer'

    email = Column(String, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)

    def __init__(self, email, first_name, last_name):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name

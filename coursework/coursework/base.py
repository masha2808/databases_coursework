from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgres://postgres:masha2001@localhost:5432/course_work')
Session = sessionmaker(bind=engine)

Base = declarative_base()

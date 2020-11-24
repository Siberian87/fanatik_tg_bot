from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///fan.db')
Session = sessionmaker(bind=engine)
session = Session()


Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, unique=True)

    def __repr__(self):
        return f"{self.user_id}"


Base.metadata.create_all(engine)


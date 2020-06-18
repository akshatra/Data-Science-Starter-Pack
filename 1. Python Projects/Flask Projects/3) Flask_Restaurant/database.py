from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Restaurant(Base):
    __tablename__ = 'restaurant'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(250), nullable=False)
    address = Column(String(1000), nullable=False)


engine = create_engine("sqlite:///restaurantmenu.db")

Base.metadata.create_all(engine)

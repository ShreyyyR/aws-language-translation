from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class UserData(Base):
    __tablename__ = "user_data"

    id = Column(Integer, primary_key=True, index=True)
    name_en = Column(String, nullable=False)
    name_kn = Column(String, nullable=False)
    address_en = Column(String, nullable=False)
    address_kn = Column(String, nullable=False)

from flask import SQLAlchemy
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table, primary_key
from sqlalchemy.orm import relationship, Sessionmaker, Session, Metadata, declarative_base

engine = create_engine("sqlite:///datdabase.db")

Base= declarative_base()

class Userdata(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(20), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(60), nullable=False)

Session = Sessionmaker(bind=engine)

Base.metadata.create_all(engine)

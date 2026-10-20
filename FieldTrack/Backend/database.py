from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "sqlite:///./fieldtrack.db" # create and use SQLite database called fieldtrack.db

engine = create_engine(
    DATABASE_URL,
connect_args={"check_same_thread": False}
) # links database and SQLite

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
Base = declarative_base() #will use to create database tables
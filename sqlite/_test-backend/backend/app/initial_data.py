#!/usr/bin/env python3

from app.db.session import get_db
from app.db.crud import create_user
from app.db.models import User
from app.db.schemas import UserCreate
from app.db.session import Base

from sqlalchemy import create_engine  # , Column, Integer, String, MetaData, Table
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "sqlite:///./db/database.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


def init() -> None:
    db = SessionLocal()
    first_name = "test-first_name"
    last_name = "test-last_name"
    email = "test-email"

    create_user(
        db,
        UserCreate(first_name=first_name, last_name=last_name, email=email),
    )
    db.commit()


if __name__ == "__main__":
    print("Creating user")
    init()
    print("Superuser created")

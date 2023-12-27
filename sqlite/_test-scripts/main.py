from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///database.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Create the table if it does not exist
Base.metadata.create_all(bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# def get_user(db: Session, fp_hash: int):
#     return user


def get_user(fp_hash: str):
    return get_user(db, fp_hash)


# def get_users(db: Session, skip: int = 0, limit: int = 100) -> t.List[schemas.UserOut]:
#     return db.query(models.Users).offset(skip).limit(limit).all()


def get_user_list():
    return get_users(db)


# def insert_entry(db: Session, entry: schemas.InsertEntry):
#     return new_entry


def put_entry(entry: dict):
    return insert_entry(db, entry)


# def create_user(db: Session, user: schemas.UserCreate):
#     return db_user


def put_user(user: dict):
    return create_user(db, user)

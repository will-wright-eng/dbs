from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from .log import get_logger


logger = get_logger(__name__)

DATABASE_URL = "sqlite:///./database.db"

engine = create_engine(
    DATABASE_URL, echo=True, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# Dependency
def get_db():
    logger.debug("db = SessionLocal()")
    db = SessionLocal()
    try:
        logger.debug("yield db")
        yield db
    finally:
        logger.debug("db.close()")
        db.close()

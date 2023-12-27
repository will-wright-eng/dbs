import typing as t

# from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from . import models, schemas


def get_user(db: Session, fp_hash: int):
    user = db.query(models.Users).filter(models.UserBase.fp_hash == fp_hash).first()
    if not user:
        # raise HTTPException(status_code=404, detail="User not found")
        raise ValueError("user not found")
    return user


def get_users(db: Session, skip: int = 0, limit: int = 100) -> t.List[schemas.UserOut]:
    return db.query(models.Users).offset(skip).limit(limit).all()


def insert_entry(db: Session, entry: schemas.InsertEntry):
    new_entry = models.Entries(
        fp_hash=entry.fp_hash,
        roastery_name=entry.roastery_name,
        roastery_location=entry.roastery_location,
        cultivar_name=entry.cultivar_name,
        cultivar_origin=entry.cultivar_origin,
        farm_name=entry.farm_name,
        farm_region=entry.farm_region,
        farm_elevation=entry.farm_elevation,
        brand_name=entry.brand_name,
        grind_setting=entry.grind_setting,
        bean_weight=entry.bean_weight,
        water_temperature=entry.water_temperature,
        extraction_time=entry.extraction_time,
        extraction_weight=entry.extraction_weight,
        extraction_notes=entry.extraction_notes,
    )
    db.add(new_entry)
    db.commit()
    db.refresh(new_entry)
    return new_entry


def create_user(db: Session, user: schemas.UserCreate):
    print(user)
    db_user = models.Users(
        fp_hash=user.fp_hash,
        email=user.email,
        first_name=user.first_name,
        last_name=user.last_name,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

from sqlalchemy import Column, String, Boolean, Integer

from .session import Base


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    fp_hash = Column(String, unique=True)
    email = Column(String, unique=True)
    first_name = Column(String)
    last_name = Column(String)


class Entries(Base):
    __tablename__ = "entries"

    id = Column(Integer, primary_key=True, index=True)
    fp_hash = Column(String)
    roastery_name = Column(String)
    roastery_location = Column(String)
    cultivar_name = Column(String)
    cultivar_origin = Column(String)
    farm_name = Column(String)
    farm_region = Column(String)
    farm_elevation = Column(String)
    brand_name = Column(String)
    grind_setting = Column(String)
    bean_weight = Column(String)
    water_temperature = Column(String)
    extraction_time = Column(String)
    extraction_weight = Column(String)
    extraction_notes = Column(String)

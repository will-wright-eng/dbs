# sqlite prototyping

- [SQL (Relational) Databases - FastAPI](https://fastapi.tiangolo.com/tutorial/sql-databases/)

## objective

- prototyping system
- two tables: users & trasactions
- users
    - fingerprint hash
    - name
    - email
- entries
    - roastery name
    - roastery location
    - cultivar name
    - cultivar origin
    - farm name
    - farm region
    - farm elevation
    - brand name
    - grind setting
    - bean weight
    - water temperature
    - extraction time
    - extraction weight
    - extraction notes

## actions

- init
    - create db
    - create tables
    - test data insertion
    - migrate S3 data to sqlite db
- sync
    - move db to server
    - sync server with local
- analysis
    - get data
    - analyze
    - visualize
    - generate html tables

## db-api

- copy prototyping project
- removed frontend
- removed prostgresql

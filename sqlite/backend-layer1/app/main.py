from fastapi import FastAPI, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from . import models, schemas
from .database import get_db, engine
from .log import get_logger
from .crud import create_transaction, get_transaction, create_item

models.Base.metadata.create_all(bind=engine)
logger = get_logger(__name__)
app = FastAPI()


@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info(f"Request: {request.method} {request.url}")
    response = await call_next(request)
    logger.info(f"Response: {response.status_code}")
    return response


@app.get("/")
def read_root():
    return {"Hello": "world"}


@app.post("/transactions/", response_model=schemas.Transaction)
def post_transaction(
    transaction: schemas.TransactionCreate, db: Session = Depends(get_db)
):
    return create_transaction(db=db, transaction_data=transaction)


@app.get("/transactions/{transaction_id}", response_model=schemas.Transaction)
def read_transaction(transaction_id: int, db: Session = Depends(get_db)):
    db_transaction = get_transaction(db, transaction_id)
    if db_transaction is None:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return db_transaction


@app.post("/items/", response_model=schemas.Item)
def post_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return create_item(db=db, item_name=item.name)

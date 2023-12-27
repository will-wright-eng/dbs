from sqlalchemy.orm import Session

from .schemas import TransactionCreate
from .models import Transaction
from .log import get_logger

logger = get_logger(__name__)


def get_transaction(db: Session, transaction_id: int):
    return db.query(Transaction).filter(Transaction.id == transaction_id).first()


def create_transaction(db: Session, transaction_data):
    logger.info(str(transaction_data.dict()))
    try:
        transaction = Transaction(**transaction_data.dict())
        logger.debug("db.add()")
        db.add(transaction)
        logger.debug("db.commit()")
        db.commit()
        logger.debug("db.refresh()")
        db.refresh(transaction)
        logger.info(f"Transaction created: {transaction}")
        return transaction
    except Exception as e:
        logger.error(f"Error creating transaction: {e}", exc_info=True)
        db.rollback()
        raise


def create_item(db: Session, item_name: str):
    db_item = models.Item(name=item_name)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

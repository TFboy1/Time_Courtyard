from sqlalchemy.orm import Session
from ..models import card as models
from ..schemas import cardSchemas as schemas
from fastapi import HTTPException


# 获取所有卡片
def get_cards(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Card).offset(skip).limit(limit).all()

# 创建新卡片
def create_card(db: Session, card: schemas.CardCreate):
    db_card = models.Card(**card.dict())
    db.add(db_card)
    db.commit()
    db.refresh(db_card)
    return db_card

# 删除卡片
def delete_card(db: Session, card_id: int):
    db_card = db.query(models.Card).filter(models.Card.id == card_id).first()
    if db_card:
        db.delete(db_card)
        db.commit()
        return db_card
    else:
        raise HTTPException(status_code=404, detail="Card not found")

# 更新卡片
def update_card(db: Session, card_id: int, card: schemas.CardCreate):
    db_card = db.query(models.Card).filter(models.Card.id == card_id).first()
    if db_card:
        for key, value in card.dict().items():
            setattr(db_card, key, value)
        db.commit()
        db.refresh(db_card)
        return db_card
    else:
        raise HTTPException(status_code=404, detail="Card not found")

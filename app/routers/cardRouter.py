from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..modules.card_manager.models import card as models
from ..modules.card_manager.schemas import cardSchemas as schemas
from ..modules.card_manager.crud import cardDAO as crud
from ..dependencies.database import get_db  # 导入 get_db 函数

router = APIRouter()


# 获取所有卡片
@router.get("/cards/", response_model=List[schemas.CardResponse])  # 修改这里
def read_cards(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    cards = crud.get_cards(db=db, skip=skip, limit=limit)
    return cards


# 创建新卡片
@router.post("/cards/", response_model=schemas.CardResponse)  # 修改这里
def create_card(card: schemas.CardCreate, db: Session = Depends(get_db)):
    return crud.create_card(db=db, card=card)


# 删除卡片
@router.delete("/cards/{card_id}", response_model=schemas.CardResponse)  # 修改这里
def delete_card(card_id: int, db: Session = Depends(get_db)):
    return crud.delete_card(db=db, card_id=card_id)


# 更新卡片
@router.put("/cards/{card_id}", response_model=schemas.CardResponse)  # 修改这里
def update_card(card_id: int, card: schemas.CardCreate, db: Session = Depends(get_db)):
    return crud.update_card(db=db, card_id=card_id, card=card)

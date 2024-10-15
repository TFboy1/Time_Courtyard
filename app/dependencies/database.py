from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
# 数据库配置
DATABASE_URL = "sqlite:///./cards.db"

# 创建数据库引擎
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# 创建数据库会话工厂
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 创建基础模型
Base = declarative_base()

#
# class Card(Base):
#     __tablename__ = 'cards'
#
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, index=True)
#     attack = Column(Integer)
#     health = Column(Integer)
#     description = Column(String)
#     speed = Column(Float)
#     range = Column(Float)

# 创建数据库的初始化函数
def init_db():
    Base.metadata.create_all(bind=engine)

# 获取数据库会话的函数
def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

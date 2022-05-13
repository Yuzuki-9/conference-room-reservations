from typing import List
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from . import crud, models, schemas  # 同じディレクトリ
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)  # DBの作成

app = FastAPI()

# dbのSessionを獲得するための関数
# いろんな知識が必要→都度調べる
# ドキュメント「Dependencies with yield」
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# @app.get("/")
# async def index():
#     return {"message": "Success"}

# Read
# 取得したデータをレスポンス（返す）する
# データはschemas.pyのUserとか
# ユーザ一覧：複数人→Listになる
# resuponse_model：returnの値

# ユーザー一覧
@app.get("/users", response_model=List[schemas.User])
async def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users
# 流れ
# アクセスがあった
# 関数を起動
# パスに引数があったらパスパラメータ, 何も書いてなかったらクエリパラメータ, デフォルトの値が入っていたらそれが使われる

# 会議室一覧
@app.get("/rooms", response_model=List[schemas.Room])
async def read_rooms(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    rooms = crud.get_rooms(db, skip=skip, limit=limit)
    return rooms

@app.get("/bookings", response_model=List[schemas.Booking])
async def read_bookings(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    bookings = crud.get_bookings(db, skip=skip, limit=limit)
    return bookings

# Create
@app.post("/users")
async def users(users: User):
    return {"users": users}

@app.post("/bookings")
async def bookings(bookings: Booking):
    return {"bookings": bookings}

@app.post("/rooms")
async def rooms(rooms: Room):
    return {"rooms": rooms}
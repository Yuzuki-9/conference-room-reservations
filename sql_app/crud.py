from sqlalchemy.orm import Session
from . import models, schemas


# ユーザー一覧取得
def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

# 会議室一覧取得
def get_rooms(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Room).offset(skip).limit(limit).all()


# 予約一覧取得
def get_bookings(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Booking).offset(skip).limit(limit).all()


# db.query(models.User)：引数で入れたDBからUserテーブルを検索する
# offset：何件目のデータを取ってくるか→skipで指定→0→最初から取ってくる
# limit：取ってくるデータの最大数
# all：すべて取ってくる

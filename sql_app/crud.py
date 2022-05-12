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

# ----
# ユーザー登録
def create_user(db:Session, user: schemas.User):
    db_user = models.User(username=user.username)  # インスタンス化
    db.add(db_user)  # dbをcreate
    db.commit()  # dbに反映
    db.refresh(db_user)  # 変更を反映するために必要
    return db_user

# 会議室登録
def create_room(db:Session, room: schemas.Room):
    db_room = models.Room(room_name=room.room_name, capacity=room.capacity)
    db.add(db_room)  # dbをcreate
    db.commit()  # dbに反映
    db.refresh(db_room)  # 変更を反映するために必要
    return db_room

# 予約登録
def create_booking(db:Session, booking: schemas.Booking):
    db_booking = models.Booking(
        user_id = booking.user_id,
        room_id = booking.room_id,
        booked_num = booking.booked_num,
        start_dataetime = booking.start_datetime,
        end_dataetime = booking.end_datetime
    )
    db.add(db_booking)  # dbをcreate
    db.commit()  # dbに反映
    db.refresh(db_booking)  # 変更を反映するために必要
    return db_booking


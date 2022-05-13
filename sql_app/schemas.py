"""FastAPI側のデータ構造について記述"""
import datetime
from pydantic import BaseModel, Field

class BookingCreate(BaseModel):
    user_id: int
    room_id: int
    booked_num: int
    start_datetime: datetime.datetime
    end_datetime: datetime.datetime

class Booking(BookingCreate):
    booking_id: int

    # pydanticのモデルは辞書型で入ってくるが、ormマッパーのモデルが入ってきても良い設定
    class Config:
        orm_mode = True


# ユーザー作成のデータ構造（idは自動生成されるためjsonにはいらない）
class UserCreate(BaseModel):
    username: str = Field(max_length=12)

# ユーザー全体の情報では、UserCreateを継承する→usernameは入っている
class User(UserCreate):
    user_id: int

    class Config:
        orm_mode = True


class RoomCreate(BaseModel):
    room_name: str = Field(max_length=12)
    capacity: int

class Room(RoomCreate):
    room_id: int

    class Config:
        orm_mode = True
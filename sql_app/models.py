from enum import unique
from textwrap import indent
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from .database import Base

class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True, index=True)  # index→検索を早くする仕組み
    username = Column(String, unique=True, index=True)  # ユーザ名は一意の値

class Room(Base):
    __tablename__ = 'rooms'
    room_id = Column(Integer, primary_key=True, index=True)  # index→検索を早くする仕組み
    room_name = Column(String, unique=True, index=True)  # ユーザ名は一意の値
    capacity = Column(Integer)

class Booking(Base):
    __tablename__ = 'bookings'
    booking_id = Column(Integer, primary_key=True, index=True)  # index→検索を早くする仕組み
    user_id = Column(Integer, ForeignKey('users.user_id', ondelete='SET NULL'), nullable=False)  # ondelete='SET NULL'：外部キーが削除されたらNULLにする
    room_id = Column(Integer, ForeignKey('rooms.room_id', ondelete='SET NULL'), nullable=False)  # nullable=False：NULL許容しない
    booked_num = Column(Integer)
    start_dataetime = Column(DateTime, nullable=False)
    end_dataetime = Column(DateTime, nullable=False)


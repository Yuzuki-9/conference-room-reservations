# データベースの共通した基本設定の記述

from requests import session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# データベースファイルの定義
SQLALCHEMY_DATABASE_URL = 'sqlite:///./sql_app.db'

# crud操作の基盤を作成
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False}
)

# データベースを接続して切断する一連の流れ（セッション）
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


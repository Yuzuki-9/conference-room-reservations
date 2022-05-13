import streamlit as st
import datetime
import random
import requests
import json

# streamlitは1画面しか表示できないから、サイドバーで切り替える
page = st.sidebar.selectbox('Choose your page', ['users', 'rooms', 'bookings'])

# ユーザー画面
if page == 'users':
    st.title('ユーザー登録画面')

    # formの中身にどういう項目を入れるのか→withの中身で指定する
    with st.form(key='user'):  # keyはformとの紐付け
        # user_id: int = random.randint(0, 10)  # user_idは登録したタイミングで決める
        username: str = st.text_input('ユーザ名', max_chars=12)  # , max12文字
        # userのpostで必要なデータを送ってあげる
        data = {
            # 'user_id': user_id,
            'username': username
        }
        submit_button = st.form_submit_button(label='ユーザー登録')  # formに紐づく送信ボタン

    # submit_buttonが押されたとき（リクエスト送信されたとき）
    if submit_button:
        url = 'http://127.0.0.1:8000/users'
        res = requests.post(
            url,
            data=json.dumps(data)
        )
        if res.status_code == 200:
            st.success('ユーザー登録完了')
        st.write(res.status_code)
        st.json(res.json())


# 会議室画面
elif page == 'rooms':
    st.title('会議室登録画面')

    # formの中身にどういう項目を入れるのか→withの中身で指定する
    with st.form(key='room'):  # keyはformとの紐付け
        # room_id: int = random.randint(0, 10)  # room_idは登録したタイミングで決める
        room_name: str = st.text_input('会議室名', max_chars=12)  # , max12文字
        capacity: int = st.number_input('定員', step=1)
        # roomのpostで必要なデータを送ってあげる
        data = {
            # 'room_id': room_id,
            'room_name': room_name,
            'capacity': capacity
        }
        submit_button = st.form_submit_button(label='会議室登録')  # formに紐づく送信ボタン

    # submit_buttonが押されたとき（リクエスト送信されたとき）
    if submit_button:
        url = 'http://127.0.0.1:8000/rooms'
        res = requests.post(
            url,
            data=json.dumps(data)
        )
        if res.status_code == 200:
            st.success('会議室登録完了')
        # st.write(res.status_code)
        st.json(res.json())


# 予約画面
elif page == 'bookings':
    st.title('APIテスト画面（予約）')

    # formの中身にどういう項目を入れるのか→withの中身で指定する
    with st.form(key='booking'):  # keyはformとの紐付け
        booking_id: int = random.randint(0, 10)
        user_id: int = random.randint(0, 10)
        room_id: int = random.randint(0, 10)
        booked_num: int = st.number_input('予約人数', step=1)
        date = st.date_input('日付: ', min_value=datetime.date.today())  # 今日以降の日付
        start_time = st.time_input('開始時刻: ', value=datetime.time(hour=9, minute=0))  # デフォルト9:00
        end_time = st.time_input('終了時刻: ', value=datetime.time(hour=20, minute=0))  # デフォルト20:00

        # formの中意味をそのまま
        data = {
            'booking_id': booking_id,
            'user_id': user_id,
            'room_id': room_id,
            'booked_num': booked_num,
            'start_datetime': datetime.datetime(
                year=date.year,
                month=date.month,
                day=date.day,
                hour=start_time.hour,
                minute=start_time.minute
            ).isoformat(),  # datetime型をisoformatに変換する
            'end_datetime': datetime.datetime(
                year=date.year,
                month=date.month,
                day=date.day,
                hour=end_time.hour,
                minute=end_time.minute
            ).isoformat(),
        }
        submit_button = st.form_submit_button(label='リクエスト送信')  # formに紐づく送信ボタン

    # submit_buttonが押されたとき（リクエスト送信されたとき）
    if submit_button:
        st.write('## 送信データ')
        st.json(data)
        st.write('## レスポンス結果')
        url = 'http://127.0.0.1:8000/bookings'
        res = requests.post(
            url,
            data=json.dumps(data)
        )
        st.write(res.status_code)
        st.json(res.json())

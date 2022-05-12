import streamlit as st
import random
import requests
import json

# streamlitは1画面しか表示できないから、サイドバーで切り替える
page = st.sidebar.selectbox('Choose your page', ['users', 'rooms'])

# ユーザー画面
if page == 'users':
    st.title('APIテスト画面（ユーザー）')

    # formの中身にどういう項目を入れるのか→withの中身で指定する
    with st.form(key='user'):  # keyはformとの紐付け
        user_id: int = random.randint(0, 10)  # user_idは登録したタイミングで決める
        username: str = st.text_input('ユーザ名', max_chars=12)  # , max12文字
        # userのpostで必要なデータを送ってあげる
        data = {
            'user_id': user_id,
            'username': username
        }
        submit_button = st.form_submit_button(label='リクエスト送信')  # formに紐づく送信ボタン

    # submit_buttonが押されたとき（リクエスト送信されたとき）
    if submit_button:
        st.write('## 送信データ')
        st.json(data)
        st.write('## レスポンス結果')
        url = 'http://127.0.0.1:8000/users'
        res = requests.post(
            url,
            data=json.dumps(data)
        )
        st.write(res.status_code)
        st.json(res.json())


# 会議室画面
elif page == 'rooms':
    st.title('APIテスト画面（会議室）')

    # formの中身にどういう項目を入れるのか→withの中身で指定する
    with st.form(key='room'):  # keyはformとの紐付け
        room_id: int = random.randint(0, 10)  # room_idは登録したタイミングで決める
        room_name: str = st.text_input('会議室名', max_chars=12)  # , max12文字
        capacity: int = st.number_input('定員', step=1)
        # roomのpostで必要なデータを送ってあげる
        data = {
            'room_id': room_id,
            'room_name': room_name,
            'capacity': capacity
        }
        submit_button = st.form_submit_button(label='リクエスト送信')  # formに紐づく送信ボタン

    # submit_buttonが押されたとき（リクエスト送信されたとき）
    if submit_button:
        st.write('## 送信データ')
        st.json(data)
        st.write('## レスポンス結果')
        url = 'http://127.0.0.1:8000/rooms'
        res = requests.post(
            url,
            data=json.dumps(data)
        )
        st.write(res.status_code)
        st.json(res.json())


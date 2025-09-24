import streamlit as st
import datetime

with st.form(key="profile_form"):

    #テキストボックス
    name=st.text_input("名前")
    adress=st.text_input("住所")
    # print(name,adress)

    #セレクトボックス
    # age_category=st.selectbox(
    #ラジオボタン
    age_category=st.radio(
        "年齢層",
        ("こども(18才未満)","大人(18才以上)"))

    #複数選択
    hobby=st.multiselect(
        "趣味",
        ("スポーツ","読書","プログラミング","アニメ・映画","釣り","料理",))
    
    #スライダー
    height=st.slider("身長",min_value=110,max_value=210)

    #日付
    start_date=st.date_input(
        "開始日",
        datetime.date(2025,9,1))
    
    #カラーピッカー
    color=st.color_picker("テーマカラー","#E89ED7")

    #ボタン
    submit_btn=st.form_submit_button("送信")
    cancel_btn=st.form_submit_button("キャンセル")
    #print(f'submit_btn: {submit_btn}')
    #print(f'cancel_btn:{cancel_btn}')


if submit_btn:
    st.text(f'ようこそ♪{name}さん♪{adress}に書類を送りました♪')
    st.text(f'年齢層：{age_category}')
    st.text(f'趣味：{",".join(hobby)}')
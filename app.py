import streamlit as st
import pandas as pd
from pyairtable import Api
from hashlib import sha256

st.set_page_config(
    page_title="#твоеслово.фтт",
    page_icon="images/ftt-logo.png",
    layout="centered",
    initial_sidebar_state="collapsed",
    menu_items={}
)

hide_decoration_bar_style = '''
    <style>
        header {visibility: hidden;}
        footer {visibility: hidden;}
    </style>
'''
st.markdown(hide_decoration_bar_style, unsafe_allow_html=True)
st.title('#твоеслово.фтт')

st.markdown('Расскажи что-нибудь')
with st.spinner('Отправляем ответ...'):
    with st.form('form'):
        txt_input = st.text_area(label='.', placeholder='Нажми и печатай', 
                                label_visibility='collapsed', height=200)
        submitted = st.form_submit_button("Поделиться")
        if submitted and txt_input:
            api = Api(st.secrets.pyairtable.api_key)
            table = api.table(st.secrets.pyairtable.base_id, 
                              st.secrets.pyairtable.table_id)
            date = str(pd.to_datetime('today'))
            m = sha256()
            h = m.update((date + txt_input).encode())
            table.create({'id': m.hexdigest(), 'date': date, 'text': txt_input})
            st.success('Отправлено!')
        elif submitted and not txt_input:
            st.error('Нужно что-нибудь написать!')
    
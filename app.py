import streamlit as st

st.set_page_config(
    page_title="Student Stories",
    page_icon="🤗",
    layout="centered",
    initial_sidebar_state="collapsed",
    menu_items={}
)

st.title('#твоеслово.фтт')

with st.form('form'):
    st.markdown('Расскажи что-нибудь')
    txt_input = st.text_area(label='.', placeholder='Нажми и печатай', 
                             label_visibility='collapsed')
    submitted = st.form_submit_button("Поделиться")
    if submitted and txt_input:
        st.success('Отправлено!')
    elif submitted and not txt_input:
        st.warning('Напишите чего-нибудь')
    
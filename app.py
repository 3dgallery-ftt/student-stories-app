import streamlit as st

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

with st.form('form'):
    st.markdown('Расскажи что-нибудь')
    txt_input = st.text_area(label='.', placeholder='Нажми и печатай', 
                             label_visibility='collapsed')
    submitted = st.form_submit_button("Поделиться")
    if submitted and txt_input:
        st.success('Отправлено!')
    elif submitted and not txt_input:
        st.error('Нужно что-нибудь написать!')
    
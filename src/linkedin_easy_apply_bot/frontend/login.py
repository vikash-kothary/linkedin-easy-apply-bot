import streamlit as st
import logging

from linkedin_easy_apply_bot import easyapplybot
from linkedin_easy_apply_bot.backend import config
from linkedin_easy_apply_bot.backend.utils import yaml_utils

# Suppress selenium debug logs
logging.getLogger('selenium').setLevel(logging.INFO)

st.set_page_config(
    page_title='LinkedIn Easy Apply Bot',
    initial_sidebar_state="collapsed"
)

st.title("LinkedIn Easy Apply Bot")

@st.cache_data
def on_startup():
    st.session_state = yaml_utils.read_file('src/config.yaml')
    
@st.cache_resource
def on_login():
    easyapplybot.EasyApplyBot(
        username=st.session_state['username'],
        password=st.session_state['password']
    )
    print('TODO: Login')

on_startup()

with st.form(key="my_form"):
    st.session_state['username'] = st.text_input("Email", value=config.LINKEDIN_USERNAME)
    st.session_state['password'] = st.text_input("Password", type='password', value=config.LINKEDIN_PASSWORD)
    if st.form_submit_button("Login", on_click=on_login):
        st.switch_page('pages/profile.py')
        
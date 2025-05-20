import streamlit as st

st.title("Profile")

profile = { **st.session_state }
profile['password'] = 'REDACTED'
profile
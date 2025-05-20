import streamlit as st

from linkedin_easy_apply_bot.backend.utils import csv_utils

st.title("Question/Answers")

questions_df = csv_utils.read_file_as_dataframe('files/data/qa.csv')
questions_df
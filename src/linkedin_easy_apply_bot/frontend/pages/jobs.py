import streamlit as st

from linkedin_easy_apply_bot.backend.utils import csv_utils

st.title("Jobs")

jobs_df = csv_utils.read_file_as_dataframe('files/data/out.csv')
jobs_df.loc[-1] = jobs_df.columns
jobs_df.index = jobs_df.index + 1
jobs_df = jobs_df.sort_index() 
jobs_df.columns = ["created_at", "job_id", "name", "company", "has_attempted", "has_succeeded"]
jobs_df
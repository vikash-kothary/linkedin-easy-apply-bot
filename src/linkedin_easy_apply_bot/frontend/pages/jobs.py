import streamlit as st
import pandas as pd


from linkedin_easy_apply_bot.backend.repos import jobs_repo

st.title("Jobs")

jobs_df = pd.DataFrame(jobs_repo.get_job_ids())
# jobs_df.loc[-1] = jobs_df.columns
# jobs_df.index = jobs_df.index + 1
# jobs_df = jobs_df.sort_index()
# jobs_df.columns = [
#     "created_at",
#     "job_id",
#     "name",
#     "company",
#     "has_attempted",
#     "has_succeeded",
# ]
jobs_df

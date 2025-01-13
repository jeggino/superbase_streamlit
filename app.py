import streamlit as st
from supabase import create_client, Client

import pandas as pd

# Initialize connection.
# Uses st.cache_resource to only run once.
def init_connection():
    url = st.secrets["SUPABASE_URL"]
    key = st.secrets["SUPABASE_KEY"]
    return create_client(url, key)

supabase = init_connection()

# Perform query.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
def run_query():
    return supabase.table("df").select("*").execute()
    
df_raw = run_query()
df_raw.keys()
# df_raw = pd.DataFrame(run_query()['data'])
# df_raw

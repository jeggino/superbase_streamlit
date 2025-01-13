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
    return supabase.table("df_observations").select("*").execute()

rows = run_query()

df_raw = pd.DataFrame(rows.data)
df_raw

if st.button('insert'):
    response = (
        supabase.table("df_observations")
        .insert({"key": 654654, "waarnemer": "pasquale"})
        .execute()
    )

if st.button('update'):
    response = (
        supabase.table("df_observations")
        .update({"waarnemer": "Antonio"})
        .eq("key", 654654)
        .execute()
    )

if st.button('delete'):
    response = (
        supabase.table("df_observations")
        .delete()
        .eq("key", 654654)
        .execute()
    )




import streamlit as st
from st_supabase_connection import SupabaseConnection

# Initialize connection.
conn = st.connection("supabase",type=SupabaseConnection)

# Perform query.
rows = conn.query("*", table="df", ttl="10m").execute()

# Perform query.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
def run_query():
    return supabase.table("df").select("*").execute()
    
rows = run_query()

# Print results.
for row in rows.data:
    st.write(f"{row['waarnemer']} has a :{row['soort']} found ({row['datum']}):")

import streamlit as st
import pandas as pd

# YOUR DATA – keep it, it's good
data = [... keep your list... ] # your 40 funders

df = pd.DataFrame(data, columns=["Funder","Occupation","Amount","Email","Status","Deadline","Link"])
df['Deadline'] = pd.to_datetime(df['Deadline'])

st.set_page_config(page_title="Grant Finder KE", layout="wide")
st.title("Grant Finder for Kenya – by Bright")
st.caption("Filter by your work: Education, Farming, Health, Tech, Creative, Climate")

search = st.text_input("What do you do?", placeholder="e.g. teacher, farmer, nurse, developer")
occupation = st.selectbox("Category", ["All", "Education", "Farming", "Health", "Tech", "Creative", "Climate"])

# Simple filter – works better than AI matching for now
filtered = df.copy()
if occupation!= "All":
    filtered = filtered[filtered['Occupation'] == occupation]

if search:
    s = search.lower()
    map_words = {"teacher":"Education","farmer":"Farming","doctor":"Health","nurse":"Health","developer":"Tech","artist":"Creative","climate":"Climate"}
    for k,v in map_words.items():
        if k in s:
            filtered = filtered[filtered['Occupation'] == v]

filtered = filtered.sort_values("Deadline")
st.success(f"Found {len(filtered)} funders")
st.dataframe(filtered, use_container_width=True, hide_index=True)

st.divider()
st.subheader("Quick Email Template")
if st.button("Generate email"):
    st.code(f"""Subject: Inquiry about {occupation} grants

Dear {filtered.iloc[0]['Funder'] if not filtered.empty else 'Grants Team'},

I am a {search or occupation} based in Kenya working in {occupation}.
I saw your program on {filtered.iloc[0]['Link'] if not filtered.empty else 'your site'} and would like to learn about current application windows.

Thank you,
Bright Muchui
Kangundo, Kenya
""")

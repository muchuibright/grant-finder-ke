import streamlit as st
import pandas as pd
import urllib.parse
import glob

st.set_page_config(page_title="Bright - 400 Global Funders", page_icon="🌍", layout="wide")
st.title("🌍 Bright - 400 Global Funders")
st.caption("Education | Farmers | Skills | Kenya | Africa | Global")

@st.cache_data
def load_data():
    csv_files = glob.glob("*.csv")
    if not csv_files:
        st.error("No CSV found in repo! Upload funders.csv")
        st.stop()
    # use first csv found
    return pd.read_csv(csv_files[0])

df = load_data()

query = st.text_input("🔍 Search 400 funders", placeholder="teacher, farmer, nursing, tech").lower()
region = st.selectbox("🌍 Region", ["All", "Kenya", "Africa", "Global"])
cats = ["All"]
if 'Category' in df.columns:
    cats += sorted(df['Category'].dropna().unique().tolist())
category = st.selectbox("📚 Category", cats)

filtered = df.copy()
if query:
    filtered = filtered[filtered.apply(lambda r: query in str(r).lower(), axis=1)]
if region!= "All" and 'Region' in filtered.columns:
    filtered = filtered[filtered['Region'].astype(str).str.contains(region, na=False)]
if category!= "All" and 'Category' in filtered.columns:
    filtered = filtered[filtered['Category'] == category]

st.success(f"✅ Found {len(filtered)} funders | File: {glob.glob('*.csv')[0]} | Total {len(df)}")

for i, row in filtered.head(50).iterrows():
    with st.expander(f"{row.iloc[0]}"):
        st.write(row.to_dict())
        c1, c2 = st.columns(2)
        term = urllib.parse.quote_plus(str(row.iloc[0]).split(' - ')[0])
        g_link = f"https://www.google.com/search?q={term}+grants+apply"
        with c1:
            if len(row) > 1 and str(row.iloc[1]).startswith("http"):
                st.link_button("✅ Apply", str(row.iloc[1]), use_container_width=True)
        with c2:
            st.link_button("🔎 Google", g_link, use_container_width=True)

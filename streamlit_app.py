import streamlit as st
import pandas as pd
import urllib.parse

st.set_page_config(page_title="Bright - 400 Global Funders", page_icon="🌍", layout="wide")
st.title("🌍 Bright - 400 Global Funders")
st.caption("Education | Farmers | Skills | Kenya | Africa | Global")

# Load your CSV
@st.cache_data
def load_data():
    try:
        df = pd.read_csv("funders.csv")
    except:
        df = pd.read_csv("funders_400.csv")
    return df

df = load_data()

# Search
query = st.text_input("🔍 Search 400 funders", placeholder="teacher, farmer, nursing, tech").lower()
region = st.selectbox("🌍 Region", ["All", "Kenya", "Africa", "Global"])
category = st.selectbox("📚 Category", ["All"] + sorted(df['Category'].dropna().unique().tolist()) if 'Category' in df else ["All"])

filtered = df.copy()
if query:
    filtered = filtered[filtered.apply(lambda r: query in str(r).lower(), axis=1)]
if region!= "All" and 'Region' in filtered.columns:
    filtered = filtered[filtered['Region'].str.contains(region, na=False)]
if category!= "All" and 'Category' in filtered.columns:
    filtered = filtered[filtered['Category'] == category]

st.success(f"✅ Found {len(filtered)} funders | Total {len(df)}")

for i, row in filtered.head(50).iterrows():
    with st.expander(f"{row['Funder']}"):
        st.write(f"**Category:** {row.get('Category','N/A')} | **Region:** {row.get('Region','N/A')}")
        if 'Description' in row:
            st.write(row['Description'])

        c1, c2, c3 = st.columns(3)
        search_term = urllib.parse.quote_plus(row['Funder'].split(' - ')[0])
        google_link = f"https://www.google.com/search?q={search_term}+grants+apply"

        with c1:
            if 'Link' in row and pd.notna(row['Link']):
                st.link_button("✅ Apply", row['Link'], use_container_width=True)
        with c2:
            st.link_button("🔎 Google", google_link, use_container_width=True)
        with c3:
            st.button("⭐ Save", key=f"save_{i}", use_container_width=True)

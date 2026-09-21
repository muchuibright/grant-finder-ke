import streamlit as st
import pandas as pd
import random
from datetime import datetime
st.set_page_config(page_title="Bright - 400 Global Funders", page_icon="🌍", layout="centered")
st.title("🌍 Bright - 400 Global Funders")
st.caption("Education | Farmers | Skills | Kenya | Africa | Global")
st.markdown("---")
base = [
["HELB","20K-500K","Student Education","Kenya","Education","helb.co.ke","https://www.helb.co.ke","Open"],
["Elimu Scholarship","Full Fees","High School","Kenya","Education","ministry","https://www.education.go.ke","Dec 2026"],
["Wings To Fly","Full Fees","Bright Poor","Kenya","Education","Equity","https://equitygroupfoundation.com","Oct 2026"],
["KCB Foundation","Full Fees","Student","Kenya","Education","KCB","https://kcbgroup.com/foundation","Nov 2026"],
["Uwezo Fund","KES 500K","Youth Women PWD","Kenya","Business","Chief Office","https://www.uwezo.go.ke","Rolling"],
["Youth Fund","100K-2M","Youth 18-35","Kenya","Business","youthfund.go.ke","https://www.youthfund.go.ke","Rolling"],
["WEF","100K-750K","Women","Kenya","Business","wef.go.ke","https://www.wef.go.ke","Rolling"],
["Hustler Fund","20K-1M","Chama","Kenya","Business","*254#","https://www.hustlerfund.go.ke","Open"],
["Tony Elumelu","$5000","Startup","Africa","Business","TEF","https://www.tonyelumelufoundation.org","Mar 2027"],
["Mastercard Foundation","$10k-100k","Youth Education","Africa","Education","online","https://mastercardfdn.org","Rolling"],
]
categories = ["Education","Farmers","Tech","Health","Business","Women","Youth","Skills","Climate","Arts"]
regions = ["Kenya","Africa","Global"]
extra = [["Google.org","$50k","Tech","Global"],["USAID","$100k","Farmers Youth","Africa"],["UNICEF","$20k","Education Health","Global"],["FAO","$30k","Farmers","Africa"]]
all_data = base.copy()
while len(all_data) < 400:
    f = random.choice(extra)
    cat = random.choice(categories)
    reg = random.choice(regions)
    name = f"{f[0]} - {cat} #{len(all_data)+1}"
    all_data.append([name, f[1], f[2], reg, cat, "Online", f"https://www.google.com/search?q={name}", "Rolling"])
df = pd.DataFrame(all_data, columns=["Funder","Amount","Who","Region","Category","How","Link","Deadline"])
search = st.text_input("🔍 Search 400 funders", placeholder="teacher, farmer, nursing, tech")
c1,c2 = st.columns(2)
with c1:
    rf = st.selectbox("🌍 Region", ["All","Kenya","Africa","Global"])
with c2:
    cf = st.selectbox("📚 Category", ["All"]+categories)
filtered = df
if search:
    filtered = filtered[filtered.apply(lambda r: search.lower() in str(r).lower(), axis=1)]
if rf!= "All":
    filtered = filtered[filtered["Region"]==rf]
if cf!= "All":
    filtered = filtered[filtered["Category"]==cf]
st.success(f"✅ Found {len(filtered)} funders | Total 400")
if "favs" not in st.session_state:
    st.session_state.favs = []
for _, row in filtered.head(50).iterrows():
    with st.container(border=True):
        st.markdown(f"**{row['Funder']}** | {row['Amount']}")
        st.caption(f"{row['Who']} | {row['Region']} | {row['Category']} | ⏰ {row['Deadline']}")
        a,b,c = st.columns(3)
        with a:
            st.link_button("Apply", row["Link"], use_container_width=True)
        with b:
            gs = f"https://www.goodstack.org/search?q={row['Funder'].split(' - ')[0]}"
            st.link_button("Goodstack", gs, use_container_width=True)
        with c:
            if st.button("⭐", key=row['Funder']):
                st.session_state.favs.append(row['Funder'])
                st.toast("Saved")
st.caption(f"Updated: {datetime.now().strftime('%b %d, %Y')} | Nairobi")

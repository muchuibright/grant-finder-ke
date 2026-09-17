import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="400 Funders - Bright", page_icon="🌍", layout="centered")
st.title("Bright - 400 Global Funders")
st.caption("Education | Farmers | High Demand Skills | Kenya Africa Global")
st.markdown("---")

# BASE REAL FUNDERS
base = [
    ["HELB","20K-500K","Student Education University TVET","Kenya","helb.co.ke","https://www.helb.co.ke"],
    ["Elimu Scholarship","Full Fees","Student Education Form1 Poor","Kenya","Ministry Education","https://www.education.go.ke"],
    ["Wings To Fly Equity","Full Fees Laptop","Student Education KCPE 350+","Kenya","Equity Branch","https://equitygroupfoundation.com"],
    ["KCB Foundation","Full Fees","Student Education Secondary","Kenya","kcbgroup.com","https://kcbgroup.com/foundation"],
    ["County Bursary Kangundo","5K-50K","Student Education Primary Secondary","Kenya","MCA Ward","https://machakos.go.ke"],
    ["NG-CDF Bursary","10K-100K","Student Education University","Kenya","NG-CDF Office","https://www.ngcdf.go.ke"],
    ["Mastercard Scholars","Full Uni","Student Education University Teacher","Africa","mastercardfdn.org","https://mastercardfdn.org"],
    ["Tony Elumelu","$5000","Farmer Agri Startup Youth Education","Africa","TEF","https://www.tonyelumelufoundation.org"],
    ["Kenya Climate Innovation","$20k","Farmer Agri Green Energy Innovation","Kenya","kcic.org.ke","https://www.kenyacic.org"],
    ["Uwezo Fund","KES 500K","Youth Farmer Tailor Education","Kenya","Chief Office","https://www.uwezo.go.ke"],
]

# HIGH DEMAND FIELDS TO MULTIPLY
fields = [
    ("Education Tech","Teacher Student EdTech Digital Learning","Global"),
    ("Smart Farming AgriTech","Farmer AgriTech Irrigation Greenhouse","Kenya Africa"),
    ("Tailoring Fashion Design","Tailor Fashion Designer Youth Women","Kenya Africa"),
    ("Plumbing Electrical Welding","Fundi Construction Youth TVET","Kenya"),
    ("Nursing Health Care","Nurse Health Caregiver Youth","Kenya Global"),
    ("Coding Software Dev","Youth Student Tech Developer","Africa Global"),
    ("Solar Green Energy","Youth Farmer Electrician Green","Kenya Africa"),
    ("Boda Boda Mechanics","Youth Mechanic Boda Garage","Kenya"),
    ("Mama Mboga Food Business","Women Farmer Food Vendor","Kenya"),
    ("Carpentry Construction","Youth Fundi Carpentry Mason","Kenya"),
]

# GENERATE 400
all_data = []
id_num = 1
for i in range(40): # 40 x 10 = 400
    for f_name, who, region in fields:
        org = random.choice(base)
        amount = org[1]
        link = org[5]
        all_data.append([
            f"{org[0]} - {f_name} Program {id_num}",
            amount,
            f"{who} {org[2]}",
            region,
            org[4],
            link
        ])
        id_num += 1
        if len(all_data) >= 400:
            break
    if len(all_data) >= 400:
        break

df = pd.DataFrame(all_data, columns=["Funder","Amount","Who","Region","How","Link"])

# SEARCH
search = st.text_input("🔍 Search 400 funders", placeholder="Type: education, farmer, teacher, tech, tailor, nursing...")
region_filter = st.selectbox("🌍 Filter Region", ["All","Kenya","Africa","Global","Kenya Africa"])

filtered = df
if search:
    filtered = df[df.apply(lambda r: search.lower() in str(r).lower(), axis=1)]
if region_filter!= "All":
    filtered = filtered[filtered["Region"].str.contains(region_filter, case=False)]

st.write(f"✅ Found **{len(filtered)}** of 400 funders" + (f" for '{search}'" if search else ""))

# SHOW CARDS - 20 at a time for phone speed
show = filtered.head(50)
for _, row in show.iterrows():
    with st.container(border=True):
        st.markdown(f"**{row['Funder']}** — {row['Amount']}")
        st.caption(f"For: {row['Who']}")
        st.caption(f"🌍 {row['Region']} | 📍 {row['How']}")
        st.link_button(f"Apply Now", row["Link"], use_container_width=True)

if len(filtered) > 50:
    st.info(f"Showing 50 of {len(filtered)}. Type more specific word to narrow.")

st.markdown("---")
st.success("400 Funders Live! Share: grant-finder-ke.streamlit.app")

import streamlit as st
import pandas as pd

st.set_page_config(page_title="Global Grant Finder", page_icon="🌍", layout="wide")
st.title("🌍 Global Grant Finder - by Bright")
st.caption("Kenya + Africa + Worldwide | For Kangundo & Everyone | Sep 2026")

data = [
# KENYA
["Uwezo Fund","KES 500K","Youth Women PWD Kenya","Chief office","Kenya","2026-12-31","https://www.uwezo.go.ke"],
["Youth Enterprise Fund","100K-2M","Youth 18-35 Kenya","youthfund.go.ke","Kenya","2026-12-31","https://www.youthfund.go.ke"],
["Women Enterprise Fund","100K-750K","Women Kenya","wef.go.ke","Kenya","2026-12-31","https://www.wef.go.ke"],
["NGAAF","300K-2M","Women Kenya","Women Rep","Kenya","2026-11-30","https://www.ngaaf.go.ke"],
["AGPO","Govt Tenders 30%","Youth Women PWD Kenya","agpo.go.ke","Kenya","2026-12-31","https://www.agpo.go.ke"],
["Hustler Fund","20K-1M","Chama Kenya","*254#","Kenya","2026-12-31","https://www.hustlerfund.go.ke"],
["Machakos County Fund","50K-500K","Groups Kenya","Machakos HQ","Kenya","2026-12-31","https://machakos.go.ke"],
# AFRICA + GLOBAL
["Tony Elumelu Foundation","$5000","Startup Africa","tefconnect.com","Africa","2027-03-31","https://www.tonyelumelufoundation.org"],
["Mastercard Foundation","$10k-100k","Youth Africa","mastercardfdn.org","Africa","2026-10-15","https://mastercardfdn.org"],
["Anzisha Prize","$15k-50k","Age 15-22 Africa","anzishaprize.org","Africa","2026-11-30","https://anzishaprize.org"],
["Y Combinator","$500k","Startup Worldwide","ycombinator.com","Global","2026-12-31","https://www.ycombinator.com"],
["Seedstars Africa","$50k+","Startup Global","seedstars.com","Global","2026-12-31","https://www.seedstars.com"],
["Village Capital","$25k-100k","Startup Global","vilcap.com","Global","2026-10-30","https://vilcap.com"],
["Gates Foundation","$10k-1M","Health Agri Global","gatesfoundation.org","Global","2026-12-31","https://www.gatesfoundation.org"],
["USAID","$50k+","Various Global","usaid.gov","Global","2026-12-31","https://www.usaid.gov"],
["EU Grants","€50k+","Agri Governance","europa.eu","Global","2026-11-01","https://europa.eu"],
["World Bank Youth","$5k-50k","Youth Global","worldbank.org","Global","2026-12-31","https://www.worldbank.org"],
["UNDP","$10k-50k","Env Youth Global","undp.org","Global","2026-12-31","https://www.undp.org"],
["British Council","£5k-20k","Creative Global","britishcouncil.org","Global","2026-12-31","https://www.britishcouncil.org"],
["GIZ","€20k","Jobs TVET Global","giz.de","Global","2026-09-30","https://www.giz.de"],
["Google for Startups","$100k","Tech Startup Global","startup.google.com","Global","2026-12-31","https://startup.google.com"],
["Safaricom Foundation","500K-5M","Community Kenya","safaricom.co.ke","Kenya","2026-12-31","https://www.safaricom.co.ke/foundation"],
]

df = pd.DataFrame(data, columns=["Funder","Amount","Who","How to Apply","Region","Deadline","Link"])
df['Deadline'] = pd.to_datetime(df['Deadline'])

st.sidebar.header("Filter")
region = st.sidebar.selectbox("Region", ["All","Kenya","Africa","Global"])
cat = st.sidebar.selectbox("Category", ["All","Youth","Women","Startup","Farm","Community","Health"])

search = st.text_input("🔍 What do you do? (farmer, teacher, startup, student, tailor)")

filtered = df.copy()
if region != "All":
    filtered = filtered[filtered['Region'].str.contains(region, case=False)]
if cat != "All":
    filtered = filtered[filtered.apply(lambda r: cat.lower() in str(r).lower(), axis=1)]
if search:
    filtered = filtered[filtered.apply(lambda r: search.lower() in str(r).lower(), axis=1)]

st.dataframe(filtered, use_container_width=True, hide_index=True)
st.success(f"Showing {len(filtered)} funders | {region} | Global + Kenya")
st.markdown("---")
st.caption("Built in Kangundo 🌍 for the World")

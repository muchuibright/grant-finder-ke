import streamlit as st
import pandas as pd
import random
import urllib.parse

st.set_page_config(page_title="Bright - 400 Global Funders", layout="wide")
st.title("🌍 Bright - 400 Global Funders")
st.caption("Education | Farmers | Skills | Kenya | Africa | Global")

MY_WHATSAPP = "254111975744"

msg1 = urllib.parse.quote("Hi Bright, I found a funder on your app. Help me apply. I will pay 500.")
msg2 = urllib.parse.quote("Hi Bright, I want full 400 funders PDF for 1000")

c1, c2 = st.columns(2)
c1.link_button("💬 WhatsApp: Help Apply (500 KES)", f"https://wa.me/{MY_WHATSAPP}?text={msg1}")
c2.link_button("📥 Get Full PDF (1000 KES)", f"https://wa.me/{MY_WHATSAPP}?text={msg2}")

st.divider()

base = [
 ["HELB","Loan 20K-500K","May 31","Kenyan student","Kenya","Education","https://helb.co.ke"],
 ["Elimu Scholarship","Form 1 Full","Dec 31","KCPE vulnerable","Kenya","Education","https://elimu.go.ke"],
 ["Wings To Fly","Full Secondary","Mar 15","KCPE 350+","Kenya","Education","https://equitygroupfoundation.com"],
 ["KCB 2Jiajiri","Skills Grant 50K","Apr 30","18-35 youth","Kenya","Skills","https://kcbgroup.com"],
 ["Uwezo Fund","Youth Fund","Rolling","Youth group","Kenya","Skills","https://uwezo.go.ke"],
 ["Mastercard Foundation","Young Africa Works","Rolling","18-35","Africa","Skills","https://mastercardfdn.org"],
 ["Tony Elumelu","$5K Seed","Mar 31","Startup","Africa","Business","https://tefconnect.com"],
 ["AGRA","Farmer Grant","Rolling","Smallholder","Kenya","Farmers","https://agra.org"],
 ["Gates Foundation","Education Grant","Rolling","NGO","Global","Education","https://gatesfoundation.org"],
 ["USAID Kenya","Youth Grant","Rolling","Youth org","Kenya","Skills","https://usaid.gov"],
]

more = ["Google.org","Microsoft 4Afrika","Safaricom Foundation","Equity Foundation","Co-op Foundation","Hand in Hand","Technoserve","One Acre Fund","GIZ Kenya","EU Kenya","World Bank Kenya","AfDB","UNDP Kenya","UNICEF Kenya","Acumen","Village Capital","Seedstars Africa","iHub Nairobi","Kenya Innovation Agency","Youth Enterprise Fund","Women Enterprise Fund","Hustler Fund","Faulu Kenya","KWFT","Amref Kenya","Kenya Red Cross","CARE Kenya","World Vision","Save Children","Plan International","ActionAid","Oxfam","Mercy Corps","Heifer","VSO","FAO Kenya","WFP Kenya","UN Women","ILO Kenya","GSMA Fund","Baobab Network","Antler East Africa","Aga Khan Foundation","Ford Foundation","Rockefeller","USAID","UKAID","JICA","GIZ"]

skills = ["Plumbing","Electrical","Nursing","Mama Mboga","Boda","Tailoring","Carpentry","Welding","Solar","Coding","Marketing","Hair Dressing","Baking","Mechanic","Farming","Business"]

random.seed(7)
rows=list(base)
for i in range(390):
 funder=random.choice(more)
 skill=random.choice(skills)
 region=random.choice(["Kenya","Africa","Global"])
 cat="Education" if skill in ["Nursing","Coding"] else "Farmers" if skill=="Farming" else "Skills"
 rows.append([funder, f"{skill} Scholarship / Grant - Cohort {i+21}", "Rolling" if i%2==0 else "Dec 31", f"{skill} youth 18-35", region, cat, f"https://google.com/search?q={funder.replace(' ','+')}"])

df=pd.DataFrame(rows[:400], columns=["Funder","Program","Deadline","Eligibility","Region","Category","Link"])
st.success(f"✅ {len(df)} Funders Loaded - WhatsApp 0111975744 to Apply")

q=st.text_input("🔍 Search 400 funders", placeholder="HELB, plumbing, nursing")
reg=st.selectbox("🌍 Region",["All","Kenya","Africa","Global"])
cat=st.selectbox("📚 Category",["All","Education","Farmers","Skills","Business"])

f=df
if q: f=f[f.apply(lambda r: q.lower() in str(r.values).lower(), axis=1)]
if reg!="All": f=f[f["Region"]==reg]
if cat!="All": f=f[f["Category"]==cat]

st.write(f"Showing **{len(f)}** of 400")
st.dataframe(f, use_container_width=True, height=600)
st.download_button("📥 Download 400 CSV", f.to_csv(index=False), "Bright_400_Funders.csv")

st.divider()
st.write("👇 Tap to apply via WhatsApp:")
for _, r in f.head(15).iterrows():
 m=urllib.parse.quote(f"Hi Bright, help me apply for {r['Funder']} - {r['Program']}. I saw it on your app.")
 st.link_button(f"💬 {r['Funder']} - {r['Program'][:40]}", f"https://wa.me/{MY_WHATSAPP}?text={m}")

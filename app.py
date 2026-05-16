import streamlit as st
import json
import os
from datetime import datetime

# 1. PAGE CONFIGURATION
st.set_page_config(
    page_title="SmartBet AI - Tanzania | Uhakika Odds 2 na Odds 5 za Leo",
    page_icon="🧠",
    layout="wide",  
    initial_sidebar_state="collapsed"
)

# Google SEO Headers
st.markdown(
    """
    <head>
        <meta name="keywords" content="SmartBet AI Tanzania, Uhakika odds 2 za leo, AI betting tips Swahili, Mikeka ya uhakika ya leo, Free football tips Tanzania">
        <meta name="description" content="Pata mikeka ya uhakika ya leo iliyochambuliwa kwa kutumia mfumo wa kisasa wa AI (SmartBet AI).">
    </head>
    """,
    unsafe_allow_html=True
)

# Pata tarehe ya leo kwa Kiswahili
miezi_swahili = {
    1: "Januari", 2: "Februari", 3: "Machi", 4: "Aprili", 5: "Mei", 6: "Juni",
    7: "Julai", 8: "Agosti", 9: "Septemba", 10: "Oktoba", 11: "Novemba", 12: "Desemba"
}
leo = datetime.now()
tarehe_ya_leo = f"{leo.day} {miezi_swahili[leo.month]}, {leo.year}"

# 2. ADVANCED CSS (Pamoja na mitindo ya vifungo vya Copy)
st.markdown("""
    <style>
    .stApp {
        background-color: #0d1117;
    }
    
    /* Button ya WhatsApp */
    .stButton>button {
        background: linear-gradient(45deg, #25D366, #128C7E);
        color: white;
        font-size: 20px;
        font-weight: bold;
        border-radius: 50px;
        width: 100%;
        padding: 16px;
        border: none;
        box-shadow: 0px 8px 20px rgba(37, 211, 102, 0.4);
        transition: all 0.3s ease-in-out;
    }
    .stButton>button:hover {
        transform: translateY(-4px);
        box-shadow: 0px 12px 25px rgba(37, 211, 102, 0.6);
        color: white;
    }
    
    /* Headers za Odds */
    .odds-header-2 {
        background: linear-gradient(135deg, #11998e, #38ef7d);
        color: white;
        padding: 20px;
        border-radius: 14px;
        text-align: center;
        font-size: 22px;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .odds-header-5 {
        background: linear-gradient(135deg, #ee0979, #ff6a00);
        color: white;
        padding: 20px;
        border-radius: 14px;
        text-align: center;
        font-size: 22px;
        font-weight: bold;
        margin-bottom: 20px;
    }
    
    /* Kadi za Mechi zenye Hover Animation */
    .match-card {
        background-color: #161b22;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.15);
        margin-bottom: 15px;
        border-left: 6px solid #38ef7d;
        color: #c9d1d9;
        transition: all 0.3s ease-in-out;
    }
    .match-card:hover {
        transform: translateX(8px);
        background-color: #1f242c;
        box-shadow: 0px 6px 20px rgba(56, 239, 125, 0.25);
    }
    
    .match-card-explosive {
        background-color: #161b22;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.15);
        margin-bottom: 15px;
        border-left: 6px solid #ff6a00;
        color: #c9d1d9;
        transition: all 0.3s ease-in-out;
    }
    .match-card-explosive:hover {
        transform: translateX(8px);
        background-color: #1f242c;
        box-shadow: 0px 6px 20px rgba(255, 106, 0, 0.25);
    }

    /* Mfumo wa Booking Code Box */
    .code-container {
        background-color: #0d1117;
        padding: 15px;
        border-radius: 8px;
        border: 1px dashed #30363d;
        text-align: center;
        margin-top: 15px;
    }
    .booking-code {
        font-size: 24px;
        font-family: 'Courier New', Courier, monospace;
        color: #58a6ff;
        font-weight: bold;
        letter-spacing: 2px;
    }
    .copy-btn {
        background-color: #21262d;
        color: #c9d1d9;
        border: 1px solid #30363d;
        padding: 6px 12px;
        border-radius: 6px;
        font-size: 14px;
        cursor: pointer;
        margin-top: 8px;
        transition: 0.2s;
    }
    .copy-btn:hover {
        background-color: #30363d;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# Function ya kutengeneza sanduku la Copy kwa JavaScript
def soko_la_copy(box_id, code_value):
    html_code = f"""
    <div class="code-container">
        <span class="booking-code" id="{box_id}">{code_value}</span><br>
        <button class="copy-btn" onclick="navigator.clipboard.writeText('{code_value}'); this.innerText='📋 Copied!'; setTimeout(() => this.innerText='📋 Copy Code', 2000)">📋 Copy Code</button>
    </div>
    """
    return html_code

# 3. DISPLAY BANNER
banner_path = os.path.join("assets", "banner.png")
if os.path.exists(banner_path):
    st.image(banner_path, use_container_width=True)
else:
    st.title("🤖 SMARTBET AI - TANZANIA")

# Sehemu ya Maelezo pamoja na TAREHE YA LEO YA KIOTOMATIKI
st.markdown(f"<h1 style='text-align: center; color: white; font-size: 28px; margin-top:20px;'>📆 Mikeka ya Uhakika ya Leo: {tarehe_ya_leo}</h1>", unsafe_allow_html=True)
st.markdown("""
<div style='text-align: center; font-size: 16px; color: #8b949e; margin-bottom: 35px;'>
    Hapa chini kuna machaguo yaliyochujwa na robot wetu wa AI kwa kuangalia takwimu, fomu, na majeraha ya timu ili kukupa ushindi mkubwa!
</div>
""", unsafe_allow_html=True)

# Sehemu ya kuweka kodi za kila siku (Weka kodi zako hapa kila asubuhi)
# -------------------------------------------------------------
KODI_YAKO_YA_ODDS2 = "BWTZ-67894-O2"  # <-- Badilisha hii tu kila siku asubuhi
KODI_YAKO_YA_ODDS5 = "BWTZ-12345-O5"  # <-- Badilisha hii tu kila siku asubuhi
# -------------------------------------------------------------

# 4. SOMA DATA KUTOKA TODAY_MATCHES.JSON
def load_matches():
    try:
        with open('today_matches.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

all_matches = load_matches()

if not all_matches:
    st.warning("⚠️ Data za leo bado zinatayarishwa na AI Robot wetu. Tafadhali run scraper yako kwanza!")
else:
    sorted_matches = sorted(all_matches, key=lambda x: float(x.get('Odds', 1.5)))
    
    slip_2 = []
    total_o2 = 1.0
    for m in sorted_matches:
        slip_2.append(m)
        total_o2 *= float(m.get('Odds', 1.0))
        if total_o2 >= 2.0:
            break

    slip_5 = []
    total_o5 = 1.0
    for m in sorted_matches:
        if m not in slip_2 or len(slip_2) <= 2:
            slip_5.append(m)
            total_o5 *= float(m.get('Odds', 1.0))
            if total_o5 >= 5.0:
                break
                
    if total_o5 < 5.0:
        for m in sorted_matches:
            if m not in slip_5:
                slip_5.append(m)
                total_o5 *= float(m.get('Odds', 1.0))
                if total_o5 >= 5.0:
                    break

    # Muundo wa Columns Mbili
    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown(f"<div class='odds-header-2'>🟢 MKEKA WA ODDS: {round(total_o2, 2)}+ [SAFE INVESTMENT]</div>", unsafe_allow_html=True)
        for m in slip_2:
            st.markdown(f"""
            <div class='match-card'>
                <span style='color: #8b949e; font-size: 13px;'>⏰ {m['Muda']} | 🏆 {m['Ligi']}</span><br>
                <b style='font-size: 19px; color: white;'>⚽ {m['Mechi']}</b><br>
                <span style='color: #38ef7d; font-weight: bold; font-size: 16px;'>🎯 UTABIRI: {m['Utabiri']}</span> 
                <span style='background-color: #21262d; color: #58a6ff; padding: 4px 10px; border-radius: 6px; float: right; font-weight: bold;'>@{m['Odds']}</span>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("<p style='color:white; font-weight:bold; margin-top:15px; margin-bottom:2px;'>📋 Copy Code na Ukabet Betway:</p>", unsafe_allow_html=True)
        st.components.v1.html(soko_la_copy("odds2", KODI_YAKO_YA_ODDS2), height=110)

    with col2:
        st.markdown(f"<div class='odds-header-5'>💣 MKEKA WA ODDS: {round(total_o5, 2)}+ [EXPLOSIVE BOOM]</div>", unsafe_allow_html=True)
        for m in slip_5:
            st.markdown(f"""
            <div class='match-card-explosive'>
                <span style='color: #8b949e; font-size: 13px;'>⏰ {m['Muda']} | 🏆 {m['Ligi']}</span><br>
                <b style='font-size: 19px; color: white;'>⚽ {m['Mechi']}</b><br>
                <span style='color: #ff6a00; font-weight: bold; font-size: 16px;'>🎯 UTABIRI: {m['Utabiri']}</span> 
                <span style='background-color: #21262d; color: #58a6ff; padding: 4px 10px; border-radius: 6px; float: right; font-weight: bold;'>@{m['Odds']}</span>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("<p style='color:white; font-weight:bold; margin-top:15px; margin-bottom:2px;'>📋 Copy Code na Ukabet Betway:</p>", unsafe_allow_html=True)
        st.components.v1.html(soko_la_copy("odds5", KODI_YAKO_YA_ODDS5), height=110)

# 5. WHATSAPP COMMUNITY CTA
st.markdown("<br><hr><br>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: white;'>🎁 Unahitaji Mechi za Live Updates au Uchambuzi Zaidi?</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #8b949e; font-size: 16px;'>Jiunge na kikundi chetu cha WhatsApp bure kupokea dondoo za ziada sekunde chache kabla ya mechi kuanza!</p>", unsafe_allow_html=True)

whatsapp_group_link = "https://chat.whatsapp.com/Kodi_Yako_Ya_Group_Hapa"

left_co, cent_co, last_co = st.columns([1,2,1])
with cent_co:
    st.link_button("🚀 JOIN OUR FREE WHATSAPP GROUP", whatsapp_group_link)

st.markdown("""
<div style='text-align: center; font-size: 12px; color: #8b949e; margin-top: 60px;'>
    © 2026 SmartBet AI - Tanzania. Haki zote zimehifadhiwa. 18+ | Bet kwa akili.
</div>
""", unsafe_allow_html=True)
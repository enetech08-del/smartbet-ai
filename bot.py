import json
import math

def load_scraped_data():
    """Soma data safi kutoka kwenye json file"""
    try:
        with open('today_matches.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print("[!] Faili la today_matches.json halijapatikana. Run scraper.py kwanza.")
        return []

def calculate_total_odds(matches):
    """Inapiga hesabu ya jumla ya odds kwa kuzizidisha zote pamoja"""
    total = 1.0
    for match in matches:
        try:
            total *= float(match['Odds'])
        except (ValueError, KeyError):
            continue
    return round(total, 2)

def generate_slips():
    all_matches = load_scraped_data()
    if not all_matches:
        return

    # Sura ya kwanza: Kupanga mechi kulingana na odds (kwa usalama)
    # Mechi zenye odds ndogo (salama zaidi) zitakaa juu, odds kubwa chini
    sorted_matches = sorted(all_matches, key=lambda x: float(x.get('Odds', 1.5)))

    slip_odds_2 = []
    slip_odds_5 = []

    # 1. Tengeneza Mkeka wa Odds 2 (Safe Slip)
    # Tunachukua mechi salama kabisa hadi tufikie au kuvuka odds 2.0
    for match in sorted_matches:
        slip_odds_2.append(match)
        if calculate_total_odds(slip_odds_2) >= 2.0:
            break

    # 2. Tengeneza Mkeka wa Odds 5 (Boom Slip/Ushawishi)
    # Tunachukua mechi kuanzia katikati/mwishoni ili kupata mlipuko wa Odds 5+
    current_odds_5_total = 1.0
    for match in sorted_matches:
        # Epuka kurudia mechi zote za odds 2 ili mikeka isifanane sana
        if match not in slip_odds_2 or len(slip_odds_2) <= 2:
            slip_odds_5.append(match)
            if calculate_total_odds(slip_odds_5) >= 5.0:
                break
            
    # Kama mechi hazikutosha kufika odds 5, ongeza kutoka zilizobaki
    if calculate_total_odds(slip_odds_5) < 5.0:
        for match in sorted_matches:
            if match not in slip_odds_5:
                slip_odds_5.append(match)
                if calculate_total_odds(slip_odds_5) >= 5.0:
                    break

    # Kutengeneza Ujumbe wa WhatsApp (The Marketing Message)
    message = "🔥 *SMARTBET AI - MKEKA WA LEO* 🔥\n"
    message += "📊 _Uchambuzi wa Juu Kutumia AI na Takwimu_\n\n"

    # Sehemu ya 1: MKKA WA ODDS 2 (INVESTMENT SLIP)
    total_odds_2 = calculate_total_odds(slip_odds_2)
    message += f"🟢 *MKEKA 01: ODDS {total_odds_2}+ (SALAMA - HIGH STAKE)* 🟢\n"
    message += "---------------------------------------\n"
    for m in slip_odds_2:
        message += f"⏰ {m['Muda']} | 🏆 {m['Ligi']}\n"
        message += f"⚽ *{m['Mechi']}*\n"
        message += f"🎯 Utabiri: *{m['Utabiri']}* (@{m['Odds']})\n\n"

    # Sehemu ya 2: MKEKA WA ODDS 5 (BOOM SLIP)
    total_odds_5 = calculate_total_odds(slip_odds_5)
    message += f"💣 *MKEKA 02: ODDS {total_odds_5}+ (MLIPUKO - MEDIUM STAKE)* 💣\n"
    message += "---------------------------------------\n"
    for m in slip_odds_5:
        message += f"⏰ {m['Muda']} | 🏆 {m['Ligi']}\n"
        message += f"⚽ *{m['Mechi']}*\n"
        message += f"🎯 Utabiri: *{m['Utabiri']}* (@{m['Odds']})\n\n"

    message += "⚠️ *ZINGATIA:* Weka dhamana unachoweza kupoteza. Betting ni uwekezaji wa akili, sio hisia! 🧠💰\n\n"
    message += "👉 _Kupata mikeka ya VIP kila siku, fungua website yetu au bofya link hapa chini!_"
    
    # Save the message to a file so it can be sent or viewed easily
    with open('whatsapp_msg.txt', 'w', encoding='utf-8') as f:
        f.write(message)
        
    print("\n================== WHATSAPP MESSAGE GENERATED ==================")
    print(message)
    print("================================================================")
    print("[SUCCESS] Ujumbe umetengenezwa na kuhifadhiwa kwenye 'whatsapp_msg.txt'")

if __name__ == "__main__":
    generate_slips()
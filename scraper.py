import time
import json
from playwright.sync_api import sync_playwright

try:
    from playwright_stealth import stealth_sync as stealth_func
except ImportError:
    try:
        from playwright_stealth import stealth_page as stealth_func
    except ImportError:
        stealth_func = None

def get_tips_from_web():
    all_tips = []
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
        )
        page = context.new_page()

        # Zuia picha pekee, acha CSS ili jedwali lisinyonyoke
        page.route("**/*.{png,jpg,jpeg,gif,svg}", lambda route: route.abort())
        
        if stealth_func:
            stealth_func(page)

        url = "https://tipsbet.co.uk"
        print(f"[*] Robot anafungua: {url}...")

        try:
            page.goto(url, wait_until="domcontentloaded", timeout=45000)
            print("[*] Page imefunguka. Tunatafuta jedwali la mechi...")
            time.sleep(6) 
            
            tables = page.locator("table").all()
            print(f"[*] Zimepatikana tables {len(tables)} kwa jumla.")

            for index, table in enumerate(tables):
                table_text = table.inner_text().upper()
                
                # Hakikisha hili ndilo jedwali halisi la mikeka
                if "TEAMS" in table_text and "TIP" in table_text:
                    print(f"[+] Jedwali la mechi limepatikana! (Table Index: {index})")
                    
                    rows = table.locator("tr").all()
                    print(f"[*] Zimepatikana safu {len(rows)} ndani ya jedwali hili.")

                    for row in rows:
                        # Tunachukua 'td' zote zilizopo NDANI ya mstari huu mahususi
                        cols = row.locator("td").all()
                        
                        # Kama safu zipo za kutosha, tunasoma kwa index zilizonyooka
                        if len(cols) >= 7:
                            match_time = cols[0].inner_text().strip()
                            country = cols[2].inner_text().strip() if len(cols) > 2 else ""
                            league = cols[4].inner_text().strip() if len(cols) > 4 else ""
                            teams = cols[5].inner_text().strip() if len(cols) > 5 else ""
                            prediction = cols[6].inner_text().strip() if len(cols) > 6 else ""
                            odds = cols[7].inner_text().strip() if len(cols) > 7 else "1.00"
                            
                            # Kusafisha kichwa cha habari cha jedwali
                            if "TEAMS" in teams.upper() or "TIME" in match_time.upper() or not teams:
                                continue
                            
                            # Validisha kama ni mstari wa mechi (Muda una ':')
                            if ":" in match_time and len(match_time) <= 5:
                                all_tips.append({
                                    "Muda": match_time,
                                    "Nchi": country,
                                    "Ligi": league,
                                    "Mechi": teams.replace(" - ", " vs "),
                                    "Utabiri": prediction,
                                    "Odds": odds,
                                    "Source": "Tipsbet.co.uk"
                                })
                                print(f"   [+] Imenaswa kwa Uhakika: {match_time} | Ligi: {league} | {teams} -> {prediction} (Odds: {odds})")
                    
                    # Toka baada ya kumaliza jedwali la kwanza la leo
                    break

        except Exception as e:
            print(f"[!] Hitilafu ya uchambuzi: {e}")
        
        finally:
            browser.close()
    
    return all_tips

def save_to_json(data):
    if data:
        with open('today_matches.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        print(f"\n[SUCCESS] Mechi {len(data)} zimehifadhiwa kwa Mpangilio Sahihi kwenye today_matches.json!")
    else:
        print("\n[!] Kushindwa kupanga safu. Data haijahifadhiwa.")

if __name__ == "__main__":
    print("--- SMARTBET AI V2: INDEX-ALIGNED SCRAPER ---")
    tips_data = get_tips_from_web()
    save_to_json(tips_data)
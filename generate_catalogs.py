#!/usr/bin/env python3
import json
import urllib.request
import urllib.parse
import os
import re

# Обов'язково вказуємо кастомний User-Agent для Radio-Browser API
USER_AGENT = "RadioCatalog-Generator/1.0 (https://github.com/radio-playlist)"

# Список країн для парсингу (ISO 2-letter codes)
TARGET_COUNTRIES = ["UA", "PL", "DE", "US", "GB", "FR", "IT", "ES", "CA"]

# Список популярних тегів/стилів
TARGET_TAGS = ["rock", "pop", "jazz", "classical", "ambient", "electronic", "news", "chillout", "metal", "retro"]

# Папка для збереження (зберігаємо прямо в корінь репозиторію)
OUTPUT_DIR = "."

def fetch_json(url):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req) as response:
            if response.status == 200:
                return json.loads(response.read().decode('utf-8'))
    except Exception as e:
        print(f"❌ Помилка завантаження {url}: {e}")
    return []

def clean_filename(name):
    return re.sub(r'[^a-zA-Z0-9_-]', '_', name.lower())

def convert_to_radiocatalog_format(stations):
    """Форматує станції під модель RadioStation у RadioCatalog"""
    formatted = []
    for s in stations:
        if not s.get("url_resolved") or not s.get("name"):
            continue
            
        station_obj = {
            "id": None,
            "source": "radio_browser_github",
            "stationuuid": s.get("stationuuid", ""),
            "name": s.get("name", "").strip(),
            "url": s.get("url", "").strip(),
            "url_resolved": s.get("url_resolved", "").strip(),
            "homepage": s.get("homepage", "").strip(),
            "favicon": s.get("favicon", "").strip(),
            "countrycode": s.get("countrycode", "").upper(),
            "state": s.get("state", "").strip(),
            "language": s.get("language", "").strip(),
            "tags": s.get("tags", "").strip(),
            "codec": s.get("codec", "MP3").upper(),
            "bitrate": s.get("bitrate", 128),
            "votes": s.get("votes", 0),
            "clickcount": s.get("clickcount", 0)
        }
        formatted.append(station_obj)
    return formatted

def save_json(data, filepath):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def save_m3u(stations, filepath, playlist_title):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("#EXTM3U\n")
        f.write("#EXTENC:UTF-8\n")
        f.write(f"#PLAYLIST:{playlist_title}\n\n")
        
        for s in stations:
            name = s.get("name", "Unknown Station").replace("\n", " ")
            url = s.get("url_resolved") or s.get("url")
            logo = s.get("favicon", "")
            group = s.get("countrycode") or "Global"
            
            if url:
                f.write(f'#EXTINF:-1 tvg-logo="{logo}" group-title="{group}",{name}\n')
                f.write(f'{url}\n\n')

def process_category(category_type, value, api_url):
    print(f"🔍 Завантажуємо {category_type}: {value}...")
    raw_stations = fetch_json(api_url)
    
    if not raw_stations:
        print(f"⚠️ Даних немає для {value}")
        return

    formatted_stations = convert_to_radiocatalog_format(raw_stations)
    count = len(formatted_stations)
    print(f"✅ Знайдено {count} робочих станцій для {value}")

    filename_base = clean_filename(value)

    # Динамічно будуємо шляхи (наприклад: ./countries/json/ua.json)
    json_path = os.path.join(OUTPUT_DIR, category_type, "json", f"{filename_base}.json")
    m3u_path = os.path.join(OUTPUT_DIR, category_type, "m3u", f"{filename_base}.m3u")

    # Збереження
    save_json(formatted_stations, json_path)
    save_m3u(formatted_stations, m3u_path, f"RadioCatalog - {value.upper()}")

def process_top200_without_ru(api_url):
    print("🔍 Завантажуємо Global Top 200 (з фільтрацією)...")
    raw_stations = fetch_json(api_url)
    
    if not raw_stations:
        print("⚠️ Даних немає для Top 200")
        return

    filtered_raw = []
    for s in raw_stations:
        country_code = (s.get("countrycode") or "").upper()
        country_name = (s.get("country") or "").lower()
        
        # Пропускаємо всі станції з Росії
        if country_code == "RU" or "russia" in country_name:
            continue
            
        filtered_raw.append(s)
        
        # Зупиняємося, коли зібрали чистих 200 станцій
        if len(filtered_raw) == 200:
            break

    formatted_stations = convert_to_radiocatalog_format(filtered_raw)
    print(f"✅ Згенеровано Top 200 без RU (відфільтровано {len(raw_stations) - len(filtered_raw)} станцій)")

    json_path = os.path.join(OUTPUT_DIR, "global", "json", "top200.json")
    m3u_path = os.path.join(OUTPUT_DIR, "global", "m3u", "top200.m3u")

    save_json(formatted_stations, json_path)
    save_m3u(formatted_stations, m3u_path, "RadioCatalog - GLOBAL TOP 200")

def main():
    print("🚀 Старт генерації каталогів для GitHub...\n")

    # 1. Обробка країн
    for country in TARGET_COUNTRIES:
        url = f"https://de1.api.radio-browser.info/json/stations/bycountrycodeexact/{country.lower()}?hidebroken=true&order=votes&reverse=true&limit=100"
        process_category("countries", country, url)

    # 2. Обробка жанрів / тегів
    for tag in TARGET_TAGS:
        tag_encoded = urllib.parse.quote(tag)
        url = f"https://de1.api.radio-browser.info/json/stations/bytagexact/{tag_encoded}?hidebroken=true&order=votes&reverse=true&limit=100"
        process_category("genres", tag, url)

    # 3. Генерація світового топу (Запитуємо 300, щоб після відсіювання RU було рівно 200)
    top_url = "https://de1.api.radio-browser.info/json/stations?hidebroken=true&order=votes&reverse=true&limit=300"
    process_top200_without_ru(top_url)

    print(f"\n🎉 Готово! Усі файли збережено.")
    
if __name__ == "__main__":
    main()

# 📻 RadioCatalog Community Sources

Welcome to the community-driven repository of curated open internet radio sources, available in both **JSON** (optimized for the **RadioCatalog** iOS/macOS app) and standard **M3U/M3U8** formats.

These stream lists are automatically compiled and verified from open-source databases to ensure broken links are filtered out.

---

### ⚡️ Quick Import to RadioCatalog App

If you are using **RadioCatalog** on iOS, iPadOS, or macOS, tap any of the quick-import links below directly from your Apple device to sync the playlist instantly:

#### 🌐 Global Selection
- 🌟 **Global Top 200**: [⚡️ Quick Add to App](radiocatalog://add-source?url=https%3A%2F%2Fradio-playlist.github.io%2FRadioCatalog-Sources%2Fglobal%2Fjson%2Ftop200.json&name=Top200) | [Raw JSON](https://radio-playlist.github.io/RadioCatalog-Sources/global/json/top200.json) | [M3U File](https://radio-playlist.github.io/RadioCatalog-Sources/global/m3u/top200.m3u)

#### 🌍 By Country (JSON)
- 🇺🇦 **Ukraine**: [⚡️ Quick Add to App](radiocatalog://add-source?url=https%3A%2F%2Fradio-playlist.github.io%2FRadioCatalog-Sources%2Fcountries%2Fjson%2Fua.json&name=Ukraine) | [Raw JSON](https://radio-playlist.github.io/RadioCatalog-Sources/countries/json/ua.json) | [M3U File](https://radio-playlist.github.io/RadioCatalog-Sources/countries/m3u/ua.m3u)
- 🇵🇱 **Poland**: [⚡️ Quick Add to App](radiocatalog://add-source?url=https%3A%2F%2Fradio-playlist.github.io%2FRadioCatalog-Sources%2Fcountries%2Fjson%2Fpl.json&name=Poland) | [Raw JSON](https://radio-playlist.github.io/RadioCatalog-Sources/countries/json/pl.json) | [M3U File](https://radio-playlist.github.io/RadioCatalog-Sources/countries/m3u/pl.m3u)
- 🇩🇪 **Germany**: [⚡️ Quick Add to App](radiocatalog://add-source?url=https%3A%2F%2Fradio-playlist.github.io%2FRadioCatalog-Sources%2Fcountries%2Fjson%2Fde.json&name=Germany) | [Raw JSON](https://radio-playlist.github.io/RadioCatalog-Sources/countries/json/de.json) | [M3U File](https://radio-playlist.github.io/RadioCatalog-Sources/countries/m3u/de.m3u)
- 🇺🇸 **United States**: [⚡️ Quick Add to App](radiocatalog://add-source?url=https%3A%2F%2Fradio-playlist.github.io%2FRadioCatalog-Sources%2Fcountries%2Fjson%2Fus.json&name=USA) | [Raw JSON](https://radio-playlist.github.io/RadioCatalog-Sources/countries/json/us.json) | [M3U File](https://radio-playlist.github.io/RadioCatalog-Sources/countries/m3u/us.m3u)
- 🇬🇧 **United Kingdom**: [⚡️ Quick Add to App](radiocatalog://add-source?url=https%3A%2F%2Fradio-playlist.github.io%2FRadioCatalog-Sources%2Fcountries%2Fjson%2Fgb.json&name=UK) | [Raw JSON](https://radio-playlist.github.io/RadioCatalog-Sources/countries/json/gb.json) | [M3U File](https://radio-playlist.github.io/RadioCatalog-Sources/countries/m3u/gb.m3u)

#### 🎵 By Music Genre (JSON)
- 🎸 **Rock**: [⚡️ Quick Add to App](radiocatalog://add-source?url=https%3A%2F%2Fradio-playlist.github.io%2FRadioCatalog-Sources%2Fgenres%2Fjson%2Frock.json&name=Rock) | [Raw JSON](https://radio-playlist.github.io/RadioCatalog-Sources/genres/json/rock.json) | [M3U File](https://radio-playlist.github.io/RadioCatalog-Sources/genres/m3u/rock.m3u)
- 🎷 **Jazz**: [⚡️ Quick Add to App](radiocatalog://add-source?url=https%3A%2F%2Fradio-playlist.github.io%2FRadioCatalog-Sources%2Fgenres%2Fjson%2Fjazz.json&name=Jazz) | [Raw JSON](https://radio-playlist.github.io/RadioCatalog-Sources/genres/json/jazz.json) | [M3U File](https://radio-playlist.github.io/RadioCatalog-Sources/genres/m3u/jazz.m3u)
- 🌌 **Ambient / Chillout**: [⚡️ Quick Add to App](radiocatalog://add-source?url=https%3A%2F%2Fradio-playlist.github.io%2FRadioCatalog-Sources%2Fgenres%2Fjson%2Fambient.json&name=Ambient) | [Raw JSON](https://radio-playlist.github.io/RadioCatalog-Sources/genres/json/ambient.json) | [M3U File](https://radio-playlist.github.io/RadioCatalog-Sources/genres/m3u/ambient.m3u)
- 🎻 **Classical**: [⚡️ Quick Add to App](radiocatalog://add-source?url=https%3A%2F%2Fradio-playlist.github.io%2FRadioCatalog-Sources%2Fgenres%2Fjson%2Fclassical.json&name=Classical) | [Raw JSON](https://radio-playlist.github.io/RadioCatalog-Sources/genres/json/classical.json) | [M3U File](https://radio-playlist.github.io/RadioCatalog-Sources/genres/m3u/classical.m3u)
- 📻 **News & Talk**: [⚡️ Quick Add to App](radiocatalog://add-source?url=https%3A%2F%2Fradio-playlist.github.io%2FRadioCatalog-Sources%2Fgenres%2Fjson%2Fnews.json&name=News) | [Raw JSON](https://radio-playlist.github.io/RadioCatalog-Sources/genres/json/news.json) | [M3U File](https://radio-playlist.github.io/RadioCatalog-Sources/genres/m3u/news.m3u)

---

### 📂 Directory Structure

```text
.
├── .github/
│   └── workflows/
│       └── update_catalogs.yml   # Automatic weekly updater workflow
├── countries/
│   ├── json/                      # JSON catalogs for RadioCatalog
│   └── m3u/                       # Standard M3U playlists
├── genres/
│   ├── json/
│   └── m3u/
├── global/
│   ├── json/                      # Top 200 worldwide streams
│   └── m3u/
├── generate_catalogs.py           # Python generator script
├── .gitignore
└── README.md

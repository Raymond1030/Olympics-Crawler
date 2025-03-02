<div align="center">
  <h1>Olympics Data Scraper🏆</h1> 
  <p align="center">
    🤗<a href="README.md">English</a> • 
    🤗 <a href="README-CN.md">中文</a> • 
  </p>
![奥运五环](https://upload.wikimedia.org/wikipedia/commons/5/5c/Olympic_rings_without_rims.svg)




This project scrapes historical Olympic Games data from [Olympics.com](https://olympics.com), including basic event information, sports disciplines, and detailed competition results. Supports both Chinese and English data extraction.

---

## File Descriptions

1. **GetOlympics_Name_Year.py**  
   - **Purpose**: Extracts Olympic Games names and years from predefined URLs, generates `olympic_games.csv`.  
   - **Output**: `Olympics_event/olympic_games.csv`

2. **GetSport.py**  
   - **Purpose**: Uses Selenium to scrape sports discipline lists for each Olympic Games, saves as `[Olympic-Game-Name]_events.csv`.  
   - **Output**: `Olympics_event/[Olympic-Game-Name]_events.csv`

3. **GetOlympics.py**  
   - **Purpose**: Scrapes detailed competition results (medals, athletes, countries) based on the sports list. Supports bilingual data.  
   - **Output Directories**:  
     - Chinese: `Olympics-result-zh/`  
     - English: `Olympics-result-en/`

---

## Dependencies

- Python 3.8+
- Required Libraries:
  ```bash
  pip install pandas beautifulsoup4 requests selenium openpyxl tqdm

- Browser Driver: [Microsoft Edge Driver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)
  (Must match your Edge browser version. Ensure the driver path is in the system environment variables.)

------

## Usage Instructions

### 1. Generate Olympic Games List

Run the script to generate basic Olympic Games info:

```
python GetOlympics_Name_Year.py
```

### 2. Scrape Sports Discipline List

Run the script to fetch sports disciplines for each Olympic Games:

```
python GetSport.py
```

**Note**: First-time execution requires manual browser login and cookie acceptance. Subsequent runs will auto-load user profiles.

### 3. Scrape Competition Results

- **For Chinese Data**:

  ```
  python GetOlympics.py
  ```

- **For English Data** (Uncomment `main_en()` in `GetOlympics.py`):

  ```
  # In GetOlympics.py, uncomment:
  # main_en()
  ```

  Then run:

  ```
  python GetOlympics.py
  ```

## Directory Structure

```
├── Olympics_event/                # Olympic Games metadata
│   ├── olympic_games.csv          # All Olympic Games names & years
│   └── [Olympic-Game-Name]_events.csv  # Sports disciplines per edition
│
├── Olympics-result-zh/            # Chinese results (by edition)
│   └── [Olympic-Game-Name]/
│       └── [Sport-Name].xlsx
│
├── Olympics-result-en/            # English results (same structure)
│
├── GetOlympics_Name_Year.py       # Script 1
├── GetSport.py                    # Script 2
└── GetOlympics.py                 # Script 3
```

------

## Important Notes

1. **Selenium Configuration**

   - Install Microsoft Edge and download the matching EdgeDriver version.

   - To modify the browser profile path, update in `GetSport.py`:

     ```
     options.add_argument("user-data-dir=/Your/Profile/Path")
     ```

2. **Network Stability**
   Some pages load slowly. Recommended to run in low-latency environments.

3. **Anti-Scraping Measures**
   If blocked frequently, adjust scroll parameters in `GetSport.py`:

   ```
   scroll_pause_time = 2   # Wait time after scrolling (seconds)
   total_scrolls = 5       # Number of scrolls
   ```

### Competition Result Excel File

| Sport    | Event           | Medal | Athlete Link  | Athlete Name | NOC  | Country       |
| :------- | :-------------- | :---- | :------------ | :----------- | :--- | :------------ |
| Swimming | Men's 100m Free | Gold  | /athletes/... | John Smith   | USA  | United States |

------

## License

Apache License 2.0
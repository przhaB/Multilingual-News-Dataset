# crawler/README.md

This folder contains the crawler scripts used to collect the multilingual news dataset.

## Files
- `crawler.py` — main crawler script (config-driven).
- `super_fixed_crawler.py` — site-specific fixes and utilities.
- `export_mysql_to_csv.py` — exports MySQL table `sim_news` to CSV.
- `README.md` — this file.

## Requirements
See repository root `requirements.txt`. Key packages:
- Python 3.8
- requests==2.26.0
- beautifulsoup4==4.11.1
- selenium==3.141.0
- mysql-connector-python
- python-dotenv
- lxml

## Setup

1. Create and activate virtual environment:
python3 -m venv venv
source venv/bin/activate
pip install -r ../requirements.txt


2. ChromeDriver (for Selenium):
- Install Chrome (or Chromium) and matching ChromeDriver.
- Place `chromedriver` on PATH or set `CHROMEDRIVER_PATH` environment variable.

3. Environment variables:
- Create `.env` in repository root with database credentials (DO NOT commit `.env`).
  ```
  MYSQL_HOST=localhost
  MYSQL_USER=youruser
  MYSQL_PASSWORD=yourpassword
  MYSQL_DB=yourdb
  ```

## Running the crawler

Example command (basic):
python crawler.py --config configs/site_configs.json --max-pages 50


- `--config` : path to site-specific configuration (listing URLs, selectors, selenium flag).
- `--max-pages`: per-site maximum pages to crawl (default set in config).
- The crawler stores results into MySQL table `sim_news`. Use `export_mysql_to_csv.py` to export.

## Export CSV
python export_mysql_to_csv.py --table sim_news --output ../dataset/dataset.csv --encoding utf8mb4


## Notes
- Default polite delays: 2s between requests, 3s between pages. These are configurable.
- Error handling is implemented via try/except blocks and logging; check logs for errors.
- Deduplication: SHA-256 of article URL (`url_hash`) enforced at ingestion.
- If a site blocks automated traffic, consider reducing crawl rate or contacting site administrators.

## Reproducibility
- See `README_EXTRA.md` for collection dates and selector notes.
- Include `requirements.txt` and ChromeDriver version for exact reproduction.

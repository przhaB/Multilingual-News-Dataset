# Multilingual-News-Dataset

Multilingual news dataset (English, Kurdish, Arabic) for academic news recommendation research.

## Overview

This repository contains a multilingual news dataset collected from public news pages of seven Kurdistan university websites. The dataset and accompanying crawler code are provided to support reproducible research in multilingual news recommendation and information retrieval.

- Total articles: 1,150  
  - English (en): 500  
  - Arabic (ar): 350  
  - Kurdish (ku): 300

Collection dates and per-site details are provided in `README_EXTRA.md` (collection_dates and per-site notes).

## Files in this repository

- `dataset/dataset.csv` — Full cleaned dataset (UTF-8 / utf8mb4 CSV).  
- `dataset/sample_small.csv` — Small sample for quick inspection.  
- `schema.txt` — Column descriptions and data types.  
- `crawler/`  
  - `crawler.py` — Primary crawler script.  
  - `super_fixed_crawler.py` — Site-specific crawler utilities / fixes.  
  - `export_mysql_to_csv.py` — Utility for exporting MySQL table to CSV.  
- `requirements.txt` — Minimal Python dependencies and versions.  
- `README.md` — This file.  
- `CITATION.cff` — Citation metadata for the dataset.  
- `LICENSE` — License file (CC BY 4.0).  
- `README_EXTRA.md` — Per-site collection dates, anonymization notes, and compliance details.

## Schema (summary)

See `schema.txt` for the full schema. Example columns:

- `id` — integer, primary key  
- `title` — string, article title  
- `content` — string, full article text (cleaned)  
- `link` — string, original article URL  
- `language` — string, language label: `en`, `ar`, or `ku`  
- `url_hash` — string, SHA-256 hash of `link` (deduplication key)  
- `source` — string, origin university/site identifier  
- `created_at` — datetime, ingestion timestamp

## Anonymization and Privacy

Personal identifiers (for example, names, emails, student numbers) were removed or replaced with irreversible hashes prior to public release. See `README_EXTRA.md` for the exact columns removed/hashed.

## Ethical and legal compliance

- Robots / TOS: We inspected each target site and respected `robots.txt` directives. Where site terms explicitly prohibited scraping, content was excluded; see `README_EXTRA.md` for per-site notes.  
- Rate limits and politeness: The crawler uses adjustable delays (default 2s between requests, 3s between pages) and per-site maximum page limits to reduce server load and minimize blocking.  
- Redistribution: If you plan to redistribute derived content, verify original publishers' terms.

## Reproducibility — how to run

1. Create a Python 3.8 virtual environment and install dependencies:
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt


2. Configure environment variables (example):
- Create a `.env` file with any required database credentials (do NOT commit `.env` to the repo).
- Example `.env`:
  ```
  MYSQL_HOST=localhost
  MYSQL_USER=youruser
  MYSQL_PASSWORD=yourpassword
  MYSQL_DB=yourdb
  ```

3. Run the crawler (example):
python crawler/crawler.py

- Note: some sites require Selenium (headless Chrome). Ensure ChromeDriver is installed and available on PATH.

4. Export MySQL table to CSV:
python crawler/export_mysql_to_csv.py --table sim_news --output dataset/dataset.csv


See `crawler/README.md` for site-specific selectors, configuration options, and command-line arguments.

## Requirements

See `requirements.txt` in repository root.

## Limitations

- Some sites required manual selector tuning; small site-specific gaps may exist.  
- Language detection is heuristic-based (character counts) and may misclassify noisy content.  
- The dataset represents the public news pages available at the time of collection and may not be exhaustive.

## License

This dataset and accompanying code are released under the Creative Commons Attribution 4.0 International (CC BY 4.0) license. See `LICENSE` for full details.

## Citation

If you use this dataset, please cite it as:

przhaB, “Multilingual university news dataset (English, Kurdish, Arabic) and crawler scripts,” GitHub repository, 2025. [Online]. Available: https://github.com/przhaB/Multilingual-News-Dataset. Accessed: 24 Aug. 2025.

See `CITATION.cff` for machine-readable citation metadata.

## Contact

For questions or issues, please open an issue on the repository or contact the dataset maintainer via the GitHub profile: https://github.com/przhaB

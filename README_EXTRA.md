# README_EXTRA

This file contains per-site collection dates, selector notes, anonymization logs, and compliance notes.

## Collection summary

- Collection period: [INSERT START DATE] — [INSERT END DATE]
- Total articles: 1,374 (en: 592; ar: 283; ku: 499)
- Repository: https://github.com/przhaB/Multilingual-News-Dataset
- Accessed: 24 Aug. 2025

## Per-site collection notes (example template)

Site: <site_name>
- Base URL: <site_base_url>
- Pages crawled: listing URLs and page range (e.g., /news?page=1..10)
- CSS selectors used (listing): `ul.news-list > li`, `.news-item`
- CSS selectors used (content): `.post-content`, `.entry-content`, `article p`
- Selenium required: Yes/No
- Collection dates: YYYY-MM-DD to YYYY-MM-DD
- Compliance notes: robots.txt allowed scraping / specific TOS considerations

(Repeat the above block for each of the seven sites. Fill exact values.)

## Anonymization log

- Columns removed or redacted from public dataset:
  - `author_email` (removed)
  - `student_id` (removed)
  - Any explicit personal identifiers found in article content were redacted or replaced with the token `[REDACTED]` where appropriate.
- Hashing:
  - `url_hash`: SHA-256(url) used for deduplication. This is irreversible for practical purposes.
- Notes:
  - No database credentials, .env files, or private keys are included in this repository.
  - If you discover additional personal data, please report by opening an issue.

## Ethical / legal compliance

- Robots/TOS: Each site was inspected for `robots.txt`. Sites disallowing scraping were excluded.
- Rate limiting: Default delays: 2s between requests; 3s between pages.
- Contact: For any dispute about content removal, contact the original site or open an issue in this repo.

## Reproducibility checklist

- `requirements.txt` is provided with minimal dependency versions.
- `crawler/` contains script names and example commands.
- `export_mysql_to_csv.py` exports `sim_news` table to CSV with `utf8mb4` encoding.
- For full re-run, ensure ChromeDriver is installed and matches your local Chrome version.

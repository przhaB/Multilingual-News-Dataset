#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Export sim_news table to CSV for public dataset release.
Only exports public fields (excludes internal experimental columns).
"""

import os
import mysql.connector
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

DATABASE_CONFIG = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'port': int(os.getenv('DB_PORT', 3306)),
    'user': os.getenv('DB_USER', 'root'),
    'password': os.getenv('DB_PASSWORD', ''),
    'database': os.getenv('DB_NAME', 'university_website'),
    'charset': 'utf8mb4'
}

def export_dataset():
    try:
        conn = mysql.connector.connect(**DATABASE_CONFIG)
        print("✓ Connected to database")
        
        query = """
        SELECT id, title, content, link, language, url_hash, source, created_at, updated_at
        FROM sim_news
        WHERE title IS NOT NULL AND title != ''
        ORDER BY id
        """
        
        df = pd.read_sql(query, conn)
        conn.close()
        
        output_file = "../Dataset.csv"
        df.to_csv(output_file, index=False, encoding="utf-8-sig")
        
        print(f"✅ Successfully exported {len(df)} records to {output_file}")
        print(f"   Languages: {df['language'].value_counts().to_dict()}")
        print(f"   Sources: {df['source'].value_counts().to_dict()}")
        
        sample_df = df.head(3)
        sample_df.to_csv("../sample_small.csv", index=False, encoding="utf-8-sig")
        print("✅ Created sample_small.csv (3 records)")
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    export_dataset()

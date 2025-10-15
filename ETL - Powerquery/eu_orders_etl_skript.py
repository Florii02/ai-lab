"""
Practice ETL Script — Day 3
EU-First / GDPR-Safe ETL with pandas

Steps:
1. Extract from CSV
2. Transform: Clean, standardize, enrich
3. Load: Save as clean CSV
"""

import pandas as pd
from pathlib import Path

def etl_pipeline():
    # -------------------
    # EXTRACT
    # -------------------
    print("📂 Extracting data...")
    try:
        script_dir = Path(__file__).parent
        csv_path = script_dir / "eu_orders.csv"
        df = pd.read_csv(csv_path)
    except FileNotFoundError:
        print("⚠️ No eu_orders.csv found. Please create the sample file first.")
        return

    print("Preview of raw data:")
    print(df.head(), "\n")

    # -------------------
    # TRANSFORM
    # -------------------
    print("🔄 Transforming data...")

    # Drop duplicates on OrderID
    df = df.drop_duplicates(subset=["OrderID"])

    # Remove rows missing critical info
    df = df.dropna(subset=["CustomerName", "Amount"])

    # Fill missing emails
    df["Email"] = df["Email"].fillna("noemail@example.com")

    # Standardize country codes to upper-case
    df["Country"] = df["Country"].str.upper()

    # Keep only selected EU countries
    eu_countries = ["DE", "FR", "IT", "ES", "NL"]
    df = df[df["Country"].isin(eu_countries)]

    # Convert Amount to numeric
    df["Amount"] = pd.to_numeric(df["Amount"], errors="coerce")

    # VAT Calculation (19%)
    df["AmountWithVAT"] = df["Amount"] * 1.19

    # Add HighValue flag if > 200
    df["HighValue"] = df["Amount"] > 200

    # Add processing timestamp
    df["ProcessedDate"] = pd.Timestamp.now()

    print("✅ Transformed data sample:")
    print(df.head(), "\n")

    # -------------------
    # LOAD
    # -------------------
    clean_csv = script_dir / "eu_orders_clean.csv"
    df.to_csv(clean_csv, index=False)
    print(f"📊 Clean data saved to {clean_csv} with {len(df)} records.")

if __name__ == "__main__":
    etl_pipeline()

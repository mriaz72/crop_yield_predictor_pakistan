# tests/test_fetch_weather.py
"""
Quick sanity check — fetches ONE district for ONE month.
Run this BEFORE running the full pipeline to verify everything works.

Usage:
    python tests/test_fetch_weather.py
"""

from src.data.fetch_weather import fetch_district_weather

def test_single_district():
    print("🧪 Testing weather fetch for Lahore (Jan 2023)...\n")

    df = fetch_district_weather(
        district="Lahore",
        lat=31.5497,
        lon=74.3436,
        start_date="2023-01-01",
        end_date="2023-01-31",
    )

    print(f"✅ Shape       : {df.shape}")
    print(f"   Columns    : {list(df.columns)}")
    print(f"   Date range : {df['date'].min().date()} → {df['date'].max().date()}")
    print(f"   Nulls      : {df.isnull().sum().sum()} total\n")
    print(df.to_string(index=False))


if __name__ == "__main__":
    test_single_district()
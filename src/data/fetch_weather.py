# src/data/fetch_weather.py
"""
Fetches daily historical weather data for all 36 Punjab districts
from the Open-Meteo Archive API (free, no API key required).

Output:
    data/raw/weather/<district_name>.parquet   (one file per district)
    data/raw/weather/all_districts.parquet     (combined file)

Usage:
    python -m src.data.fetch_weather
"""

import time
import requests
import pandas as pd
from pathlib import Path
from tqdm import tqdm

from src.data.districts import PUNJAB_DISTRICTS, START_DATE, END_DATE

# ── Config ────────────────────────────────────────────────────────────────────

BASE_URL = "https://archive-api.open-meteo.com/v1/archive"

WEATHER_VARIABLES = [
    "temperature_2m_max",       # Daily max temp (°C)  — heat stress
    "temperature_2m_min",       # Daily min temp (°C)  — frost risk
    "precipitation_sum",        # Daily rainfall (mm)  — water availability
    "et0_fao_evapotranspiration",  # Evapotranspiration  — crop water demand
    "shortwave_radiation_sum",  # Solar radiation (MJ/m²) — photosynthesis
    "windspeed_10m_max",        # Max wind speed (km/h) — evaporation risk
]

OUTPUT_DIR = Path("data/raw/weather")


# ── Core fetch function ───────────────────────────────────────────────────────

def fetch_district_weather(
    district: str,
    lat: float,
    lon: float,
    start_date: str = START_DATE,
    end_date: str = END_DATE,
    retries: int = 3,
) -> pd.DataFrame:
    """
    Fetch daily weather for a single district.
    Returns a DataFrame with one row per day.
    Retries up to `retries` times on failure.
    """
    params = {
        "latitude":  lat,
        "longitude": lon,
        "start_date": start_date,
        "end_date":   end_date,
        "daily":      ",".join(WEATHER_VARIABLES),
        "timezone":   "Asia/Karachi",
    }

    for attempt in range(1, retries + 1):
        try:
            response = requests.get(BASE_URL, params=params, timeout=60)
            response.raise_for_status()
            data = response.json()
            break
        except requests.RequestException as e:
            if attempt == retries:
                raise RuntimeError(
                    f"Failed to fetch {district} after {retries} attempts: {e}"
                )
            time.sleep(10 ** attempt)  # exponential backoff: 2s, 4s, 8s

    daily = data["daily"]
    df = pd.DataFrame({"date": pd.to_datetime(daily["time"])})

    for var in WEATHER_VARIABLES:
        df[var] = daily.get(var)

    df.insert(0, "district", district)
    df.insert(1, "latitude", lat)
    df.insert(2, "longitude", lon)

    return df


# ── Main pipeline ─────────────────────────────────────────────────────────────

def fetch_all_districts(
    start_date: str = START_DATE,
    end_date: str = END_DATE,
    save_individual: bool = True,
) -> pd.DataFrame:
    """
    Fetch weather for all 36 Punjab districts and save to Parquet files.

    Args:
        start_date: ISO date string e.g. "2000-01-01"
        end_date:   ISO date string e.g. "2024-12-31"
        save_individual: If True, also save one file per district

    Returns:
        Combined DataFrame for all districts
    """
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    all_frames = []
    failed = []

    for district, (lat, lon) in tqdm(
        PUNJAB_DISTRICTS.items(),
        desc="📡 Fetching weather",
        unit="district",
    ):
        # Skip if already fetched (resume support)
        district_file = OUTPUT_DIR / f"{district.replace(' ', '_')}.parquet"
        if district_file.exists():
            tqdm.write(f"  ⏭  {district} — already fetched, skipping")
            df = pd.read_parquet(district_file)
            all_frames.append(df)
            continue

        try:
            df = fetch_district_weather(district, lat, lon, start_date, end_date)

            if save_individual:
                df.to_parquet(district_file, index=False)
                tqdm.write(f"  ✅ {district} — {len(df):,} days saved")

            all_frames.append(df)
            time.sleep(5)  # be polite to the API

        except RuntimeError as e:
            tqdm.write(f"  ❌ {e}")
            failed.append(district)

    # Combine and save
    if all_frames:
        combined = pd.concat(all_frames, ignore_index=True)
        combined_path = OUTPUT_DIR / "all_districts.parquet"
        combined.to_parquet(combined_path, index=False)
        print(f"\n📦 Combined file saved → {combined_path}")
        print(f"   Shape : {combined.shape[0]:,} rows × {combined.shape[1]} columns")
        print(f"   Districts: {combined['district'].nunique()} / {len(PUNJAB_DISTRICTS)}")
    else:
        combined = pd.DataFrame()

    if failed:
        print(f"\n⚠️  Failed districts ({len(failed)}): {', '.join(failed)}")
        print("   Re-run the script to retry — completed districts will be skipped.")

    return combined


# ── Quick data preview ────────────────────────────────────────────────────────

def preview(n_rows: int = 5) -> None:
    """Print a quick preview of the combined weather file."""
    path = OUTPUT_DIR / "all_districts.parquet"
    if not path.exists():
        print("No combined file found. Run fetch_all_districts() first.")
        return

    df = pd.read_parquet(path)
    print("\n── Sample rows ──────────────────────────────")
    print(df.head(n_rows).to_string(index=False))
    print("\n── Missing values ───────────────────────────")
    print(df.isnull().sum())
    print("\n── Date range ───────────────────────────────")
    print(f"  From : {df['date'].min().date()}")
    print(f"  To   : {df['date'].max().date()}")


# ── Entry point ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("🌾 CropYield Predictor — Weather Ingestion")
    print(f"   Districts : {len(PUNJAB_DISTRICTS)}")
    print(f"   Period    : {START_DATE} → {END_DATE}")
    print(f"   Output    : {OUTPUT_DIR}/\n")

    fetch_all_districts()
    preview()
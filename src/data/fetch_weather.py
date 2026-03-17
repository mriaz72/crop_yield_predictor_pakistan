from pathlib import Path

import pandas as pd


def fetch_weather_data(output_path: Path) -> Path:
    """Create a placeholder weather dataset and save it to CSV."""
    output_path.parent.mkdir(parents=True, exist_ok=True)

    df = pd.DataFrame(
        {
            "district": ["Lahore", "Multan"],
            "temperature_c": [29.5, 33.1],
            "rainfall_mm": [12.4, 5.8],
        }
    )
    df.to_csv(output_path, index=False)
    return output_path


if __name__ == "__main__":
    target = Path("data/raw/weather/weather_sample.csv")
    path = fetch_weather_data(target)
    print(f"Saved weather data to: {path}")

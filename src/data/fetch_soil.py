from pathlib import Path

import pandas as pd


def fetch_soil_data(output_path: Path) -> Path:
    """Create a placeholder soil dataset and save it to CSV."""
    output_path.parent.mkdir(parents=True, exist_ok=True)

    df = pd.DataFrame(
        {
            "district": ["Lahore", "Multan"],
            "ph": [7.2, 7.8],
            "organic_matter_pct": [1.4, 0.9],
        }
    )
    df.to_csv(output_path, index=False)
    return output_path


if __name__ == "__main__":
    target = Path("data/raw/soil/soil_sample.csv")
    path = fetch_soil_data(target)
    print(f"Saved soil data to: {path}")

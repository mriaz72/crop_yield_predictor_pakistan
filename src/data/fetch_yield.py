from pathlib import Path

import pandas as pd


def fetch_yield_data(output_path: Path) -> Path:
    """Create a placeholder crop yield dataset and save it to CSV."""
    output_path.parent.mkdir(parents=True, exist_ok=True)

    df = pd.DataFrame(
        {
            "district": ["Lahore", "Multan"],
            "crop": ["Wheat", "Cotton"],
            "yield_tonnes_per_hectare": [3.2, 2.6],
        }
    )
    df.to_csv(output_path, index=False)
    return output_path


if __name__ == "__main__":
    target = Path("data/raw/yield/yield_sample.csv")
    path = fetch_yield_data(target)
    print(f"Saved yield data to: {path}")

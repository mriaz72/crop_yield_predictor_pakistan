# Crop Yield Prediction - Pakistan

This repository contains data collection utilities and project structure for a crop yield prediction workflow in Pakistan.

## Project Structure

```text
.
├── data/
│   ├── raw/
│   │   ├── weather/
│   │   ├── yield/
│   │   ├── soil/
│   │   └── ndvi/
│   ├── processed/
│   └── external/
├── notebooks/
│   └── 01_data_collection.ipynb
├── src/
│   ├── data/
│   │   ├── fetch_weather.py
│   │   ├── fetch_yield.py
│   │   └── fetch_soil.py
│   └── utils/
│       └── mongo_utils.py
├── .env
├── .gitignore
├── pyproject.toml
└── README.md
```

## UV Setup

1. Create or reuse virtual environment:
   - `uv venv .venv`
2. Activate environment (PowerShell):
   - `.venv\Scripts\activate`
3. Install project dependencies:
   - `uv sync`
4. Add a package:
   - `uv add <package-name>`

## Notes

- This project uses `pyproject.toml` (uv standard) instead of `requirements.txt`.
- Keep raw datasets inside the respective folders under `data/raw/`.

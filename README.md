# 🌾 CropYield Predictor — Pakistan

> Machine learning system for predicting crop yields across Punjab, Pakistan — powered by weather, soil, satellite, and historical data.

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.4+-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)](https://scikit-learn.org)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-EE4C2C?style=flat-square&logo=pytorch&logoColor=white)](https://pytorch.org)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-FF6F00?style=flat-square&logo=tensorflow&logoColor=white)](https://tensorflow.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.x-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)](https://streamlit.io)
[![MongoDB](https://img.shields.io/badge/MongoDB-Atlas-47A248?style=flat-square&logo=mongodb&logoColor=white)](https://www.mongodb.com/atlas)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](LICENSE)

---

## 📌 Overview

**CropYield Predictor** is an end-to-end machine learning pipeline designed to forecast yields for **Wheat**, **Cotton**, and **Rice** — the three major crops of Punjab, Pakistan.

Agriculture employs over **38% of Pakistan's workforce** and contributes significantly to its GDP. Yet yield forecasting remains largely manual, reactive, and imprecise. This project aims to change that by combining multiple data streams — weather patterns, satellite vegetation indices, soil properties, and historical yield records — into a unified predictive system accessible through an interactive web dashboard.

### 🎯 Goals

- Predict seasonal crop yields at the district level across Punjab
- Identify key environmental and agronomic drivers of yield variation
- Provide an interpretable, accessible dashboard for farmers and agronomists
- Build a reproducible, open-source pipeline that can be extended to other regions of Pakistan

---

## 🏗️ Architecture

```
Raw Data Ingestion                Processing               Modeling              Serving
─────────────────                 ──────────               ────────              ───────
  Weather API    ─┐
  Yield Records  ─┤──► MongoDB Atlas ──► Feature ──► ML/DL ──► Evaluation ──► Streamlit
  Soil Data      ─┤      (Raw Store)     Engineering   Models     & Registry      Dashboard
  NDVI (Satellite)┘                         │
                                            └──► Processed Store (data/processed/)
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Data Storage** | MongoDB Atlas |
| **Data Processing** | Pandas, NumPy |
| **Classical ML** | scikit-learn (Random Forest, XGBoost, Ridge) |
| **Deep Learning** | PyTorch, TensorFlow/Keras (LSTM, MLP) |
| **Dashboard** | Streamlit |
| **Deployment** | DigitalOcean |
| **Environment** | Python 3.11+, `uv` |
| **Version Control** | Git + GitHub |

---

## 📂 Project Structure

```
.
├── data/
│   ├── raw/
│   │   ├── weather/          # Temperature, rainfall, humidity time series
│   │   ├── yield/            # Historical district-level yield records
│   │   ├── soil/             # Soil type, pH, organic matter
│   │   └── ndvi/             # Satellite NDVI (vegetation index)
│   ├── processed/            # Cleaned, merged, feature-engineered data
│   └── external/             # Third-party datasets (FAO, PBS, etc.)
├── notebooks/
│   └── 01_data_collection.ipynb
├── src/
│   ├── data/
│   │   ├── fetch_weather.py
│   │   ├── fetch_yield.py
│   │   └── fetch_soil.py
│   └── utils/
│       └── mongo_utils.py
├── .env                      # Environment variables (never commit this!)
├── .gitignore
├── pyproject.toml
└── README.md
```

---

## 🌍 Data Sources

| Data Type | Source | Description |
|---|---|---|
| **Weather** | [Open-Meteo](https://open-meteo.com/) / ERA5 | Temperature, rainfall, humidity, solar radiation |
| **Crop Yield** | [Pakistan Bureau of Statistics](https://www.pbs.gov.pk/) | District-level annual yield records |
| **Soil** | [FAO HWSD](https://www.fao.org/soils-portal/) | Soil texture, organic carbon, pH |
| **NDVI** | [NASA MODIS / Google Earth Engine](https://earthengine.google.com/) | Seasonal vegetation index (250m resolution) |
| **Administrative** | [GADM](https://gadm.org/) | Punjab district boundaries (GeoJSON) |

> ⚠️ Some datasets require registration or API keys. See `.env.example` for required variables.

---

## ⚡ Setup & Installation

### Prerequisites

- Python 3.11+
- [`uv`](https://github.com/astral-sh/uv) package manager
- MongoDB Atlas account (free tier works)
- Git

### 1. Clone the repository

```bash
git clone https://github.com/your-username/cropyield-predictor-pakistan.git
cd cropyield-predictor-pakistan
```

### 2. Create and activate virtual environment

```bash
uv venv
source .venv/bin/activate        # Linux/macOS
.venv\Scripts\activate           # Windows
```

### 3. Install dependencies

```bash
uv pip install -e .
```

### 4. Configure environment variables

```bash
cp .env.example .env
# Edit .env with your MongoDB URI, API keys, etc.
```

### 5. Run the Streamlit dashboard (once available)

```bash
streamlit run app.py
```

---

## 🗺️ Roadmap

### Phase 1 — Data Collection *(in progress)*
- [x] Project structure & environment setup
- [ ] Weather data ingestion pipeline
- [ ] Historical yield data ingestion
- [ ] Soil data ingestion
- [ ] NDVI satellite data ingestion
- [ ] Store all raw data in MongoDB Atlas

### Phase 2 — Data Processing
- [ ] Data cleaning & missing value handling
- [ ] Feature engineering (growing degree days, rainfall aggregates, etc.)
- [ ] Exploratory data analysis (EDA) notebooks
- [ ] Processed dataset export

### Phase 3 — Modeling
- [ ] Baseline models (Ridge Regression, Random Forest)
- [ ] Advanced models (XGBoost, LSTM, MLP)
- [ ] Model evaluation & comparison
- [ ] Interpretability analysis (SHAP values)

### Phase 4 — Dashboard & Deployment
- [ ] Streamlit dashboard with district-level visualizations
- [ ] Crop-wise prediction interface (Wheat, Cotton, Rice)
- [ ] Deploy to DigitalOcean
- [ ] CI/CD pipeline

### Phase 5 — Future Work
- [ ] Extend to other provinces (Sindh, KPK)
- [ ] Integrate real-time weather forecasts for in-season prediction
- [ ] SMS/WhatsApp alert system for farmers
- [ ] Urdu language support in dashboard

---

## 🤝 Contributing

Contributions are welcome! If you have domain expertise in Pakistani agriculture, remote sensing, or ML — please open an issue or submit a PR.

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Muhammad Riaz**
- GitHub:https://github.com/mriaz72
- Location: Punjab, Pakistan 🇵🇰

---

<p align="center">
  Built with ❤️ for Pakistani farmers and agronomists
</p>
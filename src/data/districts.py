# src/data/districts.py
# Central registry of all 36 Punjab districts with centroid coordinates.
# Used by all data fetchers (weather, soil, NDVI) to ensure consistency.

PUNJAB_DISTRICTS: dict[str, tuple[float, float]] = {
    "Lahore":          (31.5497, 74.3436),
    "Faisalabad":      (31.4504, 73.1350),
    "Rawalpindi":      (33.6007, 73.0679),
    "Gujranwala":      (32.1877, 74.1945),
    "Multan":          (30.1978, 71.4711),
    "Bahawalpur":      (29.3956, 71.6722),
    "Sargodha":        (32.0836, 72.6711),
    "Sialkot":         (32.4945, 74.5229),
    "Sheikhupura":     (31.7167, 73.9850),
    "Rahim Yar Khan":  (28.4212, 70.2989),
    "Jhang":           (31.2681, 72.3181),
    "Dera Ghazi Khan": (30.0489, 70.6323),
    "Gujrat":          (32.5736, 74.0785),
    "Sahiwal":         (30.6706, 73.1064),
    "Okara":           (30.8138, 73.4534),
    "Kasur":           (31.1167, 74.4500),
    "Hafizabad":       (32.0714, 73.6878),
    "Chiniot":         (31.7197, 72.9783),
    "Khanewal":        (30.3014, 71.9322),
    "Bahawalnagar":    (29.9956, 73.2536),
    "Pakpattan":       (30.3436, 73.3872),
    "Mandi Bahauddin": (32.5864, 73.4917),
    "Muzaffargarh":    (30.0736, 71.1928),
    "Lodhran":         (29.5339, 71.6322),
    "Vehari":          (30.0453, 72.3519),
    "Narowal":         (32.1014, 74.8756),
    "Mianwali":        (32.5853, 71.5436),
    "Chakwal":         (32.9328, 72.8556),
    "Jhelum":          (32.9361, 73.7261),
    "Khushab":         (32.2981, 72.3519),
    "Bhakkar":         (31.6278, 71.0644),
    "Layyah":          (30.9614, 70.9397),
    "Rajanpur":        (29.1036, 70.3303),
    "Attock":          (33.7667, 72.3603),
    "Toba Tek Singh":  (30.9714, 72.4828),
    "Wah Cantt":       (33.7667, 72.7000),
}

# Target crops for this project
TARGET_CROPS = ["Wheat", "Cotton", "Rice"]

# Data collection date range
START_DATE = "2000-01-01"
END_DATE   = "2024-12-31"
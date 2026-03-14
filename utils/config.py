"""
Configuration settings for GLOF-RISK AI platform.
"""

# Physical constants
WATER_DENSITY = 1000  # kg/m³
GRAVITY = 9.81  # m/s²
MANNING_ROUGHNESS = 0.035  # Typical for mountain rivers

# Empirical constants for Himalayan GLOFs
PEAK_DISCHARGE_CONSTANT = 0.75  # k in Q_peak = k * V^0.67

# Risk calculation weights
HAZARD_WEIGHTS = {
    'breach_probability': 0.4,
    'rainfall_intensity': 0.3,
    'lake_growth_rate': 0.3
}

RISK_WEIGHTS = {
    'hazard': 0.4,
    'exposure': 0.3,
    'vulnerability': 0.2,
    'response_capacity': 0.1
}

# Risk thresholds
RISK_THRESHOLDS = {
    'low': 30,
    'medium': 60,
    'high': 80,
    'critical': 100
}

# Data paths
DATA_DIR = "data"
MODELS_DIR = "models"

# Monitoring update interval (seconds)
MONITORING_INTERVAL = 600  # 10 minutes

# Default values
DEFAULT_RAINFALL = 50  # mm/day
DEFAULT_TEMPERATURE_ANOMALY = 0.0  # °C

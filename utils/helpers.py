"""
Helper utility functions for GLOF-RISK AI platform.
"""

import numpy as np
from typing import Tuple, List, Dict
import pandas as pd


def calculate_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """
    Calculate distance between two points using Haversine formula.
    
    Args:
        lat1, lon1: Coordinates of first point
        lat2, lon2: Coordinates of second point
    
    Returns:
        Distance in kilometers
    """
    R = 6371  # Earth radius in km
    
    dlat = np.radians(lat2 - lat1)
    dlon = np.radians(lon2 - lon1)
    
    a = (np.sin(dlat/2)**2 + 
         np.cos(np.radians(lat1)) * np.cos(np.radians(lat2)) * np.sin(dlon/2)**2)
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1-a))
    
    return R * c


def normalize_score(value: float, min_val: float, max_val: float) -> float:
    """
    Normalize a value to 0-100 scale.
    
    Args:
        value: Value to normalize
        min_val: Minimum expected value
        max_val: Maximum expected value
    
    Returns:
        Normalized score (0-100)
    """
    if max_val == min_val:
        return 0.0
    normalized = ((value - min_val) / (max_val - min_val)) * 100
    return max(0, min(100, normalized))


def classify_risk(risk_score: float) -> str:
    """
    Classify risk score into categories.
    
    Args:
        risk_score: Risk score (0-100)
    
    Returns:
        Risk category string
    """
    if risk_score < 30:
        return "Low"
    elif risk_score < 60:
        return "Medium"
    elif risk_score < 80:
        return "High"
    else:
        return "Critical"


def format_large_number(value: float) -> str:
    """
    Format large numbers in scientific notation for display.
    
    Args:
        value: Number to format
    
    Returns:
        Formatted string
    """
    if value >= 1e12:
        return f"{value/1e12:.2f} × 10¹²"
    elif value >= 1e9:
        return f"{value/1e9:.2f} × 10⁹"
    elif value >= 1e6:
        return f"{value/1e6:.2f} × 10⁶"
    elif value >= 1e3:
        return f"{value/1e3:.2f} × 10³"
    else:
        return f"{value:.2f}"


def calculate_flood_arrival_time(distance_km: float, velocity_ms: float) -> float:
    """
    Calculate flood arrival time in minutes.
    
    Args:
        distance_km: Distance in kilometers
        velocity_ms: Velocity in m/s
    
    Returns:
        Arrival time in minutes
    """
    if velocity_ms <= 0:
        return float('inf')
    distance_m = distance_km * 1000
    time_seconds = distance_m / velocity_ms
    return time_seconds / 60  # Convert to minutes


def generate_synthetic_ml_data(n_samples: int = 1000) -> pd.DataFrame:
    """
    Generate synthetic training data for ML model.
    
    Args:
        n_samples: Number of samples to generate
    
    Returns:
        DataFrame with features and target
    """
    np.random.seed(42)
    
    data = {
        'lake_area': np.random.uniform(0.1, 5.0, n_samples),  # km²
        'lake_volume': np.random.uniform(0.5, 50.0, n_samples),  # million m³
        'dam_type': np.random.choice(['moraine', 'ice', 'bedrock'], n_samples),
        'rainfall_intensity': np.random.uniform(0, 200, n_samples),  # mm/day
        'terrain_slope': np.random.uniform(5, 45, n_samples),  # degrees
        'temperature_anomaly': np.random.uniform(-2, 5, n_samples),  # °C
    }
    
    df = pd.DataFrame(data)
    
    # Generate synthetic breach probability based on features
    breach_prob = (
        0.3 * (df['lake_volume'] / 50.0) +
        0.2 * (df['rainfall_intensity'] / 200.0) +
        0.2 * (df['terrain_slope'] / 45.0) +
        0.15 * (df['temperature_anomaly'] / 5.0) +
        0.15 * np.random.random(n_samples)
    )
    
    df['breach_probability'] = np.clip(breach_prob, 0, 1)
    df['breach_occurred'] = (df['breach_probability'] > 0.5).astype(int)
    
    return df

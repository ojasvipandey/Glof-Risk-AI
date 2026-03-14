"""
Real-time rainfall monitoring module.
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from typing import Dict, Optional
from modules.data_loader import DataLoader


class RainfallMonitor:
    """Monitor rainfall and environmental indicators."""
    
    def __init__(self, data_loader: Optional[DataLoader] = None):
        """
        Initialize rainfall monitor.
        
        Args:
            data_loader: DataLoader instance
        """
        self.data_loader = data_loader or DataLoader()
        self.update_interval = 600  # 10 minutes
    
    def get_current_rainfall(self, district: str) -> float:
        """
        Get current rainfall for a district.
        
        Args:
            district: District name
        
        Returns:
            Current rainfall in mm/day
        """
        return self.data_loader.get_rainfall_by_district(district)
    
    def get_rainfall_trend(self, district: str, days: int = 7) -> pd.DataFrame:
        """
        Get rainfall trend over specified days.
        
        Args:
            district: District name
            days: Number of days to look back
        
        Returns:
            DataFrame with rainfall trend
        """
        rainfall_data = self.data_loader.load_rainfall_data()
        district_data = rainfall_data[rainfall_data['district'] == district].copy()
        
        if len(district_data) == 0:
            # Generate synthetic trend
            dates = pd.date_range(end=datetime.now(), periods=days, freq='D')
            trend = pd.DataFrame({
                'date': dates,
                'rainfall_mm': np.random.uniform(0, 100, days)
            })
            return trend
        
        # Convert timestamp if needed
        if 'timestamp' in district_data.columns:
            district_data['date'] = pd.to_datetime(district_data['timestamp'])
            district_data = district_data.sort_values('date')
            district_data = district_data.tail(days)
        
        return district_data[['date', 'rainfall_mm']] if 'date' in district_data.columns else district_data
    
    def calculate_rainfall_intensity_level(self, rainfall_mm: float) -> str:
        """
        Classify rainfall intensity.
        
        Args:
            rainfall_mm: Rainfall in mm/day
        
        Returns:
            Intensity level string
        """
        if rainfall_mm < 10:
            return "Light"
        elif rainfall_mm < 25:
            return "Moderate"
        elif rainfall_mm < 50:
            return "Heavy"
        elif rainfall_mm < 100:
            return "Very Heavy"
        else:
            return "Extreme"
    
    def get_environmental_indicators(
        self,
        district: str,
        temperature_anomaly: float = 0.0
    ) -> Dict:
        """
        Get environmental monitoring indicators.
        
        Args:
            district: District name
            temperature_anomaly: Temperature anomaly in °C
        
        Returns:
            Dictionary with environmental indicators
        """
        rainfall = self.get_current_rainfall(district)
        trend = self.get_rainfall_trend(district, days=7)
        
        avg_rainfall = trend['rainfall_mm'].mean() if len(trend) > 0 else rainfall
        max_rainfall = trend['rainfall_mm'].max() if len(trend) > 0 else rainfall
        
        return {
            'current_rainfall_mm': rainfall,
            'avg_rainfall_7d_mm': avg_rainfall,
            'max_rainfall_7d_mm': max_rainfall,
            'rainfall_intensity': self.calculate_rainfall_intensity_level(rainfall),
            'temperature_anomaly_c': temperature_anomaly,
            'last_updated': datetime.now().isoformat()
        }

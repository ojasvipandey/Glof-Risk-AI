"""
Data loading module for GLOF-RISK AI platform.
"""

import pandas as pd
import numpy as np
from pathlib import Path
from typing import Dict, Optional
import os

from utils.config import DATA_DIR


class DataLoader:
    """Load and manage data for GLOF risk assessment."""
    
    def __init__(self, data_dir: str = DATA_DIR):
        """
        Initialize data loader.
        
        Args:
            data_dir: Directory containing data files
        """
        self.data_dir = Path(data_dir)
        self._glacial_lakes = None
        self._rainfall_data = None
        self._population_data = None
        self._infrastructure_data = None
    
    def load_glacial_lakes(self) -> pd.DataFrame:
        """
        Load glacial lake inventory data.
        
        Returns:
            DataFrame with glacial lake information
        """
        if self._glacial_lakes is None:
            file_path = self.data_dir / "glacial_lakes.csv"
            if file_path.exists():
                self._glacial_lakes = pd.read_csv(file_path)
            else:
                # Return empty DataFrame with expected columns
                self._glacial_lakes = pd.DataFrame(columns=[
                    'lake_name', 'latitude', 'longitude', 'lake_area',
                    'lake_volume', 'elevation', 'dam_type'
                ])
        return self._glacial_lakes
    
    def load_rainfall_data(self) -> pd.DataFrame:
        """
        Load rainfall monitoring data.
        
        Returns:
            DataFrame with rainfall information
        """
        if self._rainfall_data is None:
            file_path = self.data_dir / "rainfall_data.csv"
            if file_path.exists():
                self._rainfall_data = pd.read_csv(file_path)
            else:
                self._rainfall_data = pd.DataFrame(columns=[
                    'district', 'rainfall_mm', 'timestamp'
                ])
        return self._rainfall_data
    
    def load_population_data(self) -> pd.DataFrame:
        """
        Load population data for villages.
        
        Returns:
            DataFrame with village population information
        """
        if self._population_data is None:
            file_path = self.data_dir / "population_data.csv"
            if file_path.exists():
                self._population_data = pd.read_csv(file_path)
            else:
                self._population_data = pd.DataFrame(columns=[
                    'village_name', 'population', 'latitude', 'longitude', 'district'
                ])
        return self._population_data
    
    def load_infrastructure_data(self) -> pd.DataFrame:
        """
        Load infrastructure data.
        
        Returns:
            DataFrame with infrastructure information
        """
        if self._infrastructure_data is None:
            file_path = self.data_dir / "infrastructure_data.csv"
            if file_path.exists():
                self._infrastructure_data = pd.read_csv(file_path)
            else:
                self._infrastructure_data = pd.DataFrame(columns=[
                    'infrastructure_type', 'name', 'latitude', 'longitude', 'district'
                ])
        return self._infrastructure_data
    
    def get_lake_by_name(self, lake_name: str) -> Optional[Dict]:
        """
        Get glacial lake data by name.
        
        Args:
            lake_name: Name of the glacial lake
        
        Returns:
            Dictionary with lake data or None if not found
        """
        lakes = self.load_glacial_lakes()
        lake = lakes[lakes['lake_name'] == lake_name]
        if len(lake) > 0:
            return lake.iloc[0].to_dict()
        return None
    
    def get_rainfall_by_district(self, district: str) -> float:
        """
        Get latest rainfall data for a district.
        
        Args:
            district: District name
        
        Returns:
            Latest rainfall in mm/day
        """
        rainfall = self.load_rainfall_data()
        district_rainfall = rainfall[rainfall['district'] == district]
        if len(district_rainfall) > 0:
            return district_rainfall['rainfall_mm'].iloc[-1]
        return 0.0
    
    def get_villages_in_district(self, district: str) -> pd.DataFrame:
        """
        Get all villages in a district.
        
        Args:
            district: District name
        
        Returns:
            DataFrame with village data
        """
        population = self.load_population_data()
        return population[population['district'] == district]

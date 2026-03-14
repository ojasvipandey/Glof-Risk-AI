"""
Geospatial analysis module for terrain and river path analysis.
"""

import numpy as np
from typing import List, Tuple, Dict, Optional
from utils.helpers import calculate_distance


class GeospatialAnalysis:
    """Geospatial analysis for flood path and terrain."""
    
    @staticmethod
    def calculate_terrain_slope(
        elevation_start: float,
        elevation_end: float,
        distance_km: float
    ) -> float:
        """
        Calculate terrain slope.
        
        Args:
            elevation_start: Starting elevation in meters
            elevation_end: Ending elevation in meters
            distance_km: Distance in kilometers
        
        Returns:
            Slope in degrees
        """
        if distance_km <= 0:
            return 0.0
        
        elevation_drop = elevation_start - elevation_end
        distance_m = distance_km * 1000
        slope_ratio = elevation_drop / distance_m
        slope_deg = np.degrees(np.arctan(slope_ratio))
        
        return max(0, slope_deg)
    
    @staticmethod
    def estimate_elevation_drop(
        lake_elevation: float,
        distance_km: float,
        avg_slope_deg: float = 15.0
    ) -> float:
        """
        Estimate elevation drop along flood path.
        
        Args:
            lake_elevation: Lake elevation in meters
            distance_km: Distance in kilometers
            avg_slope_deg: Average slope in degrees
        
        Returns:
            Elevation drop in meters
        """
        distance_m = distance_km * 1000
        elevation_drop = distance_m * np.tan(np.radians(avg_slope_deg))
        return elevation_drop
    
    @staticmethod
    def find_downstream_path(
        lake_lat: float,
        lake_lon: float,
        villages: List[Dict],
        max_distance_km: float = 100.0
    ) -> List[Dict]:
        """
        Find villages in downstream path from lake.
        
        Args:
            lake_lat: Lake latitude
            lake_lon: Lake longitude
            villages: List of village dictionaries with lat/lon
            max_distance_km: Maximum distance to consider
        
        Returns:
            List of villages in downstream path, sorted by distance
        """
        downstream_villages = []
        
        for village in villages:
            distance = calculate_distance(
                lake_lat, lake_lon,
                village['latitude'], village['longitude']
            )
            
            if distance <= max_distance_km:
                village_copy = village.copy()
                village_copy['distance_km'] = distance
                downstream_villages.append(village_copy)
        
        # Sort by distance
        downstream_villages.sort(key=lambda x: x['distance_km'])
        
        return downstream_villages
    
    @staticmethod
    def calculate_river_path_segments(
        lake_lat: float,
        lake_lon: float,
        villages: List[Dict]
    ) -> List[Dict]:
        """
        Calculate river path segments between lake and villages.
        
        Args:
            lake_lat: Lake latitude
            lake_lon: Lake longitude
            villages: List of villages in downstream path
        
        Returns:
            List of path segments with distances
        """
        segments = []
        prev_lat, prev_lon = lake_lat, lake_lon
        
        for village in villages:
            distance = calculate_distance(
                prev_lat, prev_lon,
                village['latitude'], village['longitude']
            )
            
            segments.append({
                'from_lat': prev_lat,
                'from_lon': prev_lon,
                'to_lat': village['latitude'],
                'to_lon': village['longitude'],
                'distance_km': distance
            })
            
            prev_lat, prev_lon = village['latitude'], village['longitude']
        
        return segments
    
    @staticmethod
    def estimate_channel_characteristics(
        distance_km: float,
        elevation_drop: float
    ) -> Dict:
        """
        Estimate channel characteristics for flood routing.
        
        Args:
            distance_km: Channel distance in kilometers
            elevation_drop: Elevation drop in meters
        
        Returns:
            Dictionary with channel characteristics
        """
        slope = GeospatialAnalysis.calculate_terrain_slope(
            elevation_drop, 0, distance_km
        )
        
        # Estimate channel width (wider downstream)
        base_width = 30.0  # meters
        width_expansion = 1 + (distance_km / 50.0)
        estimated_width = base_width * width_expansion
        
        return {
            'slope_deg': slope,
            'channel_width_m': estimated_width,
            'distance_km': distance_km,
            'elevation_drop_m': elevation_drop
        }

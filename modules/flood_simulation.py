"""
Flood propagation simulation module.
"""

import numpy as np
from typing import List, Dict, Tuple
from modules.flood_models import FloodModels
from modules.geospatial_analysis import GeospatialAnalysis
from utils.helpers import calculate_flood_arrival_time


class FloodSimulation:
    """Simulate flood propagation downstream."""
    
    def __init__(self):
        """Initialize flood simulation."""
        self.flood_models = FloodModels()
        self.geo_analysis = GeospatialAnalysis()
    
    def simulate_flood_propagation(
        self,
        lake_data: Dict,
        villages: List[Dict],
        flood_params: Dict
    ) -> List[Dict]:
        """
        Simulate flood propagation to downstream villages.
        
        Args:
            lake_data: Dictionary with lake information
            villages: List of villages in downstream path
            flood_params: Dictionary with flood parameters
        
        Returns:
            List of villages with flood simulation results
        """
        lake_lat = lake_data['latitude']
        lake_lon = lake_data['longitude']
        lake_elevation = lake_data.get('elevation', 4000)
        
        # Find downstream path
        downstream_villages = self.geo_analysis.find_downstream_path(
            lake_lat, lake_lon, villages
        )
        
        # Get flood parameters
        peak_discharge = flood_params['peak_discharge_m3s']
        flood_velocity = flood_params['flood_velocity_ms']
        
        # Simulate for each village
        simulation_results = []
        
        for village in downstream_villages:
            distance_km = village['distance_km']
            
            # Calculate elevation drop
            village_elevation = village.get('elevation', lake_elevation - 500)
            elevation_drop = lake_elevation - village_elevation
            
            # Calculate local slope
            local_slope = self.geo_analysis.calculate_terrain_slope(
                lake_elevation, village_elevation, distance_km
            )
            
            # Adjust velocity for local conditions
            local_velocity = self.flood_models.calculate_flood_velocity(local_slope)
            
            # Calculate arrival time
            arrival_time = calculate_flood_arrival_time(distance_km, local_velocity)
            
            # Estimate inundation width
            channel_chars = self.geo_analysis.estimate_channel_characteristics(
                distance_km, elevation_drop
            )
            inundation_width = self.flood_models.calculate_inundation_width(
                peak_discharge, local_velocity, channel_chars['channel_width_m']
            )
            
            # Calculate flood depth (simplified)
            flow_area = peak_discharge / local_velocity if local_velocity > 0 else 0
            flood_depth = flow_area / inundation_width if inundation_width > 0 else 0
            
            simulation_results.append({
                'village_name': village.get('village_name', 'Unknown'),
                'latitude': village['latitude'],
                'longitude': village['longitude'],
                'distance_km': distance_km,
                'arrival_time_min': arrival_time,
                'flood_velocity_ms': local_velocity,
                'inundation_width_m': inundation_width,
                'flood_depth_m': flood_depth,
                'peak_discharge_m3s': peak_discharge,
                'elevation_drop_m': elevation_drop,
                'local_slope_deg': local_slope
            })
        
        return simulation_results
    
    def generate_flood_zones(
        self,
        simulation_results: List[Dict]
    ) -> Dict[str, List[Dict]]:
        """
        Generate flood zones based on simulation results.
        
        Args:
            simulation_results: List of simulation results
        
        Returns:
            Dictionary with flood zones categorized by severity
        """
        zones = {
            'severe': [],
            'moderate': [],
            'mild': []
        }
        
        for result in simulation_results:
            depth = result['flood_depth_m']
            arrival = result['arrival_time_min']
            
            # Classify severity
            if depth > 5.0 or arrival < 30:
                zones['severe'].append(result)
            elif depth > 2.0 or arrival < 60:
                zones['moderate'].append(result)
            else:
                zones['mild'].append(result)
        
        return zones
    
    def calculate_flood_path_coordinates(
        self,
        lake_lat: float,
        lake_lon: float,
        villages: List[Dict]
    ) -> List[Tuple[float, float]]:
        """
        Generate coordinates for flood path visualization.
        
        Args:
            lake_lat: Lake latitude
            lake_lon: Lake longitude
            villages: List of villages
        
        Returns:
            List of (lat, lon) tuples for path
        """
        path = [(lake_lat, lake_lon)]
        
        for village in villages:
            path.append((village['latitude'], village['longitude']))
        
        return path

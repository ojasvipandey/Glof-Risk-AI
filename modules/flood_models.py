"""
Physics-based flood models for GLOF risk assessment.
"""

import numpy as np
from typing import Dict, Tuple
from utils.config import (
    WATER_DENSITY, GRAVITY, MANNING_ROUGHNESS, PEAK_DISCHARGE_CONSTANT
)


class FloodModels:
    """Physics-based flood modeling calculations."""
    
    @staticmethod
    def calculate_energy_release(lake_volume: float, elevation_drop: float) -> float:
        """
        Calculate potential energy stored in glacial lake.
        
        Formula: E = ρ * g * V * h
        
        Args:
            lake_volume: Lake volume in million m³
            elevation_drop: Elevation difference in meters
        
        Returns:
            Energy in Joules
        """
        volume_m3 = lake_volume * 1e6  # Convert to m³
        energy = WATER_DENSITY * GRAVITY * volume_m3 * elevation_drop
        return energy
    
    @staticmethod
    def calculate_peak_discharge(lake_volume: float) -> float:
        """
        Calculate peak flood discharge using empirical relation.
        
        Formula: Q_peak = k * V^0.67
        
        Args:
            lake_volume: Lake volume in million m³
        
        Returns:
            Peak discharge in m³/s
        """
        volume_m3 = lake_volume * 1e6  # Convert to m³
        peak_discharge = PEAK_DISCHARGE_CONSTANT * (volume_m3 ** 0.67)
        return peak_discharge
    
    @staticmethod
    def calculate_flood_velocity(
        slope: float,
        hydraulic_radius: float = 2.0,
        manning_n: float = MANNING_ROUGHNESS
    ) -> float:
        """
        Calculate flood velocity using Manning equation.
        
        Formula: V = (1/n) * R^(2/3) * S^(1/2)
        
        Args:
            slope: Channel slope (m/m or dimensionless)
            hydraulic_radius: Hydraulic radius in meters
            manning_n: Manning roughness coefficient
        
        Returns:
            Velocity in m/s
        """
        if slope <= 0:
            return 0.0
        
        slope_rad = np.radians(slope) if slope > 1 else slope
        velocity = (1.0 / manning_n) * (hydraulic_radius ** (2/3)) * (slope_rad ** 0.5)
        return max(0, velocity)
    
    @staticmethod
    def calculate_flood_arrival_time(distance_km: float, velocity_ms: float) -> float:
        """
        Calculate flood arrival time.
        
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
    
    @staticmethod
    def calculate_inundation_width(
        discharge: float,
        velocity: float,
        channel_width: float = 50.0
    ) -> float:
        """
        Estimate inundation width based on discharge and velocity.
        
        Args:
            discharge: Flood discharge in m³/s
            velocity: Flood velocity in m/s
            channel_width: Base channel width in meters
        
        Returns:
            Estimated inundation width in meters
        """
        if velocity <= 0:
            return channel_width
        
        flow_area = discharge / velocity
        depth = flow_area / channel_width
        # Simple expansion model: width increases with depth
        expansion_factor = 1 + (depth / 10.0)  # Rough estimate
        inundation_width = channel_width * expansion_factor
        
        return max(channel_width, inundation_width)
    
    @staticmethod
    def calculate_flood_parameters(
        lake_volume: float,
        elevation_drop: float,
        terrain_slope: float
    ) -> Dict[str, float]:
        """
        Calculate all flood parameters for a given lake.
        
        Args:
            lake_volume: Lake volume in million m³
            elevation_drop: Elevation difference in meters
            terrain_slope: Terrain slope in degrees
        
        Returns:
            Dictionary with all flood parameters
        """
        energy = FloodModels.calculate_energy_release(lake_volume, elevation_drop)
        peak_discharge = FloodModels.calculate_peak_discharge(lake_volume)
        velocity = FloodModels.calculate_flood_velocity(terrain_slope)
        
        return {
            'energy_release_joules': energy,
            'peak_discharge_m3s': peak_discharge,
            'flood_velocity_ms': velocity,
            'elevation_drop_m': elevation_drop,
            'terrain_slope_deg': terrain_slope
        }

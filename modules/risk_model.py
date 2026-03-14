"""
Risk index calculation module.
"""

import numpy as np
from typing import Dict
from utils.config import HAZARD_WEIGHTS, RISK_WEIGHTS
from utils.helpers import normalize_score, classify_risk


class RiskModel:
    """Calculate GLOF risk index."""
    
    @staticmethod
    def calculate_hazard_score(
        breach_probability: float,
        rainfall_intensity: float,
        lake_growth_rate: float = 0.0
    ) -> float:
        """
        Calculate hazard score.
        
        Args:
            breach_probability: Breach probability (0-1)
            rainfall_intensity: Rainfall intensity (mm/day)
            lake_growth_rate: Lake growth rate (%/year)
        
        Returns:
            Hazard score (0-100)
        """
        # Normalize components
        breach_norm = breach_probability * 100
        rainfall_norm = normalize_score(rainfall_intensity, 0, 200)
        growth_norm = normalize_score(lake_growth_rate, 0, 10)
        
        # Weighted combination
        hazard = (
            HAZARD_WEIGHTS['breach_probability'] * breach_norm +
            HAZARD_WEIGHTS['rainfall_intensity'] * rainfall_norm +
            HAZARD_WEIGHTS['lake_growth_rate'] * growth_norm
        )
        
        return min(100, max(0, hazard))
    
    @staticmethod
    def calculate_exposure_score(
        population_exposed: int,
        infrastructure_count: int = 0
    ) -> float:
        """
        Calculate exposure score.
        
        Args:
            population_exposed: Total population at risk
            infrastructure_count: Number of critical infrastructure
        
        Returns:
            Exposure score (0-100)
        """
        # Normalize population (assuming max 100,000)
        pop_norm = normalize_score(population_exposed, 0, 100000)
        
        # Normalize infrastructure (assuming max 20)
        infra_norm = normalize_score(infrastructure_count, 0, 20)
        
        # Weighted combination
        exposure = 0.7 * pop_norm + 0.3 * infra_norm
        
        return min(100, max(0, exposure))
    
    @staticmethod
    def calculate_vulnerability_score(
        terrain_slope: float,
        building_resilience: float = 0.5
    ) -> float:
        """
        Calculate vulnerability score.
        
        Args:
            terrain_slope: Terrain slope in degrees
            building_resilience: Building resilience factor (0-1)
        
        Returns:
            Vulnerability score (0-100)
        """
        # Higher slope = higher vulnerability
        slope_norm = normalize_score(terrain_slope, 0, 45)
        
        # Lower resilience = higher vulnerability
        resilience_norm = (1 - building_resilience) * 100
        
        # Weighted combination
        vulnerability = 0.6 * slope_norm + 0.4 * resilience_norm
        
        return min(100, max(0, vulnerability))
    
    @staticmethod
    def calculate_response_capacity_score(
        evacuation_routes: int = 1,
        warning_systems: bool = True
    ) -> float:
        """
        Calculate response capacity score (inverse of risk).
        
        Args:
            evacuation_routes: Number of evacuation routes
            warning_systems: Presence of warning systems
        
        Returns:
            Response capacity score (0-100, higher = better capacity)
        """
        routes_norm = normalize_score(evacuation_routes, 0, 5)
        warning_score = 100 if warning_systems else 30
        
        capacity = 0.5 * routes_norm + 0.5 * warning_score
        
        return min(100, max(0, capacity))
    
    @staticmethod
    def calculate_risk_index(
        hazard_score: float,
        exposure_score: float,
        vulnerability_score: float,
        response_capacity_score: float
    ) -> Dict[str, float]:
        """
        Calculate overall risk index.
        
        Formula: Risk = (Hazard × Exposure × Vulnerability) / ResponseCapacity
        
        Args:
            hazard_score: Hazard score (0-100)
            exposure_score: Exposure score (0-100)
            vulnerability_score: Vulnerability score (0-100)
            response_capacity_score: Response capacity score (0-100)
        
        Returns:
            Dictionary with risk components and final index
        """
        # Normalize response capacity (inverse relationship)
        response_factor = max(0.1, (100 - response_capacity_score) / 100)
        
        # Calculate risk
        risk_index = (
            (hazard_score * exposure_score * vulnerability_score) /
            (response_capacity_score + 1)  # Add 1 to avoid division by zero
        )
        
        # Normalize to 0-100 scale
        risk_index = min(100, max(0, risk_index))
        
        return {
            'hazard_score': hazard_score,
            'exposure_score': exposure_score,
            'vulnerability_score': vulnerability_score,
            'response_capacity_score': response_capacity_score,
            'risk_index': risk_index,
            'risk_category': classify_risk(risk_index)
        }

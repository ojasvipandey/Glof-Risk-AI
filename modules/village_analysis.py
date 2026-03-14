"""
Village exposure analysis module.
"""

import pandas as pd
from typing import List, Dict
from modules.flood_simulation import FloodSimulation
from utils.helpers import classify_risk


class VillageAnalysis:
    """Analyze village exposure to GLOF risk."""
    
    def __init__(self):
        """Initialize village analysis."""
        self.flood_sim = FloodSimulation()
    
    def analyze_village_exposure(
        self,
        lake_data: Dict,
        villages: List[Dict],
        flood_params: Dict,
        risk_index: float
    ) -> pd.DataFrame:
        """
        Analyze exposure of villages to GLOF risk.
        
        Args:
            lake_data: Dictionary with lake information
            villages: List of villages
            flood_params: Dictionary with flood parameters
            risk_index: Overall risk index
        
        Returns:
            DataFrame with village exposure analysis
        """
        # Simulate flood propagation
        simulation_results = self.flood_sim.simulate_flood_propagation(
            lake_data, villages, flood_params
        )
        
        # Create analysis DataFrame
        analysis_data = []
        
        for result in simulation_results:
            # Find corresponding village data
            village_name = result['village_name']
            village_data = next(
                (v for v in villages if v.get('village_name') == village_name),
                {}
            )
            
            # Calculate village-specific risk
            arrival_time = result['arrival_time_min']
            flood_depth = result['flood_depth_m']
            population = village_data.get('population', 0)
            
            # Risk level based on arrival time and depth
            if arrival_time < 30 or flood_depth > 5:
                village_risk = "Critical"
            elif arrival_time < 60 or flood_depth > 2:
                village_risk = "High"
            elif arrival_time < 120:
                village_risk = "Medium"
            else:
                village_risk = "Low"
            
            analysis_data.append({
                'Village': village_name,
                'Population': int(population) if population else 0,
                'Distance (km)': round(result['distance_km'], 2),
                'Flood Arrival (min)': round(arrival_time, 1) if arrival_time != float('inf') else 'N/A',
                'Flood Depth (m)': round(flood_depth, 2),
                'Risk Level': village_risk,
                'Latitude': result['latitude'],
                'Longitude': result['longitude']
            })
        
        df = pd.DataFrame(analysis_data)
        
        # Sort by arrival time
        df['SortKey'] = df['Flood Arrival (min)'].apply(
            lambda x: float('inf') if x == 'N/A' else float(x)
        )
        df = df.sort_values('SortKey')
        df = df.drop('SortKey', axis=1)
        
        return df
    
    def get_critical_villages(
        self,
        village_analysis: pd.DataFrame,
        threshold: str = "High"
    ) -> pd.DataFrame:
        """
        Get villages above risk threshold.
        
        Args:
            village_analysis: DataFrame from analyze_village_exposure
            threshold: Risk threshold (Low, Medium, High, Critical)
        
        Returns:
            Filtered DataFrame with critical villages
        """
        risk_order = {"Low": 0, "Medium": 1, "High": 2, "Critical": 3}
        threshold_level = risk_order.get(threshold, 2)
        
        filtered = village_analysis[
            village_analysis['Risk Level'].apply(
                lambda x: risk_order.get(x, 0) >= threshold_level
            )
        ]
        
        return filtered

"""
Evacuation planning module.
"""

from typing import List, Dict
from datetime import datetime, timedelta
import pandas as pd


class EvacuationPlanner:
    """Generate evacuation recommendations."""
    
    @staticmethod
    def calculate_evacuation_window(
        flood_arrival_min: float,
        buffer_factor: float = 0.3
    ) -> Dict[str, float]:
        """
        Calculate evacuation time window.
        
        Args:
            flood_arrival_min: Flood arrival time in minutes
            buffer_factor: Safety buffer factor (0-1)
        
        Returns:
            Dictionary with evacuation timing information
        """
        if flood_arrival_min == float('inf'):
            return {
                'evacuation_window_min': 0,
                'preparation_time_min': 0,
                'status': 'Safe'
            }
        
        # Evacuation window is arrival time minus buffer
        buffer_time = flood_arrival_min * buffer_factor
        evacuation_window = max(0, flood_arrival_min - buffer_time)
        
        # Preparation time (time before evacuation must start)
        preparation_time = max(0, evacuation_window - 30)  # 30 min prep
        
        # Determine status
        if evacuation_window < 20:
            status = 'Immediate Evacuation'
        elif evacuation_window < 60:
            status = 'Urgent Evacuation'
        elif evacuation_window < 120:
            status = 'Prepare Evacuation'
        else:
            status = 'Monitor'
        
        return {
            'evacuation_window_min': round(evacuation_window, 1),
            'preparation_time_min': round(preparation_time, 1),
            'status': status,
            'flood_arrival_min': round(flood_arrival_min, 1)
        }
    
    def generate_evacuation_plan(
        self,
        village_analysis: pd.DataFrame
    ) -> pd.DataFrame:
        """
        Generate evacuation plan for all villages.
        
        Args:
            village_analysis: DataFrame from village analysis
        
        Returns:
            DataFrame with evacuation recommendations
        """
        evacuation_data = []
        
        for _, row in village_analysis.iterrows():
            arrival_str = row['Flood Arrival (min)']
            
            if arrival_str == 'N/A':
                arrival_min = float('inf')
            else:
                arrival_min = float(arrival_str)
            
            evac_info = self.calculate_evacuation_window(arrival_min)
            
            evacuation_data.append({
                'Village': row['Village'],
                'Population': row['Population'],
                'Flood Arrival': f"{arrival_min:.1f} min" if arrival_min != float('inf') else 'N/A',
                'Evacuation Window': f"{evac_info['evacuation_window_min']:.1f} min",
                'Status': evac_info['status'],
                'Priority': self._get_priority(evac_info['status'])
            })
        
        df = pd.DataFrame(evacuation_data)
        
        # Sort by priority
        priority_order = {
            'Immediate Evacuation': 1,
            'Urgent Evacuation': 2,
            'Prepare Evacuation': 3,
            'Monitor': 4,
            'Safe': 5
        }
        df['SortKey'] = df['Status'].map(priority_order)
        df = df.sort_values('SortKey')
        df = df.drop('SortKey', axis=1)
        
        return df
    
    def _get_priority(self, status: str) -> str:
        """Get priority level from status."""
        if status == 'Immediate Evacuation':
            return 'P1 - Critical'
        elif status == 'Urgent Evacuation':
            return 'P2 - High'
        elif status == 'Prepare Evacuation':
            return 'P3 - Medium'
        else:
            return 'P4 - Low'
    
    def get_immediate_actions(
        self,
        evacuation_plan: pd.DataFrame
    ) -> List[Dict]:
        """
        Get immediate evacuation actions.
        
        Args:
            evacuation_plan: DataFrame from generate_evacuation_plan
        
        Returns:
            List of immediate action dictionaries
        """
        immediate = evacuation_plan[
            evacuation_plan['Status'].isin(['Immediate Evacuation', 'Urgent Evacuation'])
        ]
        
        actions = []
        for _, row in immediate.iterrows():
            actions.append({
                'village': row['Village'],
                'population': row['Population'],
                'action': row['Status'],
                'time_window': row['Evacuation Window']
            })
        
        return actions

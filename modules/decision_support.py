"""
AI decision support module for disaster recommendations.
"""

from typing import Dict, List
from datetime import datetime


class DecisionSupport:
    """Generate AI-driven disaster recommendations."""
    
    def __init__(self):
        """Initialize decision support system."""
        pass
    
    def generate_recommendations(
        self,
        risk_index: float,
        risk_category: str,
        breach_probability: float,
        rainfall_intensity: float,
        arrival_times: List[float],
        evacuation_actions: List[Dict]
    ) -> Dict[str, List[str]]:
        """
        Generate AI-driven disaster recommendations.
        
        Args:
            risk_index: Overall risk index (0-100)
            risk_category: Risk category string
            breach_probability: Breach probability (0-1)
            rainfall_intensity: Rainfall intensity (mm/day)
            arrival_times: List of flood arrival times in minutes
            evacuation_actions: List of evacuation actions
        
        Returns:
            Dictionary with recommendation categories
        """
        recommendations = {
            'emergency_actions': [],
            'preparedness_actions': [],
            'infrastructure_warnings': [],
            'monitoring_recommendations': []
        }
        
        # Emergency actions based on risk
        if risk_index >= 80 or risk_category == "Critical":
            recommendations['emergency_actions'].extend([
                "🚨 IMMEDIATE EVACUATION REQUIRED",
                "Activate District Emergency Response Team",
                "Issue public warning through all channels",
                "Deploy rescue teams to high-risk villages",
                "Establish emergency shelters"
            ])
        elif risk_index >= 60:
            recommendations['emergency_actions'].extend([
                "Prepare for potential evacuation",
                "Alert all downstream communities",
                "Mobilize emergency response resources",
                "Coordinate with state disaster management"
            ])
        
        # Breach probability based actions
        if breach_probability > 0.7:
            recommendations['emergency_actions'].append(
                "High breach probability detected - Consider controlled lake drainage"
            )
        
        # Rainfall based actions
        if rainfall_intensity > 100:
            recommendations['emergency_actions'].append(
                "Extreme rainfall conditions - Enhanced monitoring required"
            )
        elif rainfall_intensity > 50:
            recommendations['preparedness_actions'].append(
                "Heavy rainfall expected - Prepare evacuation routes"
            )
        
        # Arrival time based actions
        min_arrival = min([t for t in arrival_times if t != float('inf')], default=float('inf'))
        if min_arrival < 60:
            recommendations['emergency_actions'].append(
                f"Flood arrival expected in {min_arrival:.0f} minutes - Immediate action required"
            )
        elif min_arrival < 120:
            recommendations['preparedness_actions'].append(
                f"Flood arrival in {min_arrival:.0f} minutes - Begin evacuation preparations"
            )
        
        # Evacuation actions
        if evacuation_actions:
            immediate_count = sum(1 for a in evacuation_actions if 'Immediate' in a.get('action', ''))
            if immediate_count > 0:
                recommendations['emergency_actions'].append(
                    f"{immediate_count} villages require immediate evacuation"
                )
        
        # Preparedness actions
        recommendations['preparedness_actions'].extend([
            "Review and update evacuation plans",
            "Check communication systems",
            "Stock emergency supplies",
            "Coordinate with neighboring districts"
        ])
        
        # Infrastructure warnings
        if risk_index >= 60:
            recommendations['infrastructure_warnings'].extend([
                "⚠️ Hydropower plants downstream at risk",
                "⚠️ Bridges and roads may be damaged",
                "⚠️ Communication infrastructure vulnerable"
            ])
        
        # Monitoring recommendations
        recommendations['monitoring_recommendations'].extend([
            "Continue real-time rainfall monitoring",
            "Monitor lake level changes via satellite",
            "Track temperature anomalies",
            "Update risk assessment every 10 minutes"
        ])
        
        if breach_probability > 0.5:
            recommendations['monitoring_recommendations'].append(
                "Consider deploying field sensors near lake"
            )
        
        return recommendations
    
    def format_recommendations(
        self,
        recommendations: Dict[str, List[str]]
    ) -> str:
        """
        Format recommendations for display.
        
        Args:
            recommendations: Dictionary of recommendations
        
        Returns:
            Formatted string
        """
        output = []
        
        if recommendations['emergency_actions']:
            output.append("## 🚨 EMERGENCY ACTIONS")
            for action in recommendations['emergency_actions']:
                output.append(f"- {action}")
            output.append("")
        
        if recommendations['preparedness_actions']:
            output.append("## 📋 PREPAREDNESS ACTIONS")
            for action in recommendations['preparedness_actions']:
                output.append(f"- {action}")
            output.append("")
        
        if recommendations['infrastructure_warnings']:
            output.append("## ⚠️ INFRASTRUCTURE WARNINGS")
            for warning in recommendations['infrastructure_warnings']:
                output.append(f"- {warning}")
            output.append("")
        
        if recommendations['monitoring_recommendations']:
            output.append("## 📊 MONITORING RECOMMENDATIONS")
            for rec in recommendations['monitoring_recommendations']:
                output.append(f"- {rec}")
        
        return "\n".join(output)

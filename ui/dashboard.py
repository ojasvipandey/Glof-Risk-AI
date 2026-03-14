"""
Main dashboard UI components.
"""

import streamlit as st
import pandas as pd
from typing import Dict, List
from modules.flood_models import FloodModels
from utils.helpers import format_large_number


def render_physics_results(flood_params: Dict):
    """
    Render physics-based flood model results.
    
    Args:
        flood_params: Dictionary with flood parameters
    """
    st.subheader("🔬 Physics-Based Flood Models")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        energy = flood_params.get('energy_release_joules', 0)
        st.metric(
            "Energy Release",
            format_large_number(energy) + " J"
        )
    
    with col2:
        discharge = flood_params.get('peak_discharge_m3s', 0)
        st.metric(
            "Peak Discharge",
            f"{discharge:,.0f} m³/s"
        )
    
    with col3:
        velocity = flood_params.get('flood_velocity_ms', 0)
        st.metric(
            "Flood Velocity",
            f"{velocity:.2f} m/s"
        )
    
    # Additional details
    with st.expander("View Detailed Parameters"):
        st.write(f"**Elevation Drop:** {flood_params.get('elevation_drop_m', 0):.0f} m")
        st.write(f"**Terrain Slope:** {flood_params.get('terrain_slope_deg', 0):.1f}°")


def render_village_table(village_analysis: pd.DataFrame):
    """
    Render village exposure analysis table.
    
    Args:
        village_analysis: DataFrame with village analysis
    """
    st.subheader("🏘️ Village Exposure Analysis")
    
    if len(village_analysis) == 0:
        st.info("No villages found in flood path.")
        return
    
    # Color code by risk level
    def color_risk(val):
        color_map = {
            'Low': 'background-color: lightgreen',
            'Medium': 'background-color: yellow',
            'High': 'background-color: orange',
            'Critical': 'background-color: red; color: white'
        }
        return color_map.get(val, '')
    
    # Display table
    display_cols = ['Village', 'Population', 'Distance (km)', 'Flood Arrival (min)', 'Risk Level']
    available_cols = [col for col in display_cols if col in village_analysis.columns]
    
    styled_df = village_analysis[available_cols].style.applymap(
        color_risk, subset=['Risk Level']
    )
    
    st.dataframe(styled_df, use_container_width=True, hide_index=True)


def render_evacuation_table(evacuation_plan: pd.DataFrame):
    """
    Render evacuation plan table.
    
    Args:
        evacuation_plan: DataFrame with evacuation plan
    """
    st.subheader("🚨 Evacuation Plan")
    
    if len(evacuation_plan) == 0:
        st.info("No evacuation plan available.")
        return
    
    # Color code by status
    def color_status(val):
        color_map = {
            'Immediate Evacuation': 'background-color: darkred; color: white',
            'Urgent Evacuation': 'background-color: red; color: white',
            'Prepare Evacuation': 'background-color: orange',
            'Monitor': 'background-color: lightblue',
            'Safe': 'background-color: lightgreen'
        }
        return color_map.get(val, '')
    
    styled_df = evacuation_plan.style.applymap(
        color_status, subset=['Status']
    )
    
    st.dataframe(styled_df, use_container_width=True, hide_index=True)

"""
Real-time monitoring panel UI component.
"""

import streamlit as st
import plotly.graph_objects as go
from typing import Dict
from datetime import datetime


def render_monitoring_panel(env_indicators: Dict):
    """
    Render real-time monitoring panel.
    
    Args:
        env_indicators: Dictionary with environmental indicators
    """
    st.subheader("🌡️ Real-Time Environmental Monitoring")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(
            "Current Rainfall",
            f"{env_indicators['current_rainfall_mm']:.1f} mm/day",
            delta=f"{env_indicators['rainfall_intensity']}"
        )
    
    with col2:
        st.metric(
            "7-Day Avg Rainfall",
            f"{env_indicators['avg_rainfall_7d_mm']:.1f} mm/day"
        )
    
    with col3:
        temp_anomaly = env_indicators.get('temperature_anomaly_c', 0.0)
        st.metric(
            "Temperature Anomaly",
            f"{temp_anomaly:.1f} °C",
            delta=f"{'High' if temp_anomaly > 2 else 'Normal'}"
        )
    
    # Rainfall intensity indicator
    rainfall = env_indicators['current_rainfall_mm']
    intensity = env_indicators['rainfall_intensity']
    
    st.write("**Rainfall Intensity Level:**")
    intensity_levels = {
        'Light': (0, 10, 'green'),
        'Moderate': (10, 25, 'blue'),
        'Heavy': (25, 50, 'orange'),
        'Very Heavy': (50, 100, 'red'),
        'Extreme': (100, 200, 'darkred')
    }
    
    for level, (min_val, max_val, color) in intensity_levels.items():
        if min_val <= rainfall < max_val or (level == 'Extreme' and rainfall >= max_val):
            st.markdown(f"<div style='background-color: {color}; color: white; padding: 10px; border-radius: 5px;'>{level}</div>", unsafe_allow_html=True)
            break
    
    # Last updated
    last_updated = env_indicators.get('last_updated', datetime.now().isoformat())
    st.caption(f"Last updated: {last_updated}")

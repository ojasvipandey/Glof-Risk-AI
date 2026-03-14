"""
AI Disaster Advisor panel UI component.
"""

import streamlit as st
from typing import Dict


def render_advisor_panel(recommendations: Dict[str, list]):
    """
    Render AI disaster advisor panel.
    
    Args:
        recommendations: Dictionary with recommendation categories
    """
    st.subheader("🤖 AI Disaster Advisor")
    
    # Emergency actions
    if recommendations.get('emergency_actions'):
        st.markdown("### 🚨 Emergency Actions")
        for action in recommendations['emergency_actions']:
            st.warning(action)
    
    # Preparedness actions
    if recommendations.get('preparedness_actions'):
        st.markdown("### 📋 Preparedness Actions")
        for action in recommendations['preparedness_actions']:
            st.info(action)
    
    # Infrastructure warnings
    if recommendations.get('infrastructure_warnings'):
        st.markdown("### ⚠️ Infrastructure Warnings")
        for warning in recommendations['infrastructure_warnings']:
            st.error(warning)
    
    # Monitoring recommendations
    if recommendations.get('monitoring_recommendations'):
        st.markdown("### 📊 Monitoring Recommendations")
        for rec in recommendations['monitoring_recommendations']:
            st.success(rec)

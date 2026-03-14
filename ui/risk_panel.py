"""
Risk assessment panel UI component.
"""

import streamlit as st
import plotly.graph_objects as go
from typing import Dict


def render_risk_panel(risk_results: Dict):
    """
    Render risk assessment panel.
    
    Args:
        risk_results: Dictionary with risk calculation results
    """
    st.subheader("⚠️ Risk Assessment")
    
    risk_index = risk_results['risk_index']
    risk_category = risk_results['risk_category']
    
    # Risk gauge
    fig = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=risk_index,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "Risk Index"},
        delta={'reference': 50},
        gauge={
            'axis': {'range': [None, 100]},
            'bar': {'color': "darkblue"},
            'steps': [
                {'range': [0, 30], 'color': "lightgreen"},
                {'range': [30, 60], 'color': "yellow"},
                {'range': [60, 80], 'color': "orange"},
                {'range': [80, 100], 'color': "red"}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': 80
            }
        }
    ))
    
    fig.update_layout(height=300)
    st.plotly_chart(fig, use_container_width=True)
    
    # Risk category badge
    color_map = {
        'Low': 'green',
        'Medium': 'yellow',
        'High': 'orange',
        'Critical': 'red'
    }
    color = color_map.get(risk_category, 'gray')
    
    st.markdown(
        f"<h3 style='text-align: center; color: {color};'>{risk_category} Risk</h3>",
        unsafe_allow_html=True
    )
    
    # Risk components
    st.write("**Risk Components:**")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Hazard", f"{risk_results['hazard_score']:.1f}")
    
    with col2:
        st.metric("Exposure", f"{risk_results['exposure_score']:.1f}")
    
    with col3:
        st.metric("Vulnerability", f"{risk_results['vulnerability_score']:.1f}")
    
    with col4:
        st.metric("Response Capacity", f"{risk_results['response_capacity_score']:.1f}")
    
    # Risk breakdown chart
    components = ['Hazard', 'Exposure', 'Vulnerability']
    values = [
        risk_results['hazard_score'],
        risk_results['exposure_score'],
        risk_results['vulnerability_score']
    ]
    
    fig_bar = go.Figure(data=[
        go.Bar(x=components, y=values, marker_color=['red', 'orange', 'yellow'])
    ])
    fig_bar.update_layout(
        title="Risk Component Breakdown",
        yaxis_title="Score (0-100)",
        height=300
    )
    st.plotly_chart(fig_bar, use_container_width=True)

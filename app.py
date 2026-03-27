"""
GLOF-RISK AI - Main Streamlit Application
An AI-Powered Glacial Lake Outburst Flood Risk Intelligence Platform
"""

import streamlit as st
import pandas as pd
import numpy as np
from typing import Dict, List, Optional

# Import modules
from modules.data_loader import DataLoader
from modules.rainfall_monitor import RainfallMonitor
from modules.geospatial_analysis import GeospatialAnalysis
from modules.flood_models import FloodModels
from modules.flood_simulation import FloodSimulation
from modules.ml_model import BreachPredictionModel
from modules.risk_model import RiskModel
from modules.village_analysis import VillageAnalysis
from modules.evacuation_planner import EvacuationPlanner
from modules.decision_support import DecisionSupport

# Import UI components
from ui.dashboard import render_physics_results, render_village_table, render_evacuation_table
from ui.monitoring_panel import render_monitoring_panel
from ui.risk_panel import render_risk_panel
from ui.advisor_panel import render_advisor_panel
from ui.map_visualization import MapVisualization

# Import utilities
from utils.config import DEFAULT_RAINFALL, DEFAULT_TEMPERATURE_ANOMALY
from utils.helpers import calculate_distance

# Page configuration
st.set_page_config(
    page_title="GLOF-RISK AI",
    page_icon="🌊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state
if 'ml_model' not in st.session_state:
    st.session_state.ml_model = None
if 'data_loader' not in st.session_state:
    st.session_state.data_loader = DataLoader()

# Initialize components
@st.cache_resource
def load_ml_model():
    """Load ML model (cached)."""
    return BreachPredictionModel()

# Load ML model
if st.session_state.ml_model is None:
    with st.spinner("Loading AI models..."):
        st.session_state.ml_model = load_ml_model()

# Header
st.title("🌊 GLOF-RISK AI")
st.markdown("### District-Level Glacial Lake Outburst Flood Risk Intelligence System")
st.markdown("---")

# Sidebar inputs
st.sidebar.header("⚙️ Configuration")

# Load data
data_loader = st.session_state.data_loader
lakes_df = data_loader.load_glacial_lakes()
population_df = data_loader.load_population_data()

# Lake selection
if len(lakes_df) > 0:
    lake_names = lakes_df['lake_name'].tolist()
    selected_lake_name = st.sidebar.selectbox(
        "Select Glacial Lake",
        lake_names,
        index=0 if 'South Lhonak Lake' in lake_names else 0
    )
    lake_data = data_loader.get_lake_by_name(selected_lake_name)
else:
    st.sidebar.error("No glacial lake data available. Please check data files.")
    st.stop()

# District selection
districts = population_df['district'].unique().tolist() if len(population_df) > 0 else ['Sikkim']
selected_district = st.sidebar.selectbox(
    "Select District",
    districts,
    index=0
)

# Rainfall input (force all args to float to avoid MixedNumericTypes)
rainfall_intensity = st.sidebar.number_input(
    "Rainfall Intensity (mm/day)",
    min_value=float(0.0),
    max_value=float(500.0),
    value=float(DEFAULT_RAINFALL),
    step=float(5.0),
)

# Temperature anomaly (also ensure pure float types)
temperature_anomaly = st.sidebar.number_input(
    "Temperature Anomaly (°C)",
    min_value=float(-5.0),
    max_value=float(10.0),
    value=float(DEFAULT_TEMPERATURE_ANOMALY),
    step=float(0.5),
)
# Calculate button
calculate_button = st.sidebar.button("🚀 Calculate Risk", type="primary", use_container_width=True)

# Main content
if lake_data:
    # Initialize monitoring
    rainfall_monitor = RainfallMonitor(data_loader)
    env_indicators = rainfall_monitor.get_environmental_indicators(
        selected_district, temperature_anomaly
    )
    
    # Update rainfall in indicators
    env_indicators['current_rainfall_mm'] = rainfall_intensity
    env_indicators['rainfall_intensity'] = rainfall_monitor.calculate_rainfall_intensity_level(rainfall_intensity)
    
    # Display monitoring panel
    render_monitoring_panel(env_indicators)
    
    st.markdown("---")
    
    if calculate_button or 'results_calculated' in st.session_state:
        # Mark as calculated
        st.session_state.results_calculated = True
        
        with st.spinner("🔄 Calculating risk assessment..."):
            # Get villages in district
            villages_list = data_loader.get_villages_in_district(selected_district)
            villages_dict = villages_list.to_dict('records') if len(villages_list) > 0 else []
            
            # Lake elevation used in multiple downstream calculations
            lake_elevation = float(lake_data.get('elevation', 4000))

            # Add elevation estimates if missing
            for village in villages_dict:
                if 'elevation' not in village or pd.isna(village.get('elevation')):
                    village['elevation'] = lake_elevation - 500  # Rough estimate
            
            # Geospatial analysis
            geo_analysis = GeospatialAnalysis()
            
            # Calculate terrain slope (simplified - using average)
            avg_slope = 15.0  # Default slope
            
            # ML breach prediction
            ml_model = st.session_state.ml_model
            breach_probability = ml_model.predict_breach_probability(
                lake_area=lake_data.get('lake_area', 1.0),
                lake_volume=lake_data.get('lake_volume', 10.0),
                dam_type=lake_data.get('dam_type', 'moraine'),
                rainfall_intensity=rainfall_intensity,
                terrain_slope=avg_slope,
                temperature_anomaly=temperature_anomaly
            )
            
            # Physics-based flood models
            flood_models = FloodModels()
            
            # Estimate elevation drop
            if villages_dict:
                first_village = villages_dict[0]
                distance = calculate_distance(
                    lake_data['latitude'], lake_data['longitude'],
                    first_village['latitude'], first_village['longitude']
                )
                elevation_drop = geo_analysis.estimate_elevation_drop(
                    lake_elevation, distance, avg_slope
                )
            else:
                elevation_drop = 500  # Default
            
            flood_params = flood_models.calculate_flood_parameters(
                lake_volume=lake_data.get('lake_volume', 10.0),
                elevation_drop=elevation_drop,
                terrain_slope=avg_slope
            )
            
            # Flood simulation
            flood_sim = FloodSimulation()
            simulation_results = flood_sim.simulate_flood_propagation(
                lake_data, villages_dict, flood_params
            )
            
            # Risk calculation
            risk_model = RiskModel()
            
            # Calculate hazard score
            hazard_score = risk_model.calculate_hazard_score(
                breach_probability=breach_probability,
                rainfall_intensity=rainfall_intensity,
                lake_growth_rate=0.0
            )
            
            # Calculate exposure score
            total_population = int(villages_list['population'].sum()) if len(villages_list) > 0 else 0
            infrastructure_df = data_loader.load_infrastructure_data()
            infrastructure_count = len(infrastructure_df[infrastructure_df['district'] == selected_district]) if len(infrastructure_df) > 0 else 0
            
            exposure_score = risk_model.calculate_exposure_score(
                population_exposed=total_population,
                infrastructure_count=infrastructure_count
            )
            
            # Calculate vulnerability score
            vulnerability_score = risk_model.calculate_vulnerability_score(
                terrain_slope=avg_slope,
                building_resilience=0.5
            )
            
            # Calculate response capacity
            response_capacity_score = risk_model.calculate_response_capacity_score(
                evacuation_routes=2,
                warning_systems=True
            )
            
            # Calculate overall risk
            risk_results = risk_model.calculate_risk_index(
                hazard_score=hazard_score,
                exposure_score=exposure_score,
                vulnerability_score=vulnerability_score,
                response_capacity_score=response_capacity_score
            )
            
            # Village analysis
            village_analyzer = VillageAnalysis()
            village_analysis_df = village_analyzer.analyze_village_exposure(
                lake_data, villages_dict, flood_params, risk_results['risk_index']
            )
            
            # Evacuation planning
            evacuation_planner = EvacuationPlanner()
            evacuation_plan_df = evacuation_planner.generate_evacuation_plan(village_analysis_df)
            immediate_actions = evacuation_planner.get_immediate_actions(evacuation_plan_df)
            
            # Decision support
            decision_support = DecisionSupport()
            arrival_times = [r.get('arrival_time_min', float('inf')) for r in simulation_results]
            recommendations = decision_support.generate_recommendations(
                risk_index=risk_results['risk_index'],
                risk_category=risk_results['risk_category'],
                breach_probability=breach_probability,
                rainfall_intensity=rainfall_intensity,
                arrival_times=arrival_times,
                evacuation_actions=immediate_actions
            )
            
            # Display results
            col1, col2 = st.columns([2, 1])
            
            with col1:
                # Physics results
                render_physics_results(flood_params)
                
                st.markdown("---")
                
                # Risk panel
                render_risk_panel(risk_results)
                
                st.markdown("---")
                
                # Village analysis
                render_village_table(village_analysis_df)
                
                st.markdown("---")
                
                # Evacuation plan
                render_evacuation_table(evacuation_plan_df)
            
            with col2:
                # Breach probability
                st.metric(
                    "Breach Probability",
                    f"{breach_probability*100:.1f}%",
                    delta=f"{'High' if breach_probability > 0.5 else 'Low'} Risk"
                )
                
                st.markdown("---")
                
                # AI Advisor
                render_advisor_panel(recommendations)
            
            # Map visualization
            st.markdown("---")
            st.subheader("🗺️ Interactive Map")
            
            if len(village_analysis_df) > 0:
                # Prepare map data
                map_viz = MapVisualization(
                    center_lat=lake_data['latitude'],
                    center_lon=lake_data['longitude'],
                    zoom=10
                )
                
                # Get flood path coordinates
                path_coords = flood_sim.calculate_flood_path_coordinates(
                    lake_data['latitude'],
                    lake_data['longitude'],
                    villages_dict
                )
                
                # Get flood zones
                flood_zones = flood_sim.generate_flood_zones(simulation_results)
                
                # Create map
                map_obj = map_viz.create_complete_map(
                    lake_data=lake_data,
                    villages=village_analysis_df,
                    path_coordinates=path_coords,
                    risk_level=risk_results['risk_category'],
                    flood_zones=flood_zones
                )
                
                # Display map - save to HTML and render (cloud-compatible)
                import os
                import tempfile
                
                # Use tempfile for better cloud compatibility
                with tempfile.NamedTemporaryFile(delete=False, suffix='.html', mode='w', encoding='utf-8') as tmp_file:
                    map_obj.save(tmp_file.name)
                    tmp_path = tmp_file.name
                
                with open(tmp_path, 'r', encoding='utf-8') as f:
                    html_map = f.read()
                
                # Clean up temp file
                try:
                    if os.path.exists(tmp_path):
                        os.remove(tmp_path)
                except:
                    pass  # Ignore cleanup errors
                
                st.components.v1.html(html_map, height=600, scrolling=True)
            else:
                st.info("No villages found for map visualization.")
    
    else:
        st.info("👈 Configure parameters in the sidebar and click 'Calculate Risk' to begin analysis.")
        
        # Show lake information
        st.subheader("📊 Selected Lake Information")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Lake Area", f"{lake_data.get('lake_area', 'N/A')} km²")
            st.metric("Lake Volume", f"{lake_data.get('lake_volume', 'N/A')} million m³")
        
        with col2:
            st.metric("Elevation", f"{lake_data.get('elevation', 'N/A')} m")
            st.metric("Dam Type", lake_data.get('dam_type', 'N/A'))
        
        with col3:
            st.metric("Latitude", f"{lake_data.get('latitude', 'N/A'):.4f}°")
            st.metric("Longitude", f"{lake_data.get('longitude', 'N/A'):.4f}°")

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: gray;'>
    <p>GLOF-RISK AI - Glacial Lake Outburst Flood Risk Intelligence Platform</p>
    <p>Built for District Disaster Management Authorities</p>
    </div>
    """,
    unsafe_allow_html=True
)

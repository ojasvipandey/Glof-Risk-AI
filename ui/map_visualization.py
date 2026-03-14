"""
Map visualization module using Folium.
"""

import folium
from folium import plugins
from typing import List, Dict, Tuple, Optional
import pandas as pd


class MapVisualization:
    """Create interactive maps for GLOF risk visualization."""
    
    def __init__(self, center_lat: float = 27.8, center_lon: float = 88.6, zoom: int = 10):
        """
        Initialize map visualization.
        
        Args:
            center_lat: Center latitude
            center_lon: Center longitude
            zoom: Initial zoom level
        """
        self.center_lat = center_lat
        self.center_lon = center_lon
        self.zoom = zoom
    
    def create_base_map(self) -> folium.Map:
        """
        Create base map.
        
        Returns:
            Folium map object
        """
        m = folium.Map(
            location=[self.center_lat, self.center_lon],
            zoom_start=self.zoom,
            tiles='OpenStreetMap'
        )
        
        # Add satellite tile layer
        folium.TileLayer(
            tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
            attr='Esri',
            name='Satellite',
            overlay=False,
            control=True
        ).add_to(m)
        
        return m
    
    def add_glacial_lake(
        self,
        map_obj: folium.Map,
        lake_data: Dict,
        risk_level: str = "Medium"
    ):
        """
        Add glacial lake marker to map.
        
        Args:
            map_obj: Folium map object
            lake_data: Dictionary with lake information
            risk_level: Risk level (Low, Medium, High, Critical)
        """
        lat = lake_data['latitude']
        lon = lake_data['longitude']
        name = lake_data.get('lake_name', 'Unknown Lake')
        
        # Color based on risk
        color_map = {
            'Low': 'green',
            'Medium': 'yellow',
            'High': 'orange',
            'Critical': 'red'
        }
        color = color_map.get(risk_level, 'blue')
        
        # Create popup
        popup_html = f"""
        <b>{name}</b><br>
        Area: {lake_data.get('lake_area', 'N/A')} km²<br>
        Volume: {lake_data.get('lake_volume', 'N/A')} million m³<br>
        Elevation: {lake_data.get('elevation', 'N/A')} m<br>
        Risk: {risk_level}
        """
        
        folium.Marker(
            location=[lat, lon],
            popup=folium.Popup(popup_html, max_width=300),
            icon=folium.Icon(color=color, icon='tint', prefix='fa'),
            tooltip=name
        ).add_to(map_obj)
        
        # Add circle for lake area
        folium.Circle(
            location=[lat, lon],
            radius=lake_data.get('lake_area', 1) * 1000,  # Convert km² to meters
            popup=f"Lake Area: {lake_data.get('lake_area', 'N/A')} km²",
            color=color,
            fill=True,
            fillOpacity=0.2
        ).add_to(map_obj)
    
    def add_flood_path(
        self,
        map_obj: folium.Map,
        path_coordinates: List[Tuple[float, float]],
        color: str = 'red'
    ):
        """
        Add flood path to map.
        
        Args:
            map_obj: Folium map object
            path_coordinates: List of (lat, lon) tuples
            color: Path color
        """
        folium.PolyLine(
            locations=path_coordinates,
            color=color,
            weight=4,
            opacity=0.7,
            popup='Flood Propagation Path'
        ).add_to(map_obj)
    
    def add_villages(
        self,
        map_obj: folium.Map,
        villages: pd.DataFrame,
        risk_col: str = 'Risk Level'
    ):
        """
        Add village markers to map.
        
        Args:
            map_obj: Folium map object
            villages: DataFrame with village data
            risk_col: Column name for risk level
        """
        color_map = {
            'Low': 'green',
            'Medium': 'yellow',
            'High': 'orange',
            'Critical': 'red'
        }
        
        for _, row in villages.iterrows():
            lat = row['Latitude']
            lon = row['Longitude']
            name = row.get('Village', 'Unknown')
            risk = row.get(risk_col, 'Medium')
            population = row.get('Population', 0)
            arrival = row.get('Flood Arrival (min)', 'N/A')
            
            color = color_map.get(risk, 'blue')
            
            popup_html = f"""
            <b>{name}</b><br>
            Population: {population}<br>
            Risk: {risk}<br>
            Flood Arrival: {arrival} min
            """
            
            folium.Marker(
                location=[lat, lon],
                popup=folium.Popup(popup_html, max_width=300),
                icon=folium.Icon(color=color, icon='home', prefix='fa'),
                tooltip=f"{name} ({risk})"
            ).add_to(map_obj)
    
    def add_flood_zones(
        self,
        map_obj: folium.Map,
        flood_zones: Dict[str, List[Dict]]
    ):
        """
        Add flood zones to map.
        
        Args:
            map_obj: Folium map object
            flood_zones: Dictionary with flood zones by severity
        """
        zone_colors = {
            'severe': 'red',
            'moderate': 'orange',
            'mild': 'yellow'
        }
        
        for severity, zones in flood_zones.items():
            color = zone_colors.get(severity, 'gray')
            for zone in zones:
                folium.Circle(
                    location=[zone['latitude'], zone['longitude']],
                    radius=zone.get('inundation_width_m', 100),
                    popup=f"Flood Zone: {severity}",
                    color=color,
                    fill=True,
                    fillOpacity=0.3
                ).add_to(map_obj)
    
    def create_complete_map(
        self,
        lake_data: Dict,
        villages: pd.DataFrame,
        path_coordinates: List[Tuple[float, float]],
        risk_level: str = "Medium",
        flood_zones: Optional[Dict] = None
    ) -> folium.Map:
        """
        Create complete map with all elements.
        
        Args:
            lake_data: Lake data dictionary
            villages: Village DataFrame
            path_coordinates: Flood path coordinates
            risk_level: Risk level
            flood_zones: Flood zones dictionary
        
        Returns:
            Complete Folium map
        """
        # Set center to lake location
        self.center_lat = lake_data['latitude']
        self.center_lon = lake_data['longitude']
        
        m = self.create_base_map()
        
        # Add elements
        self.add_glacial_lake(m, lake_data, risk_level)
        self.add_flood_path(m, path_coordinates)
        self.add_villages(m, villages)
        
        if flood_zones:
            self.add_flood_zones(m, flood_zones)
        
        # Add layer control
        folium.LayerControl().add_to(m)
        
        return m

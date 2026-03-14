# GLOF-RISK AI

**An AI-Powered Glacial Lake Outburst Flood Risk Intelligence Platform**

A district-level disaster intelligence system that predicts and monitors Glacial Lake Outburst Flood (GLOF) risks in the Himalayan region. The platform combines hydrological physics models, geospatial analysis, machine learning, real-time environmental monitoring, and decision-support systems to help disaster authorities assess flood risk and plan evacuation actions.

## 🌊 Features

### Core Capabilities

1. **Data Ingestion** - Load and manage glacial lake, rainfall, population, and infrastructure data
2. **Geospatial Processing** - Analyze terrain, river paths, and downstream settlements
3. **Hydrological Modeling** - Physics-based flood models (energy release, peak discharge, velocity)
4. **Machine Learning Prediction** - Random Forest model for breach probability prediction
5. **Flood Simulation** - 1-D flood routing and propagation simulation
6. **Real-Time Monitoring** - Environmental indicators and rainfall trends
7. **Risk Scoring** - Comprehensive risk index calculation (Hazard × Exposure × Vulnerability)
8. **Village Exposure Analysis** - Identify and analyze at-risk villages
9. **Evacuation Planning** - Generate evacuation time windows and recommendations
10. **AI Decision Support** - Actionable disaster management recommendations

## 🏗️ System Architecture

```
glof-risk-ai/
├── data/                    # Data files (CSV)
│   ├── glacial_lakes.csv
│   ├── rainfall_data.csv
│   ├── population_data.csv
│   └── infrastructure_data.csv
├── models/                  # Trained ML models
│   └── breach_model.pkl
├── modules/                 # Core modules
│   ├── data_loader.py
│   ├── rainfall_monitor.py
│   ├── geospatial_analysis.py
│   ├── flood_models.py
│   ├── flood_simulation.py
│   ├── ml_model.py
│   ├── risk_model.py
│   ├── village_analysis.py
│   ├── evacuation_planner.py
│   └── decision_support.py
├── ui/                      # UI components
│   ├── dashboard.py
│   ├── map_visualization.py
│   ├── monitoring_panel.py
│   ├── risk_panel.py
│   └── advisor_panel.py
├── utils/                   # Utilities
│   ├── config.py
│   └── helpers.py
├── app.py                   # Main Streamlit application
├── requirements.txt
└── README.md
```

## 📊 Physics-Based Models

### Energy Release Model
Calculates potential energy stored in glacial lake:
```
E = ρ × g × V × h
```
Where:
- ρ = 1000 kg/m³ (water density)
- g = 9.81 m/s² (gravity)
- V = lake volume (m³)
- h = elevation difference (m)

### Peak Discharge Model
Empirical relation for Himalayan GLOFs:
```
Q_peak = k × V^0.67
```
Where k = 0.75 (empirical constant)

### Flood Velocity Model
Manning equation:
```
V = (1/n) × R^(2/3) × S^(1/2)
```

## 🤖 Machine Learning Model

**Random Forest Classifier** for breach probability prediction

**Features:**
- Lake area (km²)
- Lake volume (million m³)
- Dam type (moraine/ice/bedrock)
- Rainfall intensity (mm/day)
- Terrain slope (degrees)
- Temperature anomaly (°C)

**Output:** Breach probability (0-1)

## 📈 Risk Index Model

**Formula:**
```
Risk = (Hazard × Exposure × Vulnerability) / ResponseCapacity
```

**Components:**
- **Hazard Score** (0-100): Based on breach probability, rainfall intensity, lake growth rate
- **Exposure Score** (0-100): Based on population and infrastructure at risk
- **Vulnerability Score** (0-100): Based on terrain slope and building resilience
- **Response Capacity Score** (0-100): Based on evacuation routes and warning systems

**Risk Classification:**
- 0-30: **Low**
- 30-60: **Medium**
- 60-80: **High**
- 80-100: **Critical**

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Steps

1. **Clone or download the repository**
   ```bash
   cd "GLOF RISK AI"
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

4. **Access the application**
   - Open your browser to `http://localhost:8501`

## 📝 Usage

1. **Select Glacial Lake** - Choose from available glacial lakes in the sidebar
2. **Select District** - Choose the district for analysis
3. **Configure Parameters**:
   - Rainfall intensity (mm/day)
   - Temperature anomaly (°C)
4. **Calculate Risk** - Click the "Calculate Risk" button
5. **Review Results**:
   - Physics-based flood parameters
   - Risk assessment with gauge visualization
   - Village exposure analysis
   - Evacuation plan
   - AI disaster advisor recommendations
   - Interactive map with flood path

## 📊 Data Sources

The system integrates open datasets:

- **Glacial Lake Inventory**: ISRO Bhuvan / NRSC
- **Rainfall Data**: Indian Meteorological Department
- **DEM Elevation Data**: NASA SRTM DEM
- **Population Data**: Census of India
- **Infrastructure Data**: OpenStreetMap

## 🗺️ Map Visualization

Interactive maps display:
- Glacial lake location (color-coded by risk)
- Flood propagation path
- At-risk villages (color-coded by risk level)
- Flood zones (severe/moderate/mild)

## ⚙️ Configuration

Edit `utils/config.py` to customize:
- Physical constants
- Risk calculation weights
- Risk thresholds
- Monitoring intervals

## 🚢 Deployment

### Streamlit Cloud

1. **Push to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin <your-repo-url>
   git push -u origin main
   ```

2. **Deploy on Streamlit Cloud**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Sign in with GitHub
   - Click "New app"
   - Select repository and branch
   - Set main file path: `app.py`
   - Click "Deploy"

### Local Deployment

For production deployment, consider:
- Using a reverse proxy (nginx)
- Setting up SSL certificates
- Configuring environment variables
- Using a process manager (systemd, supervisor)

## 🔧 Performance

- **Response Time**: < 5 seconds per query
- **System Requirements**: CPU-based (no GPU required)
- **Scalability**: Handles multiple concurrent users

## 📚 Documentation

### Module Documentation

- **data_loader.py**: Loads and manages all data sources
- **flood_models.py**: Physics-based flood calculations
- **ml_model.py**: Machine learning breach prediction
- **risk_model.py**: Risk index calculation
- **flood_simulation.py**: Flood propagation simulation
- **village_analysis.py**: Village exposure analysis
- **evacuation_planner.py**: Evacuation time window calculation
- **decision_support.py**: AI-driven recommendations

## 🛠️ Development

### Adding New Features

1. Create new module in `modules/` directory
2. Add UI component in `ui/` directory if needed
3. Integrate into `app.py`
4. Update `requirements.txt` if new dependencies needed

### Testing

Run the application locally and test with:
- Different glacial lakes
- Various rainfall intensities
- Different districts
- Edge cases (no villages, extreme values)

## 📄 License

This project is designed for disaster management and research purposes.

## 👥 Target Users

- **Primary**: District Disaster Management Authorities (DDMA)
- **Secondary**: 
  - NDMA planners
  - Hydropower plant operators
  - Climate researchers
  - Disaster response agencies

## 🎯 Future Enhancements

- Real-time satellite data integration
- Advanced 2D flood routing models
- Historical GLOF event database
- Multi-lake risk assessment
- Automated alert system
- Mobile app integration

## 📞 Support

For issues, questions, or contributions, please refer to the project documentation or contact the development team.

---

**Built with ❤️ for Disaster Risk Reduction**

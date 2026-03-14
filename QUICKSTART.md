# Quick Start Guide

## Installation

1. **Install Python 3.8+** (if not already installed)

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   streamlit run app.py
   ```

4. **Open your browser** to `http://localhost:8501`

## First Use

1. **Select a Glacial Lake** from the sidebar dropdown
2. **Select a District** for analysis
3. **Set Rainfall Intensity** (default: 50 mm/day)
4. **Set Temperature Anomaly** (default: 0.0 °C)
5. **Click "Calculate Risk"** button

## Understanding the Results

### Monitoring Panel
- Current rainfall and intensity level
- 7-day average rainfall
- Temperature anomaly

### Physics Results
- **Energy Release**: Potential energy stored in the lake (Joules)
- **Peak Discharge**: Maximum flood discharge (m³/s)
- **Flood Velocity**: Estimated flood wave velocity (m/s)

### Risk Assessment
- **Risk Index**: Overall risk score (0-100)
- **Risk Category**: Low / Medium / High / Critical
- **Component Scores**: Hazard, Exposure, Vulnerability, Response Capacity

### Village Analysis
- List of villages in flood path
- Population at risk
- Flood arrival time
- Risk level per village

### Evacuation Plan
- Evacuation time windows
- Priority levels
- Action status

### AI Disaster Advisor
- Emergency actions
- Preparedness recommendations
- Infrastructure warnings
- Monitoring suggestions

### Interactive Map
- Glacial lake location
- Flood propagation path
- At-risk villages
- Flood zones

## Troubleshooting

### Import Errors
If you get import errors, make sure all dependencies are installed:
```bash
pip install -r requirements.txt
```

### Map Not Displaying
The map requires internet connection for tile loading. If maps don't display:
- Check internet connection
- Try refreshing the page
- Check browser console for errors

### Model Training
On first run, the ML model will train automatically using synthetic data. This may take 10-30 seconds.

### No Data Available
If you see "No data available" messages:
- Check that CSV files exist in the `data/` directory
- Verify CSV files have correct column names
- Check file encoding (should be UTF-8)

## Next Steps

- Customize data files in `data/` directory
- Adjust risk weights in `utils/config.py`
- Add more glacial lakes to `data/glacial_lakes.csv`
- Add more villages to `data/population_data.csv`

## Support

For issues or questions, refer to the main README.md file.

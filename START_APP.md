# 🚀 How to Use GLOF-RISK AI

## ⚡ Quick Start (3 Steps)

### Step 1: Open Terminal/Command Prompt
- **Windows**: Press `Win + R`, type `cmd`, press Enter
- **Mac/Linux**: Open Terminal

### Step 2: Navigate to Project Folder
```bash
cd "C:\Users\Lenovo!\Desktop\GLOF RISK AI"
```

### Step 3: Run These Commands
```bash
# Install dependencies (first time only)
pip install -r requirements.txt

# Start the application
streamlit run app.py
```

### Step 4: Open in Browser
- The app will automatically open at: **http://localhost:8501**
- If not, manually open: http://localhost:8501

---

## 🎯 Alternative: Double-Click to Run (Windows)

1. **Double-click** `RUN_LOCALLY.bat` file
2. Wait for dependencies to install (first time only)
3. Browser will open automatically

---

## 🌐 Deploy Online (Free - Streamlit Cloud)

### Quick Deployment Steps:

1. **Create GitHub Account** (if you don't have one)
   - Go to: https://github.com/signup

2. **Upload Code to GitHub**
   - Download GitHub Desktop: https://desktop.github.com/
   - Or use web interface to create repository and upload files

3. **Deploy on Streamlit Cloud**
   - Go to: https://share.streamlit.io
   - Sign in with GitHub
   - Click "New app"
   - Select your repository
   - Main file: `app.py`
   - Click "Deploy"

4. **Get Your Public Link**
   - Your app will be live at: `https://YOUR-APP-NAME.streamlit.app`
   - Share this link with anyone!

---

## 📱 Access Your App

### Local Access:
- **URL**: http://localhost:8501
- **When**: App is running on your computer
- **Who**: Only you (or others on your network)

### Online Access (Streamlit Cloud):
- **URL**: https://YOUR-APP-NAME.streamlit.app
- **When**: Always available
- **Who**: Anyone with the link (public)

---

## 🎮 How to Use the App

1. **Select Glacial Lake** from dropdown (sidebar)
2. **Select District** for analysis
3. **Set Rainfall Intensity** (mm/day)
4. **Set Temperature Anomaly** (°C)
5. **Click "Calculate Risk"** button
6. **View Results**:
   - Physics calculations
   - Risk assessment
   - Village analysis
   - Evacuation plan
   - AI recommendations
   - Interactive map

---

## 🔗 Direct Links

### Run Locally:
```
http://localhost:8501
```
(Only works when app is running)

### Deploy Online:
```
https://share.streamlit.io
```
(Free hosting platform)

### Documentation:
- Full Guide: See `README.md`
- Quick Start: See `QUICKSTART.md`
- Deployment: See `DEPLOYMENT.md`

---

## ❓ Troubleshooting

### "Python not found"
- Install Python from: https://www.python.org/downloads/
- Make sure to check "Add to PATH" during installation

### "Module not found"
- Run: `pip install -r requirements.txt`

### "Port already in use"
- Close other Streamlit apps
- Or use: `streamlit run app.py --server.port 8502`

### "Map not showing"
- Check internet connection
- Maps need online tile loading

---

## ✅ You're Ready!

**Choose your method:**
- 🏠 **Local**: Run `streamlit run app.py` (for testing)
- 🌐 **Online**: Deploy on Streamlit Cloud (for sharing)

**Need help?** Check the other documentation files in this folder!

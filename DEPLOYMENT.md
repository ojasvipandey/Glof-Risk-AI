# Deployment Guide - GLOF-RISK AI

## 🚀 Quick Start Options

### Option 1: Run Locally (Recommended for Testing)

#### Step 1: Install Python
- Download Python 3.8+ from [python.org](https://www.python.org/downloads/)
- Make sure to check "Add Python to PATH" during installation

#### Step 2: Install Dependencies
Open terminal/command prompt in the project folder and run:
```bash
pip install -r requirements.txt
```

#### Step 3: Run the Application
```bash
streamlit run app.py
```

#### Step 4: Access the Application
- The app will automatically open in your browser at: **http://localhost:8501**
- If it doesn't open automatically, copy the URL from the terminal

---

### Option 2: Deploy on Streamlit Cloud (Free & Public)

Streamlit Cloud is the easiest way to share your app online for free!

#### Prerequisites
1. GitHub account (free) - Sign up at [github.com](https://github.com)

#### Step-by-Step Deployment

**Step 1: Create GitHub Repository**
1. Go to [github.com](https://github.com) and sign in
2. Click the "+" icon → "New repository"
3. Name it: `glof-risk-ai`
4. Make it **Public** (required for free Streamlit Cloud)
5. Click "Create repository"

**Step 2: Upload Your Code to GitHub**

**Option A: Using GitHub Desktop (Easiest)**
1. Download [GitHub Desktop](https://desktop.github.com/)
2. Install and sign in
3. Click "File" → "Add Local Repository"
4. Select your project folder: `C:\Users\Lenovo!\Desktop\GLOF RISK AI`
5. Click "Publish repository"
6. Select your repository and click "Publish"

**Option B: Using Command Line**
Open PowerShell in your project folder and run:
```powershell
git init
git add .
git commit -m "Initial commit - GLOF-RISK AI"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/glof-risk-ai.git
git push -u origin main
```
(Replace `YOUR_USERNAME` with your GitHub username)

**Step 3: Deploy on Streamlit Cloud**
1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Click "Sign in" and authorize with GitHub
3. Click "New app"
4. Fill in:
   - **Repository**: Select `YOUR_USERNAME/glof-risk-ai`
   - **Branch**: `main`
   - **Main file path**: `app.py`
5. Click "Deploy"
6. Wait 2-3 minutes for deployment
7. Your app will be live at: `https://YOUR_APP_NAME.streamlit.app`

**Your app is now live and accessible worldwide!** 🌐

---

### Option 3: Run in Google Colab (Alternative)

If you want to test without installing locally:

1. Upload your project to Google Drive
2. Open [Google Colab](https://colab.research.google.com/)
3. Install Streamlit:
   ```python
   !pip install streamlit
   !pip install -r requirements.txt
   ```
4. Run:
   ```python
   !streamlit run app.py --server.port 8501 --server.address 0.0.0.0
   ```
5. Use ngrok to create public URL (requires ngrok account)

---

## 📱 Access Methods

### Local Access
- **URL**: http://localhost:8501
- **Network Access**: http://YOUR_IP:8501 (for other devices on same network)

### Streamlit Cloud Access
- **Public URL**: https://YOUR_APP_NAME.streamlit.app
- Share this link with anyone!

---

## 🔧 Troubleshooting

### Port Already in Use
If port 8501 is busy, use a different port:
```bash
streamlit run app.py --server.port 8502
```

### Dependencies Not Installing
Try upgrading pip first:
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### Module Import Errors
Make sure you're in the project root directory:
```bash
cd "C:\Users\Lenovo!\Desktop\GLOF RISK AI"
streamlit run app.py
```

### Map Not Displaying
- Check internet connection (maps need online tiles)
- Try refreshing the page
- Check browser console (F12) for errors

---

## 🌐 Sharing Your App

### Share Locally
1. Find your computer's IP address:
   ```powershell
   ipconfig
   ```
   Look for "IPv4 Address" (e.g., 192.168.1.100)

2. Run Streamlit with network access:
   ```bash
   streamlit run app.py --server.address 0.0.0.0
   ```

3. Share URL: `http://YOUR_IP:8501`
   - Others on your network can access it

### Share Publicly (Streamlit Cloud)
- Just share your Streamlit Cloud URL
- No setup needed for viewers
- Works on any device with internet

---

## 📊 Recommended Setup

**For Development/Testing:**
- Run locally using Option 1

**For Production/Sharing:**
- Deploy on Streamlit Cloud using Option 2

---

## 🎯 Quick Commands Reference

```bash
# Install dependencies
pip install -r requirements.txt

# Run locally
streamlit run app.py

# Run on specific port
streamlit run app.py --server.port 8502

# Run with network access
streamlit run app.py --server.address 0.0.0.0

# View Streamlit help
streamlit --help
```

---

## 🔗 Useful Links

- **Streamlit Documentation**: https://docs.streamlit.io
- **Streamlit Cloud**: https://share.streamlit.io
- **GitHub**: https://github.com
- **Python Downloads**: https://www.python.org/downloads/

---

## ✅ Next Steps After Deployment

1. **Test the application** with different parameters
2. **Customize data files** in `data/` folder
3. **Share the link** with your team/users
4. **Monitor usage** on Streamlit Cloud dashboard
5. **Update code** - changes auto-deploy on Streamlit Cloud!

---

**Need Help?** Check the README.md or QUICKSTART.md files for more details.

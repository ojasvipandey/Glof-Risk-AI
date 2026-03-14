# 🌐 Streamlit Cloud Deployment - Complete Setup Guide

## 🎯 Goal
Deploy your GLOF-RISK AI application online so it's accessible to anyone, anywhere, anytime.

## ⏱️ Total Time: 15-20 minutes

---

## 📋 Prerequisites Checklist

Before starting, make sure you have:

- [ ] Internet connection
- [ ] GitHub account (free) - Create at https://github.com/signup
- [ ] Git installed (usually comes with GitHub Desktop)
- [ ] All project files in: `C:\Users\Lenovo!\Desktop\GLOF RISK AI`

---

## 🚀 Method 1: Automated Deployment (Easiest)

### For Windows Users:

1. **Double-click** `deploy.ps1` file
2. Follow the prompts
3. Script will guide you through the process

**OR**

### For Mac/Linux Users:

1. Open Terminal in project folder
2. Run: `chmod +x deploy.sh`
3. Run: `./deploy.sh`
4. Follow the prompts

---

## 🛠️ Method 2: Manual Step-by-Step

### PART A: Set Up GitHub Repository

#### Step 1: Create GitHub Account
1. Go to: **https://github.com/signup**
2. Sign up (takes 2 minutes)
3. Verify your email

#### Step 2: Create New Repository
1. Go to: **https://github.com/new**
2. Repository name: `glof-risk-ai`
3. Description: "AI-Powered GLOF Risk Assessment Platform"
4. **Make it PUBLIC** (required for free Streamlit Cloud)
5. **DO NOT** check "Initialize with README"
6. Click **"Create repository"**

#### Step 3: Upload Code to GitHub

**Option A: Using GitHub Desktop (Recommended)**
1. Download: **https://desktop.github.com/**
2. Install and sign in
3. Click **"File" → "Add Local Repository"**
4. Browse to: `C:\Users\Lenovo!\Desktop\GLOF RISK AI`
5. Click **"Publish repository"**
6. Name: `glof-risk-ai`
7. Make it **Public**
8. Click **"Publish"**

**Option B: Using Command Line**
```powershell
# Open PowerShell in project folder
cd "C:\Users\Lenovo!\Desktop\GLOF RISK AI"

# Initialize Git (if not done)
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit - GLOF-RISK AI"

# Add remote (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/glof-risk-ai.git

# Push to GitHub
git branch -M main
git push -u origin main
```

**Note:** If asked for password, use a **Personal Access Token**:
1. Go to: https://github.com/settings/tokens
2. Generate new token (classic)
3. Select `repo` scope
4. Copy token and use as password

---

### PART B: Deploy to Streamlit Cloud

#### Step 4: Access Streamlit Cloud
1. Go to: **https://share.streamlit.io**
2. Click **"Sign in"** (top right)
3. Click **"Continue with GitHub"**
4. Authorize Streamlit Cloud access

#### Step 5: Create New App
1. Click **"New app"** button
2. Fill in:
   - **Repository**: Select `YOUR_USERNAME/glof-risk-ai`
   - **Branch**: `main`
   - **Main file path**: `app.py`
   - **App URL**: Leave default or customize
3. Click **"Deploy"**

#### Step 6: Wait for Deployment
- Deployment takes 2-5 minutes
- You'll see build logs
- Status will change to "Running" when ready

#### Step 7: Access Your Live App! 🎉
Your app is now live at:
```
https://YOUR-APP-NAME.streamlit.app
```

**Share this link with anyone!**

---

## ✅ Verification Steps

After deployment, test:

1. **App loads** without errors
2. **Select a lake** from dropdown
3. **Click "Calculate Risk"** - should work
4. **Maps display** correctly
5. **All panels** show data

---

## 🔄 Updating Your App

Whenever you make changes:

```powershell
cd "C:\Users\Lenovo!\Desktop\GLOF RISK AI"
git add .
git commit -m "Update: Description of changes"
git push
```

Streamlit Cloud **automatically redeploys** in 1-2 minutes!

---

## 🆘 Troubleshooting

### Problem: "Repository not found"
**Solution:**
- Check repository name matches exactly
- Ensure repository is **Public**
- Verify you're signed in to correct GitHub account

### Problem: "Deployment failed"
**Solution:**
- Check deployment logs on Streamlit Cloud
- Verify `app.py` is in root directory
- Check `requirements.txt` is correct
- Look for error messages in logs

### Problem: "Module not found"
**Solution:**
- Verify all packages in `requirements.txt`
- Check import statements are correct
- Ensure `__init__.py` files exist in modules/, ui/, utils/

### Problem: "Data files not found"
**Solution:**
- Verify CSV files are in `data/` folder
- Check files are committed to Git
- Ensure paths are relative (not absolute)

### Problem: "Map not displaying"
**Solution:**
- Maps need internet connection for tiles
- Check browser console (F12) for errors
- Try refreshing the page

---

## 📊 What Gets Deployed

Your deployment includes:
- ✅ All Python modules
- ✅ Data files (CSV)
- ✅ UI components
- ✅ Configuration files
- ✅ Requirements.txt
- ✅ README and documentation

**Model files** (`breach_model.pkl`) will be generated automatically on first run.

---

## 🔒 Security Notes

- Repository is **Public** (required for free tier)
- No sensitive data should be in code
- Data files are sample/demo data
- For production, consider private repos (paid plan)

---

## 📈 Next Steps

1. **Test thoroughly** on live app
2. **Share link** with stakeholders
3. **Monitor usage** on Streamlit Cloud dashboard
4. **Update data** as needed
5. **Iterate** based on feedback

---

## 🎓 Additional Resources

- **Streamlit Cloud Docs**: https://docs.streamlit.io/streamlit-community-cloud
- **GitHub Guides**: https://guides.github.com
- **Streamlit Forum**: https://discuss.streamlit.io

---

## ✨ Quick Reference

**Your Live App URL:**
```
https://YOUR-APP-NAME.streamlit.app
```

**Update Command:**
```powershell
git add . && git commit -m "Update" && git push
```

**Streamlit Cloud Dashboard:**
```
https://share.streamlit.io
```

---

**🎉 Congratulations! Your GLOF-RISK AI platform is now live and accessible worldwide!**

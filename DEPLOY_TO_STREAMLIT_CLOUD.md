# 🚀 Deploy GLOF-RISK AI to Streamlit Cloud - Step-by-Step Guide

## ✅ Pre-Deployment Checklist

- [x] All code uses relative paths (✓ Verified)
- [x] Streamlit config file created (✓ Created)
- [x] Requirements.txt is complete (✓ Ready)
- [x] All data files included (✓ Ready)
- [x] No hardcoded paths (✓ Verified)

---

## 📋 Step-by-Step Deployment Instructions

### STEP 1: Create GitHub Account (If You Don't Have One)

1. Go to: **https://github.com/signup**
2. Fill in:
   - Username (e.g., `yourname`)
   - Email address
   - Password
3. Verify your email
4. Complete setup

**Time: 2-3 minutes**

---

### STEP 2: Install Git (If Not Installed)

**Check if Git is installed:**
```bash
git --version
```

**If not installed, download from:**
- Windows: https://git-scm.com/download/win
- Mac: https://git-scm.com/download/mac
- Linux: `sudo apt-get install git`

**Time: 5 minutes**

---

### STEP 3: Prepare Your Code for GitHub

**Open PowerShell or Command Prompt in your project folder:**

```powershell
cd "C:\Users\Lenovo!\Desktop\GLOF RISK AI"
```

**Initialize Git repository:**
```powershell
git init
```

**Add all files:**
```powershell
git add .
```

**Create first commit:**
```powershell
git commit -m "Initial commit - GLOF-RISK AI Platform"
```

**Time: 1 minute**

---

### STEP 4: Create GitHub Repository

1. Go to: **https://github.com/new**
2. Fill in:
   - **Repository name**: `glof-risk-ai` (or any name you prefer)
   - **Description**: "AI-Powered Glacial Lake Outburst Flood Risk Intelligence Platform"
   - **Visibility**: Choose **Public** (required for free Streamlit Cloud)
   - **DO NOT** check "Initialize with README" (we already have files)
3. Click **"Create repository"**

**Time: 1 minute**

---

### STEP 5: Push Code to GitHub

**After creating the repository, GitHub will show you commands. Use these:**

```powershell
# Add your GitHub repository as remote (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/glof-risk-ai.git

# Rename branch to main (if needed)
git branch -M main

# Push code to GitHub
git push -u origin main
```

**You'll be prompted for GitHub username and password:**
- Username: Your GitHub username
- Password: Use a **Personal Access Token** (see below if you need help)

**Time: 2-3 minutes**

---

### STEP 6: Create Personal Access Token (If Needed)

**If Git asks for password and regular password doesn't work:**

1. Go to: **https://github.com/settings/tokens**
2. Click **"Generate new token"** → **"Generate new token (classic)"**
3. Fill in:
   - **Note**: "Streamlit Deployment"
   - **Expiration**: 90 days (or your preference)
   - **Scopes**: Check `repo` (all repo permissions)
4. Click **"Generate token"**
5. **Copy the token** (you won't see it again!)
6. Use this token as your password when Git prompts

**Time: 2 minutes**

---

### STEP 7: Deploy on Streamlit Cloud

1. Go to: **https://share.streamlit.io**
2. Click **"Sign in"** (top right)
3. Click **"Continue with GitHub"**
4. Authorize Streamlit Cloud
5. Click **"New app"** button
6. Fill in the form:
   - **Repository**: Select `YOUR_USERNAME/glof-risk-ai`
   - **Branch**: `main`
   - **Main file path**: `app.py`
   - **App URL** (optional): Leave default or customize
7. Click **"Deploy"**
8. Wait 2-5 minutes for deployment

**Time: 5-10 minutes**

---

### STEP 8: Access Your Live App! 🎉

**Your app will be available at:**
```
https://YOUR-APP-NAME.streamlit.app
```

**Or:**
```
https://YOUR_USERNAME-glof-risk-ai-app-XXXXXX.streamlit.app
```

**Share this link with anyone!**

---

## 🔄 Updating Your Deployed App

**Whenever you make changes:**

```powershell
cd "C:\Users\Lenovo!\Desktop\GLOF RISK AI"
git add .
git commit -m "Update: Description of changes"
git push
```

**Streamlit Cloud will automatically redeploy!** (Takes 1-2 minutes)

---

## 🛠️ Alternative: Using GitHub Desktop (Easier GUI Method)

**If command line seems complicated:**

1. **Download GitHub Desktop**: https://desktop.github.com/
2. **Install and sign in** with your GitHub account
3. **Click "File" → "Add Local Repository"**
4. **Browse to**: `C:\Users\Lenovo!\Desktop\GLOF RISK AI`
5. **Click "Publish repository"**
6. **Name it**: `glof-risk-ai`
7. **Make it Public**
8. **Click "Publish"**
9. **Then proceed to Step 7** (Deploy on Streamlit Cloud)

**Time: 5 minutes**

---

## 📝 Quick Command Reference

```powershell
# Navigate to project
cd "C:\Users\Lenovo!\Desktop\GLOF RISK AI"

# Initialize Git
git init

# Add files
git add .

# Commit
git commit -m "Initial commit"

# Add remote (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/glof-risk-ai.git

# Push to GitHub
git push -u origin main

# Update app (after making changes)
git add .
git commit -m "Update description"
git push
```

---

## ✅ Verification Checklist

After deployment, verify:

- [ ] App loads without errors
- [ ] Data files are accessible
- [ ] ML model trains successfully
- [ ] Maps display correctly
- [ ] All calculations work
- [ ] App is accessible from other devices

---

## 🆘 Troubleshooting

### "Repository not found"
- Check repository name matches exactly
- Ensure repository is Public
- Verify you have access to the repository

### "Deployment failed"
- Check Streamlit Cloud logs
- Verify `app.py` is in root directory
- Ensure `requirements.txt` is correct
- Check for import errors in logs

### "Module not found"
- Verify all dependencies in `requirements.txt`
- Check import paths are correct
- Ensure all `__init__.py` files exist

### "Data files not found"
- Verify CSV files are in `data/` folder
- Check file paths are relative (not absolute)
- Ensure files are committed to Git

---

## 🎯 Next Steps After Deployment

1. **Test all features** on the live app
2. **Share the link** with stakeholders
3. **Monitor usage** on Streamlit Cloud dashboard
4. **Update data files** as needed
5. **Iterate and improve** based on feedback

---

## 📞 Need Help?

- **Streamlit Cloud Docs**: https://docs.streamlit.io/streamlit-community-cloud
- **GitHub Help**: https://docs.github.com
- **Streamlit Forum**: https://discuss.streamlit.io

---

**🎉 Congratulations! Your GLOF-RISK AI platform is now live and accessible worldwide!**

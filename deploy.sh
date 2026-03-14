#!/bin/bash

# GLOF-RISK AI - Automated Deployment Script for Streamlit Cloud
# This script helps you deploy your app to GitHub and Streamlit Cloud

echo "========================================"
echo "  GLOF-RISK AI - Deployment Helper"
echo "========================================"
echo ""

# Check if Git is installed
echo "Checking Git installation..."
if command -v git &> /dev/null; then
    echo "✓ Git found: $(git --version)"
else
    echo "✗ Git is not installed!"
    echo "Please install Git from: https://git-scm.com/download"
    exit 1
fi

# Check if we're in the right directory
if [ ! -f "app.py" ]; then
    echo "✗ app.py not found!"
    echo "Please run this script from the project root directory."
    exit 1
fi

echo "✓ Project files found"
echo ""

# Check Git status
echo "Checking Git repository status..."
if [ -d ".git" ]; then
    echo "✓ Git repository initialized"
else
    echo "Initializing Git repository..."
    git init
    echo "✓ Git repository initialized"
fi

echo ""
echo "========================================"
echo "  STEP 1: Prepare Files"
echo "========================================"
echo ""

# Add all files
echo "Adding files to Git..."
git add .
echo "✓ Files added"

# Check if there are changes to commit
if [ -n "$(git status --porcelain)" ]; then
    echo ""
    read -p "Enter commit message (or press Enter for default): " commit_message
    if [ -z "$commit_message" ]; then
        commit_message="Deploy GLOF-RISK AI to Streamlit Cloud"
    fi
    git commit -m "$commit_message"
    echo "✓ Changes committed"
else
    echo "✓ No changes to commit"
fi

echo ""
echo "========================================"
echo "  STEP 2: GitHub Setup"
echo "========================================"
echo ""

# Check if remote exists
if git remote get-url origin &> /dev/null; then
    echo "✓ Remote repository configured: $(git remote get-url origin)"
    echo ""
    read -p "Push to GitHub? (y/n): " push_choice
    if [ "$push_choice" = "y" ] || [ "$push_choice" = "Y" ]; then
        echo "Pushing to GitHub..."
        git push -u origin main
        echo "✓ Code pushed to GitHub"
    fi
else
    echo "GitHub remote not configured."
    echo ""
    echo "To set up GitHub:"
    echo "1. Go to https://github.com/new"
    echo "2. Create a new repository (make it PUBLIC)"
    echo "3. Copy the repository URL"
    echo "4. Run these commands:"
    echo "   git remote add origin YOUR_REPO_URL"
    echo "   git branch -M main"
    echo "   git push -u origin main"
    echo ""
    read -p "Enter your GitHub repository URL (or press Enter to skip): " repo_url
    if [ -n "$repo_url" ]; then
        git remote add origin "$repo_url"
        git branch -M main
        echo "Pushing to GitHub..."
        git push -u origin main
        echo "✓ Code pushed to GitHub"
    fi
fi

echo ""
echo "========================================"
echo "  STEP 3: Deploy to Streamlit Cloud"
echo "========================================"
echo ""

echo "Next steps:"
echo ""
echo "1. Go to: https://share.streamlit.io"
echo "2. Sign in with GitHub"
echo "3. Click 'New app'"
echo "4. Select your repository"
echo "5. Main file: app.py"
echo "6. Click 'Deploy'"
echo ""
echo "Your app will be live in 2-5 minutes!"
echo ""

# Open browser to Streamlit Cloud (if on Mac)
if [[ "$OSTYPE" == "darwin"* ]]; then
    read -p "Open Streamlit Cloud in browser? (y/n): " open_browser
    if [ "$open_browser" = "y" ] || [ "$open_browser" = "Y" ]; then
        open "https://share.streamlit.io"
    fi
fi

echo ""
echo "========================================"
echo "  Deployment Helper Complete!"
echo "========================================"
echo ""

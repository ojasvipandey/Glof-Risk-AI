#!/bin/bash

echo "========================================"
echo "  GLOF-RISK AI - Local Launcher"
echo "========================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed"
    echo "Please install Python from https://www.python.org/downloads/"
    exit 1
fi

echo "Python found!"
echo ""

# Check if dependencies are installed
echo "Checking dependencies..."
if ! python3 -c "import streamlit" &> /dev/null; then
    echo "Installing dependencies..."
    pip3 install -r requirements.txt
    if [ $? -ne 0 ]; then
        echo "ERROR: Failed to install dependencies"
        exit 1
    fi
fi

echo ""
echo "Starting GLOF-RISK AI..."
echo "The application will open in your browser automatically."
echo ""
echo "To stop the server, press Ctrl+C"
echo ""

# Run Streamlit
streamlit run app.py

# Windows Setup Guide

## Quick Start for Windows Users

### 1. Install Python
- Download Python 3.9+ from python.org
- **Important**: Check "Add Python to PATH" during installation
- Verify: Open Command Prompt and type `python --version`

### 2. Clone Repository
```cmd
git clone https://github.com/hcyber7/global-university-campus-explorer.git
cd global-university-campus-explorer
```

### 3. Create Virtual Environment
```cmd
python -m venv venv
venv\Scripts\activate
```

### 4. Install Dependencies
```cmd
pip install -r requirements.txt
```

### 5. Run Application
```cmd
python app.py
```

Then open: http://localhost:5000

## Troubleshooting Windows

**"Python not found"**
- Add Python to PATH manually
- Restart Command Prompt after installing Python

**"pip not recognized"**
- Use `python -m pip install` instead of `pip install`

**Port 5000 already in use**
- Edit app.py and change `port=5000` to `port=5001`

## Requirements
- Windows 7+
- 500MB free disk space
- Internet connection (for API calls)


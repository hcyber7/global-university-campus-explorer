#!/bin/bash

echo "🎓 Global University & Campus Explorer - W7 Evaluation"
echo "======================================================="
echo ""

# Check if venv exists
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python -m venv venv
fi

# Activate venv
echo "🔌 Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "📚 Installing dependencies..."
pip install -q -r requirements.txt

# Run app
echo ""
echo "✅ Starting application..."
echo ""
echo "🌐 Application running at: http://localhost:5000"
echo "📊 Press Ctrl+C to stop"
echo ""

python app.py

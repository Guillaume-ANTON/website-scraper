echo "Activating virtual environment..."
source venv/bin/activate

echo "Installing requirements..."
pip install -r requirements.txt > /dev/null

echo "Starting FastAPI server..."
uvicorn app.main:app --reload
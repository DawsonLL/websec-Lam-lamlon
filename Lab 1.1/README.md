# 1. Create a virtual environment
python -m venv venv

# 2. Activate it
# On Linux/macOS:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. (Optional) Freeze to lock exact versions
pip freeze > requirements.txt
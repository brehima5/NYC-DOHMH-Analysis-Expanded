## Running the Streamlit App

### Prerequisites
- Python 3.8+
- `pip` package manager

### Steps

1. **Clone the repo**
   ```bash
   git clone https://github.com/<your-username>/NYC-DOHMH-Analysis.git
   cd NYC-DOHMH-Analysis
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate        # macOS/Linux
   # .venv\Scripts\activate          # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install streamlit pandas matplotlib
   ```

4. **Run the app**
   ```bash
   streamlit run project_expanded/app/app.py
   ```

5. The app will open automatically in your browser at `http://localhost:8501`.

> **Note:** The app uses a pre-generated `forecast_results.pkl` file included in the repo. If you want to regenerate it, run the `project_expanded/full_model_pipeline.ipynb` notebook first.

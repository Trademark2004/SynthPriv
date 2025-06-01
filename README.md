# SynthPriv: Quick Start Guide

## 1. Install Python 3.13
- Download and install Python 3.13 from https://www.python.org/downloads/
- Add Python and its Scripts folder to your PATH.

## 2. Install Dependencies
- Open a terminal in the project folder and run:
  ```powershell
  pip install -r requirements.txt
  ```

## 3. Launch the Web App
- Start the Streamlit UI:
  ```powershell
  python -m streamlit run app.py
  ```
- Open http://localhost:8501 in your browser.

## 4. Upload Data and Generate Synthetic Data
- Upload a CSV file (e.g., `testdata.csv`).
- Set privacy parameters (epsilon, delta, etc.).
- Click "Train" to generate synthetic data.
- Click "Evaluate" to see utility metrics and plots.

## 5. Command Line Usage
- Train a model:
  ```powershell
  python -m synthpriv.cli train testdata.csv --epsilon 1.0 --delta 1e-5 --epochs 100 --seed 42
  ```
- Evaluate synthetic data:
  ```powershell
  python -m synthpriv.cli evaluate testdata.csv reports/testdata_synth.csv
  ```

## 6. Testing
- Run tests with:
  ```powershell
  pytest
  ```

## 7. Lint and Format
- Lint:
  ```powershell
  ruff .
  ```
- Format:
  ```powershell
  black .
  ```

## 8. Example Test Data

See `testdata.csv`:
```
age,income,gender
25,50000,M
32,62000,F
47,83000,M
51,91000,F
38,70000,M
29,54000,F
44,80000,M
36,67000,F
```

---
For advanced usage, see `USAGE.md` and `VS_CODE_GUIDE.md`.

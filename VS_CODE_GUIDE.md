# SynthPriv: Step-by-step VS Code Guide

## 1. Install Prerequisites
- Python 3.11 (https://www.python.org/downloads/)
- [Poetry](https://python-poetry.org/docs/#installation):
  ```sh
  pip install poetry
  ```
- (Optional) Docker Desktop for containerized runs

## 2. Open the Project in VS Code
- Open the folder containing this project (`PROJECT_TREE.txt` root) in VS Code.

## 3. Set Up the Python Environment
- Open a VS Code terminal (``Ctrl+` ``).
- Run:
  ```sh
  poetry install
  ```
- If prompted, select the Poetry-created Python interpreter in the VS Code status bar.

## 4. (Optional) Configure PostgreSQL
- Copy `.env.example` to `.env` and edit the DSN if you want to use PostgreSQL for the catalog.

## 5. Run the Streamlit Web UI
- In the terminal:
  ```sh
  poetry run streamlit run app.py
  ```
- Open http://localhost:8501 in your browser.
- Upload a CSV, set privacy parameters, and run training/evaluation.

## 6. Run CLI Commands
- Example: Train a model
  ```sh
  poetry run python -m synthpriv.cli train data/adult.csv --epsilon 1.0 --delta 1e-5 --epochs 100 --seed 42
  ```
- Example: Evaluate synthetic data
  ```sh
  poetry run python -m synthpriv.cli evaluate data/adult.csv reports/adult_synth.csv
  ```

## 7. Run Tests
- In the terminal:
  ```sh
  poetry run pytest
  ```

## 8. Lint and Format
- Lint:
  ```sh
  poetry run ruff .
  ```
- Format:
  ```sh
  poetry run black .
  ```

## 9. Build and Run with Docker (CPU)
- Build:
  ```sh
  docker build -f Dockerfile.cpu -t synthpriv-cpu .
  ```
- Run:
  ```sh
  docker run -it -p 8501:8501 synthpriv-cpu
  ```

## 10. Troubleshooting
- If you see missing module errors, ensure Poetry environment is selected in VS Code.
- For GPU, use `Dockerfile.gpu` and a CUDA-capable system.

---

**You are ready to use SynthPriv in VS Code!**

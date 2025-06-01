# USAGE.md

## Example 1: Train a DP-CTGAN model

```shell
poetry run python -m synthpriv.cli train data/adult.csv --epsilon 1.0 --delta 1e-5 --epochs 100 --seed 42
```

**Expected output:**
```
Synthetic data saved to reports/adult_synth.csv
Column epsilons: {'age': 1.0, 'workclass': 1.0, ...}
```

---

## Example 2: Evaluate synthetic data utility/privacy

```shell
poetry run python -m synthpriv.cli evaluate data/adult.csv reports/adult_synth.csv
```

**Expected output:**
```
Metrics: {'ks': 0.12, 'js': 0.08, 'efficacy': 0.91}
Report: reports/adult/20250601_120000
```

![utility_privacy.png](reports/adult/20250601_120000/utility_privacy.png)

---

## Example 3: Use the Streamlit UI

```shell
poetry run streamlit run app.py
```

**Expected output:**

![streamlit_ui.png](docs/streamlit_ui.png)

---

See the [project tree](PROJECT_TREE.txt) for file layout.

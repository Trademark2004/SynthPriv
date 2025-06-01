# synthpriv/eval.py
import os
import json
import pandas as pd  # Data handling
import matplotlib.pyplot as plt  # Plotting

# Evaluate synthetic data utility by comparing to real data
# Uses mean absolute error (MAE) per column as a simple metric
def evaluate(real_csv, synth_csv, report_dir=None):
    real = pd.read_csv(real_csv)
    synth = pd.read_csv(synth_csv)
    # Compute MAE for each column present in both datasets
    mae = {col: abs(real[col] - synth[col]).mean() for col in real.columns if col in synth.columns}
    metrics = {'mae': mae}
    # Create a report directory if not provided
    if not report_dir:
        report_dir = os.path.join('reports', os.path.basename(real_csv).replace('.csv', ''), pd.Timestamp.now().strftime('%Y%m%d_%H%M%S'))
    os.makedirs(report_dir, exist_ok=True)
    # Save metrics as JSON
    with open(os.path.join(report_dir, 'metrics.json'), 'w') as f:
        json.dump(metrics, f, indent=2)
    # Plot MAE per column
    plt.figure()
    plt.bar(mae.keys(), mae.values())
    plt.title('Mean Absolute Error (MAE) per column')
    plt.ylabel('MAE')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join(report_dir, 'utility_mae.png'))
    plt.close()
    return metrics, report_dir

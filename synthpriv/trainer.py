# synthpriv/trainer.py
import os
import pandas as pd  # Data handling
from sdv.tabular import GaussianCopula  # Tabular data synthesizer
from synthpriv.epsilon_allocator import adaptive_epsilon  # Privacy budget allocation


# Main training function for synthetic data generation
# Uses SDV's GaussianCopula for compatibility with Python 3.13
# Returns the path to the synthetic CSV and the per-column epsilon allocation
def train_copula(csv_path, epsilon, delta, epochs=100, seed=42, output_path=None):
    pd.options.mode.chained_assignment = None
    df = pd.read_csv(csv_path)
    schema_stats = df.describe(include='all')
    col_eps = adaptive_epsilon(schema_stats, epsilon)
    model = GaussianCopula()
    model.fit(df)
    synth = model.sample(len(df))
    if not output_path:
        output_path = os.path.join('reports', os.path.basename(csv_path).replace('.csv', '_synth.csv'))
    synth.to_csv(output_path, index=False)
    return output_path, col_eps

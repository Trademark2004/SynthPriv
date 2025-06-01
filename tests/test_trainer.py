# tests/test_trainer.py
import pytest  # Testing framework
import pandas as pd  # Data handling
from synthpriv.trainer import train_copula  # Synthetic data trainer

# Test that synthetic data generation works and epsilon allocation is valid
def test_train_copula(tmp_path):
    # Create mock CSV
    df = pd.DataFrame({'a': [1,2,3], 'b': [4,5,6]})
    csv_path = tmp_path / 'mock.csv'
    df.to_csv(csv_path, index=False)
    synth_path, col_eps = train_copula(str(csv_path), epsilon=1.0, delta=1e-5, epochs=2, seed=123)
    synth = pd.read_csv(synth_path)
    assert synth.shape == df.shape  # Output shape matches input
    assert all(eps >= 0 for eps in col_eps.values())  # Epsilon values are non-negative

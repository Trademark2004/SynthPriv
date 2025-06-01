# synthpriv/epsilon_allocator.py
import numpy as np

# Allocate epsilon (privacy budget) per column
# Greedy allocation: higher epsilon to low-sensitivity columns, mask IDs
# Returns a dict mapping column names to epsilon values
def adaptive_epsilon(schema_stats, global_budget):
    """Greedy allocation: higher epsilon to low-sensitivity columns."""
    n_cols = len(schema_stats.columns)
    eps = {}
    for col in schema_stats.columns:
        if 'id' in col.lower():
            eps[col] = 0.0  # Mask ID columns
        else:
            eps[col] = global_budget / (n_cols - 1)  # Uniform allocation for others
    return eps

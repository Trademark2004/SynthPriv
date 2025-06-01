import streamlit as st  # Streamlit for web UI
import subprocess  # For running CLI commands
import os
import pandas as pd  # Data handling

# Set up Streamlit page
st.set_page_config(page_title="SynthPriv", layout="wide")
st.title("SynthPriv: Differentially Private Synthetic Data Generator")

# Help section explaining all UI fields and actions
with st.expander("What do these settings mean?", expanded=False):
    st.markdown("""
- **Epsilon (privacy budget):** Controls the strength of privacy. Lower values mean stronger privacy but less accurate synthetic data. Typical values: 0.1 (very private) to 10 (less private).
- **Delta:** A very small probability that privacy may not be perfectly preserved. Usually set to a tiny value like 1e-5.
- **Epochs:** Number of training cycles for the model. More epochs can improve synthetic data quality but take longer.
- **Seed:** Random seed for reproducibility. Use the same seed to get the same synthetic data from the same input.
- **Train DP-CTGAN:** Start the process to generate differentially private synthetic data from your uploaded CSV.
- **Evaluate Synthetic Data:** Compare the real and synthetic data using utility metrics and plots.
    """)

# Session state for uploaded file
if 'uploaded' not in st.session_state:
    st.session_state['uploaded'] = None

# File uploader for CSV
uploaded = st.file_uploader("Upload CSV", type=["csv"])
if uploaded:
    st.session_state['uploaded'] = uploaded
    df = pd.read_csv(uploaded)
    st.write("Preview:", df.head())  # Show preview of uploaded data
    st.session_state['csv_path'] = f"tmp_{uploaded.name}"
    df.to_csv(st.session_state['csv_path'], index=False)

# If a file is uploaded, show parameter inputs and actions
if st.session_state.get('uploaded'):
    # Privacy and training parameters
    eps = st.number_input("Epsilon (privacy budget)", min_value=0.1, max_value=10.0, value=1.0, step=0.1)
    delta = st.number_input("Delta", min_value=1e-8, max_value=1e-2, value=1e-5, step=1e-5, format="%e")
    epochs = st.number_input("Epochs", min_value=1, max_value=1000, value=100, step=1)
    seed = st.number_input("Seed", min_value=0, max_value=999999, value=42, step=1)
    # Train button: runs the CLI to generate synthetic data
    if st.button("Train DP-CTGAN"):
        cmd = ["python", "-m", "synthpriv.cli", "train", st.session_state['csv_path'], "--epsilon", str(eps), "--delta", str(delta), "--epochs", str(epochs), "--seed", str(seed)]
        proc = subprocess.run(cmd, capture_output=True, text=True)
        st.session_state['train_output'] = proc.stdout
        st.success("Training complete!")
        st.text(proc.stdout)

    # Evaluate button: runs the CLI to compare real and synthetic data
    if st.button("Evaluate Synthetic Data"):
        # Assume output path from train
        synth_path = st.session_state['csv_path'].replace('.csv', '_synth.csv')
        cmd = ["python", "-m", "synthpriv.cli", "evaluate", st.session_state['csv_path'], synth_path]
        proc = subprocess.run(cmd, capture_output=True, text=True)
        st.text(proc.stdout)
        # Show plot if exists
        report_dir = os.path.join("reports", os.path.basename(st.session_state['csv_path']).replace('.csv', ''),)
        if os.path.exists(report_dir):
            for f in os.listdir(report_dir):
                if f.endswith(".png"):
                    st.image(os.path.join(report_dir, f))

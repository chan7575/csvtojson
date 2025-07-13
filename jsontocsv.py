import pandas as pd
from pandas import json_normalize
import sys

def json_to_csv(json_input_path, csv_output_path):
    try:
        # Load JSON
        data = pd.read_json(json_input_path)

        # Normalize if needed
        if isinstance(data.iloc[0], dict):
            data = json_normalize(data)

        # Export to CSV
        data.to_csv(csv_output_path, index=False)
        print(f"CSV file saved at: {csv_output_path}")
    except Exception as e:
        print("Error:", e)

# Run from command line
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python json_to_csv.py <input.json> <output.csv>")
    else:
        json_to_csv(sys.argv[1], sys.argv[2])

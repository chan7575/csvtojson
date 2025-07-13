import pandas as pd

fr = pd.read_json("test.json")
normalized_json = pd.json_normalize(fr);
normalized_json.to_csv("test.csv",index=False);

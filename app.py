import pandas as pd

df = pd.read_csv('sample_data/VNL2023.csv')

print(df.sample(5))
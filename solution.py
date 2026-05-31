import pandas as pd
import glob

# Load all 3 CSV files
files = glob.glob('data/*.csv')
dfs = []

for file in files:
    df = pd.read_csv(file)
    # Filter only Pink Morsel
    df = df[df['product'] == 'pink morsel']
    # Create sales column
    df['sales'] = df['quantity'] * df['price']
    # Keep only required columns
    df = df[['sales', 'date', 'region']]
    dfs.append(df)

# Combine all into one file
result = pd.concat(dfs)
result.to_csv('data/output.csv', index=False)
print("Done! output.csv created.")
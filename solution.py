import pandas as pd
import glob

files = glob.glob('data/daily_sales_data_*.csv')
dfs = []

for file in files:
    df = pd.read_csv(file)
    df = df[df['product'] == 'pink morsel']
    # Remove $ sign and convert price to float
    df['price'] = df['price'].str.replace('$', '', regex=False).astype(float)
    df['sales'] = df['quantity'] * df['price']
    df = df[['sales', 'date', 'region']]
    dfs.append(df)

result = pd.concat(dfs)
result.to_csv('data/output.csv', index=False)
print("Done! output.csv created.")
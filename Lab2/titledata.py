import pandas as pd


data = pd.read_csv('data4.csv')

if 'Body' in data.columns:
    body_data = data[['Body']] 
else:
    raise ValueError("The 'Body' column does not exist in the data4.csv file.")


body_data.to_csv('Bodydata.csv', index=False)

print("Body data has been saved to bodydata.csv successfully.")

import pandas as pd

old_path = '3-3File.csv'
data = pd.read_csv(old_path)

pitcher_data = data[data['Pitcher']] == "Kuhle, Aiden"




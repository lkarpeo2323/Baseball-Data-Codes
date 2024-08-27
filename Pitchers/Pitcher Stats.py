import pandas as pd
from scipy import stats

#Original File Name
old_path = '3-3File.csv'
data = pd.read_csv(old_path)

#Pitcher Name
pitcher_name = 'Colosimo, Dominic'


filtered_data = data[data['Pitcher'] == pitcher_name]

new_data = filtered_data.describe()

print(new_data)




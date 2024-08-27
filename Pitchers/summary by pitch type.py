import pandas as pd
from scipy import stats

#Original File Name
old_path = '3-3File.csv'
data = pd.read_csv(old_path)

#Pitcher Name and Pitch Type
pitcher_name = 'Kuhle, Aiden'
pitch_type = 'Curveball'

keep = [
'Pitcher',
'AutoPitchType',
'RelHeight',
'Extension',
'SpinRate',
'SpinAxis'
    ]
kept = data[keep]

filtered_data = kept[(kept['Pitcher'] == pitcher_name) &
                     (kept['AutoPitchType'] == pitch_type) ]

new_data = filtered_data.describe()

print(new_data)




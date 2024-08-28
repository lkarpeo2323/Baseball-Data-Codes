import pandas as pd
from scipy.stats import skew, kurtosis

# Original File Name
old_path = '3-3File.csv'
data = pd.read_csv(old_path)

# Enter desired Pitcher Name , number of balls, and strikes
pitcher_name = 'Colosimo, Dominic'
balls = 0
strikes = 2

# Columns to keep
keep = [
    'Pitcher',
    'AutoPitchType',
    'Balls',
    'Strikes'
]

# Filter and keep relevant columns
kept = data[keep]

#Pitcher name and count
filtered_data = kept[(kept['Pitcher'] == pitcher_name) &
                     (kept['Balls'] == balls) &
                     (kept['Strikes'] == strikes)]


#Pitch Usage
usage = filtered_data['AutoPitchType'].value_counts()

pd.set_option('display.max_columns', None)  
pd.set_option('display.width', None)

# Print results
print(f"{pitcher_name}")

print(f"\nCount: {balls}-{strikes}")
print(usage)


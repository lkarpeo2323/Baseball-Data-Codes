import pandas as pd
from scipy.stats import skew, kurtosis


# Original File Name
old_path = '3-3File.csv'
data = pd.read_csv(old_path)

# Pitcher Name and Pitch Type
pitcher_name = 'Colosimo, Dominic'
pitch_type = 'ChangeUp'

# Columns to keep
keep = [
    'Pitcher',
    'AutoPitchType',
    'RelSpeed',
    'RelHeight',
    'Extension',
    'SpinRate',
    'SpinAxis',
    'VertBreak',
    'HorzApprAngle'
]

#All number columns
number = keep[3:]

# Filter and keep relevant columns
kept = data[keep]

# Filter data for the specific pitcher and pitch type
filtered_data = kept[(kept['Pitcher'] == pitcher_name) &
                     (kept['AutoPitchType'] == pitch_type)]

# Calculate skewness and kurtosis for numerical columns
skewness = filtered_data[number].apply(lambda x: skew(x.dropna()))
kurt = filtered_data[number].apply(lambda x: kurtosis(x.dropna()))
summary = filtered_data[number].describe()

# Print results
print("Skewness:")
print(skewness)

print("\nKurtosis:")
print(kurt)

print("\nSummary:")
print(summary)

import pandas as pd

# Assuming you have a CSV file or DataFrame
df = pd.read_excel('Hofstra Pitching Results.xlsx')

# Group and summarize by category and subcategory
summary = df.groupby(['Stretch/Windup', 'Task', 'Pitch Type'])['Accomplished'].value_counts().unstack().fillna(0)

print(summary)


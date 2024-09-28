import pandas as pd

# Load all the sheets from the Excel file
xls = pd.ExcelFile('Hofstra Pitching Results.xlsx')
sheet_names = xls.sheet_names

# Create a list to hold DataFrames for each sheet
dataframes = []

# Iterate over each sheet, adding its name as a column and appending it to the list
for sheet_name in sheet_names:
    df = pd.read_excel(xls, sheet_name=sheet_name)
    df['Player Name'] = sheet_name  # Add a column for the player's name
    dataframes.append(df)

# Concatenate all sheets into a master DataFrame
master_df = pd.concat(dataframes, ignore_index=True)

# Group and calculate the count of each result for each player (excluding Pitch Type)
counts = master_df.groupby(['Player Name', 'Stretch/Windup', 'Task', 'Accomplished?']).size().unstack().fillna(0)

# Calculate the percentage of each result for each player
percentages = counts.div(counts.sum(axis=1), axis=0) * 100

# Save the percentages as an Excel sheet
percentages.to_excel('Hofstra_Pitching_Percentages_No_Pitch_Type.xlsx')

print("The summary of percentages has been saved as 'Hofstra_Pitching_Percentages.xlsx'")

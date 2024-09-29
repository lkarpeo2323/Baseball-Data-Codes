import pandas as pd

# Load the Excel workbook
file_path = 'Hofstra Pitching Results.xlsx'
xls = pd.ExcelFile(file_path)
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

# Rename columns to match the desired output
counts.rename(columns={'No': 'No', 'Not accomplished but a strike': 'Not accomplished but a strike', 'Yes': 'Yes'}, inplace=True)

# Calculate Attempts and Success Rate
counts['Attempts'] = counts.sum(axis=1)
counts['Success Rate 9/25 (Yes %)'] = (counts['Yes'] / counts['Attempts'] * 100).round(2)

# Reset index to convert it to a column format
result = counts.reset_index()

# Save the result as an Excel sheet
output_path_counts = 'Hofstra Pitching Summary.xlsx'
result.to_excel(output_path_counts, index=False)

print(f"The summary of counts with success rate has been saved as '{output_path_counts}'.")

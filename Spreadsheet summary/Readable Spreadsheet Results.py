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

# Save the counts as an Excel sheet
output_path_counts = 'Hofstra_Pitching_Counts_No_Pitch_Type.xlsx'
counts.to_excel(output_path_counts)

print(f"The summary of counts has been saved as '{output_path_counts}'.")

import pandas as pd

# Load the Excel workbook
file_path = 'Hofstra Pitching Results.xlsx'
try:
    xls = pd.ExcelFile(file_path)
except FileNotFoundError:
    print(f"Error: The file '{file_path}' does not exist.")
    exit()

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

# Ensure the date column is in datetime format
if 'Date' in master_df.columns:
    master_df['Date'] = pd.to_datetime(master_df['Date'], errors='coerce')
else:
    print("Error: The 'Date' column is not present in the data.")
    exit()

# Group and calculate counts for each combination of Player, Date, etc.
counts = (master_df.groupby(['Player Name', 'Date', 'Stretch/Windup', 'Task', 'Accomplished?'])
          .size()
          .unstack(fill_value=0))

# Rename columns to be clearer
counts.rename(columns={'No': 'No', 'Not accomplished but a strike': 'Not accomplished but a strike', 'Yes': 'Yes'}, inplace=True)

# Calculate Attempts (Total of Yes + No + Not accomplished but a strike)
counts['Attempts'] = counts.sum(axis=1)

# Reset index to get the columns back into a standard format
counts = counts.reset_index()

# Now pivot the table so that each date has its own column for the success rate
pivoted_counts = counts.pivot_table(index=['Player Name', 'Stretch/Windup', 'Task'],
                                    columns='Date',
                                    values='Yes',
                                    aggfunc='sum').fillna(0)

# Calculate Success Rate for each Date
attempts_pivot = counts.pivot_table(index=['Player Name', 'Stretch/Windup', 'Task'],
                                    columns='Date',
                                    values='Attempts',
                                    aggfunc='sum').fillna(0)

# Now, divide the 'Yes' values by the attempts to get success rates for each date
success_rate_by_date = (pivoted_counts / attempts_pivot * 100).round(2)

# Rename the columns to indicate success rate by date
success_rate_by_date.columns = [f'Success Rate {date.strftime("%m/%d")}' for date in success_rate_by_date.columns]

# Merge success rates back with the main data
final_result = counts[['Player Name', 'Stretch/Windup', 'Task']].drop_duplicates().merge(success_rate_by_date, on=['Player Name', 'Stretch/Windup', 'Task'])

# Save the final result to an Excel file
output_path = 'Hofstra Pitching Summary by Date.xlsx'
final_result.to_excel(output_path, index=False)

print(f"The summary of counts with success rates for each date has been saved as '{output_path}'.")


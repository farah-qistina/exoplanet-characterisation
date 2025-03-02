import pandas as pd

# Specify the input CSV file and the output file
input_file = 'all_fields.csv'
output_file = 'ps_fields.csv'

# Load the CSV file into a DataFrame
df = pd.read_csv(input_file)

# Define the substrings to search for (all in lowercase)
unwanted_substrings = ["err1", "err2", "lim", "str", "PLANETARY SYSTEMS COMPOSITE PARAMETERS ONLY"]

def row_contains_unwanted(row):
    """Check if any cell in the row contains any of the unwanted substrings."""
    for cell in row:
        cell_str = str(cell)  # Convert the cell value to a lowercase string
        if any(sub in cell_str for sub in unwanted_substrings):
            return True
    return False

# Create a mask that is True for rows that contain any unwanted substring
mask = df.apply(lambda row: row_contains_unwanted(row), axis=1)

# Filter out those rows
df_cleaned = df[~mask]

# Save the cleaned DataFrame to a new CSV file
df_cleaned.to_csv(output_file, index=False)

print(f"Cleaned CSV saved as '{output_file}'.")

import pandas as pd
import os

# Find the exact folder this script is in
script_dir = os.path.dirname(os.path.abspath(__file__))

# Go up one level to the project folder, then into the 'data' folder
file_path = os.path.join(script_dir, '..', 'data', 'students_performance.csv')

# Load the dataset
df = pd.read_csv(file_path)

# Print the first 5 rows
print(df.head())
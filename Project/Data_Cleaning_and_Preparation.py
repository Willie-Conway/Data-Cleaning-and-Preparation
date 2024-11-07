import pandas as pd
import numpy as np
import sqlite3

# Load the dataset
data = pd.read_csv(r'csv/layoffs_2024.csv')

# Display the initial structure of the data
print("Initial data structure:")
print(data.info())

# Check for duplicate records
initial_count = data.shape[0]
data = data.drop_duplicates()
final_count = data.shape[0]
print(f"Removed {initial_count - final_count} duplicate rows.")

# Check for missing values
print("\nMissing values before cleaning:")
print(data.isnull().sum())

# Impute missing values
# Impute numeric columns with the rounded mean
numeric_columns = data.select_dtypes(include=['float64', 'int64']).columns
for column in numeric_columns:
    mean_value = round(data[column].mean(), 2)  # Round to 2 decimal places
    data[column] = data[column].fillna(mean_value)  # Replace NaNs with the rounded mean
    print(f"Imputed missing values in {column} with rounded mean: {mean_value}")

# Impute categorical columns with the mode
categorical_columns = data.select_dtypes(include=['object']).columns
for column in categorical_columns:
    mode_value = data[column].mode()[0]
    data[column] = data[column].fillna(mode_value)  # Replace NaNs with the mode
    print(f"Imputed missing values in {column} with mode: {mode_value}")

# Normalize data formats
# Convert text columns to lowercase for consistency
for column in categorical_columns:
    data[column] = data[column].str.lower()  # Convert text to lowercase
    print(f"Converted {column} to lowercase.")

# Standardize date formats (assuming there is a 'date' column)
if 'date' in data.columns:
    data['date'] = pd.to_datetime(data['date']).dt.strftime('%Y-%m-%d')
    print("Standardized date format in 'date' column.")

# Check for remaining missing values after cleaning
print("\nMissing values after cleaning:")
print(data.isnull().sum())

# Ensure data types are appropriate for analysis
# Use the correct column names based on your dataset
data['total_laid_off'] = pd.to_numeric(data['total_laid_off'], errors='coerce')
data['percentage_laid_off'] = pd.to_numeric(data['percentage_laid_off'], errors='coerce')
data['funds_raised'] = pd.to_numeric(data['funds_raised'], errors='coerce')

# Final check on data types
print("\nFinal data types:")
print(data.dtypes)

# Save the cleaned data to a new CSV file for Power BI
cleaned_file_path = 'cleaned_layoffs_2024.csv'
data.to_csv(cleaned_file_path, index=False)
print(f"Cleaned dataset saved as '{cleaned_file_path}'.")

# Optional: Save cleaned data to SQL database
# Create a connection to the SQLite database
conn = sqlite3.connect('cleaned_layoffs.db')
data.to_sql('cleaned_layoffs', conn, if_exists='replace', index=False)
print("Cleaned data has been inserted into the SQL database 'cleaned_layoffs.db'.")

# Close the database connection
conn.close()
print("Database connection closed.")

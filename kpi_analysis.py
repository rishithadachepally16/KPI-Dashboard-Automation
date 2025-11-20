import pandas as pd

# Load data
df = pd.read_csv('data.csv')

# Data Validation
df['Tasks_Completed'] = pd.to_numeric(df['Tasks_Completed'], errors='coerce')
df['Hours_Worked'] = pd.to_numeric(df['Hours_Worked'], errors='coerce')
df['Errors_Found'] = pd.to_numeric(df['Errors_Found'], errors='coerce')

# Check for missing values
print("Missing values:\n", df.isnull().sum())

# KPI Calculations
df['Efficiency'] = df['Tasks_Completed'] / df['Hours_Worked']
df['Error_Rate'] = df['Errors_Found'] / df['Tasks_Completed']

# Detect anomalies (Efficiency < 0.5 or Error Rate > 0.2)
anomalies = df[(df['Efficiency'] < 0.5) | (df['Error_Rate'] > 0.2)]
print("\nAnomalies detected:\n", anomalies)

# Summary Statistics
print("\nSummary Statistics:\n", df.describe())

# Export processed data
df.to_csv('processed_data.csv', index=False)

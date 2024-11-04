# Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset (update the file path if necessary)
data = pd.read_csv('C:\\Users\\Afiya\\Downloads\\prodigy\\UK_Accident.csv')

# Display the first few rows of the dataset to understand the data structure
print(data.head())

# Data Cleaning (handling missing values if any)
data.dropna(inplace=True)  # Drop rows with missing values for simplicity

# Convert date and time columns to datetime objects if not already in that format
data['Date'] = pd.to_datetime(data['Date'], errors='coerce')  # Handles non-date formats
data['Year'] = data['Date'].dt.year  # Extract year
data['Month'] = data['Date'].dt.month  # Extract month
data['Day'] = data['Date'].dt.day  # Extract day

# Check the columns available in the dataset
print(data.columns)

# 1. Accident Severity Distribution
plt.figure(figsize=(8, 6))
sns.countplot(x='Accident_Severity', data=data, palette='viridis')
plt.title('Distribution of Accident Severity')
plt.xlabel('Severity Level')
plt.ylabel('Number of Accidents')
plt.show()

# 2. Monthly Accident Trend
plt.figure(figsize=(10, 6))
sns.countplot(x='Month', data=data, palette='magma')
plt.title('Monthly Accident Trend')
plt.xlabel('Month')
plt.ylabel('Number of Accidents')
plt.show()

# 3. Accidents by Weather Condition
plt.figure(figsize=(12, 6))
sns.countplot(y='Weather_Conditions', data=data, order=data['Weather_Conditions'].value_counts().index, palette='coolwarm')
plt.title('Accidents by Weather Condition')
plt.xlabel('Number of Accidents')
plt.ylabel('Weather Condition')
plt.show()

# 4. Hourly Accident Trend
data['Hour'] = pd.to_datetime(data['Time'], format='%H:%M', errors='coerce').dt.hour
plt.figure(figsize=(10, 6))
sns.countplot(x='Hour', data=data, palette='plasma')
plt.title('Hourly Accident Trend')
plt.xlabel('Hour of the Day')
plt.ylabel('Number of Accidents')
plt.show()

# 5. Accident Analysis by Road Surface Conditions (Top Conditions)
top_conditions = data['Road_Surface_Conditions'].value_counts().head(10)
plt.figure(figsize=(12, 6))
sns.barplot(y=top_conditions.index, x=top_conditions.values, palette='inferno')
plt.title('Accidents by Road Surface Condition')
plt.xlabel('Number of Accidents')
plt.ylabel('Road Surface Condition')
plt.show()

# Step 6: Bivariate Analysis - Analyze the interaction between weather, road conditions, and accident time
plt.figure(figsize=(10, 6))
sns.heatmap(pd.crosstab(data['Weather_Conditions'], data['Road_Surface_Conditions']), annot=True, cmap='coolwarm')
plt.title('Weather vs Road Surface Type')
plt.show()


# 7. Yearly Accident Trend
yearly_data = data.groupby('Year').size()  # Grouping data by year
plt.figure(figsize=(10, 6))
sns.lineplot(x=yearly_data.index, y=yearly_data.values, marker='o')
plt.title('Yearly Accident Trend')
plt.xlabel('Year')
plt.ylabel('Number of Accidents')
plt.show()

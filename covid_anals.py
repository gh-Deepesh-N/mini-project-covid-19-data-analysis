# Importing required libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Load the dataset
file_path = "country_wise_latest.csv"  # Replace with actual path
data = pd.read_csv(file_path)

# Display dataset information
print("Dataset Information:\n")
print(data.info())

# Handling missing values
print("\nMissing values before handling:")
print(data.isnull().sum())

# Filling missing values with mean or zero (based on column type)
data.fillna(data.mean(numeric_only=True), inplace=True)

print("\nMissing values after handling:")
print(data.isnull().sum())

# Display basic statistics of dataset
print("\nBasic Statistics:\n")
print(data.describe())

# ========================= #
# VISUALIZATIONS & ANALYSIS #
# ========================= #

# 1. Top 10 Countries with the Most Confirmed Cases
top_confirmed = data.nlargest(10, 'Confirmed')
plt.figure(figsize=(12, 6))
sns.barplot(x="Country/Region", y="Confirmed", data=top_confirmed, palette="coolwarm")
plt.xticks(rotation=45)
plt.title("Top 10 Countries with the Most Confirmed Cases")
plt.xlabel("Country")
plt.ylabel("Number of Confirmed Cases")
plt.show()

# 2. Top 10 Countries with the Most Deaths
top_deaths = data.nlargest(10, 'Deaths')
plt.figure(figsize=(12, 6))
sns.barplot(x="Country/Region", y="Deaths", data=top_deaths, palette="Reds")
plt.xticks(rotation=45)
plt.title("Top 10 Countries with the Most Deaths")
plt.xlabel("Country")
plt.ylabel("Number of Deaths")
plt.show()

# 3. Correlation Matrix Heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(data.corr(numeric_only=True), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap of COVID-19 Data")
plt.show()

# 4. Relationship between New Cases and Deaths
plt.figure(figsize=(10, 6))
sns.scatterplot(x="New cases", y="New deaths", hue="Country/Region", size="New deaths", data=data, legend=False)
plt.title("New Cases vs New Deaths")
plt.xlabel("New Cases")
plt.ylabel("New Deaths")
plt.show()

# 5. Recovery Rate Distribution
data['Recovery Rate'] = (data["Recovered"] / data["Confirmed"]) * 100
plt.figure(figsize=(10, 5))
sns.histplot(data["Recovery Rate"], bins=30, kde=True, color='green')
plt.title("Recovery Rate Distribution")
plt.xlabel("Recovery Rate (%)")
plt.ylabel("Frequency")
plt.show()

# 6. Fatality Rate Distribution
data['Fatality Rate'] = (data["Deaths"] / data["Confirmed"]) * 100
plt.figure(figsize=(10, 5))
sns.histplot(data["Fatality Rate"], bins=30, kde=True, color='red')
plt.title("Fatality Rate Distribution")
plt.xlabel("Fatality Rate (%)")
plt.ylabel("Frequency")
plt.show()

# 7. Total Cases vs. Total Recovered (Regression Line)
plt.figure(figsize=(10, 6))
sns.regplot(x="Confirmed", y="Recovered", data=data, scatter_kws={"color": "blue"}, line_kws={"color": "red"})
plt.title("Total Confirmed Cases vs Total Recovered Cases")
plt.xlabel("Confirmed Cases")
plt.ylabel("Recovered Cases")
plt.show()

# 8. Top 10 Countries with the Highest Fatality Rate
top_fatality = data.nlargest(10, 'Fatality Rate')
plt.figure(figsize=(12, 6))
sns.barplot(x="Country/Region", y="Fatality Rate", data=top_fatality, palette="Reds")
plt.xticks(rotation=45)
plt.title("Top 10 Countries with the Highest Fatality Rate")
plt.xlabel("Country")
plt.ylabel("Fatality Rate (%)")
plt.show()

print("\nAnalysis Completed! 📊✅")

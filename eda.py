import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("=== CODEALPHA TASK 2: EDA ON TITANIC DATASET ===")

# 1. LOAD DATASET
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# 2. BASIC INFO
print("\n1. FIRST 5 ROWS:")
print(df.head())

print("\n2. DATASET INFO:")
print(df.info())

print("\n3. MISSING VALUES:")
print(df.isnull().sum())

print("\n4. STATISTICAL SUMMARY:")
print(df.describe())

# 3. KEY INSIGHTS
print("\n5. KEY INSIGHTS:")
print(f"Total Passengers: {len(df)}")
print(f"Survival Rate: {df['Survived'].mean()*100:.2f}%")
print(f"Average Age: {df['Age'].mean():.2f}")
print(f"Average Fare: ${df['Fare'].mean():.2f}")

# 4. DATA CLEANING
df['Age'].fillna(df['Age'].mean(), inplace=True) # Fill missing age

# 5. VISUALIZATIONS
plt.figure(figsize=(14, 5))

# Chart 1: Survival Count
plt.subplot(1, 3, 1)
sns.countplot(x='Survived', data=df)
plt.title('Survival Count\n0=Did Not Survive, 1=Survived')
plt.xlabel('Survived')
plt.ylabel('Count')

# Chart 2: Survival by Gender
plt.subplot(1, 3, 2)
sns.countplot(x='Sex', hue='Survived', data=df)
plt.title('Survival by Gender')
plt.xlabel('Gender')

# Chart 3: Age Distribution
plt.subplot(1, 3, 3)
sns.histplot(df['Age'], bins=30, kde=True)
plt.title('Age Distribution')
plt.xlabel('Age')

plt.tight_layout()
plt.savefig('eda_charts.png')
print("\nCharts saved as 'eda_charts.png'")

# 6. SAVE CLEANED DATA
df.to_csv('titanic_cleaned.csv', index=False)
print("Cleaned data saved as 'titanic_cleaned.csv'")
print("\n=== EDA COMPLETE ===")
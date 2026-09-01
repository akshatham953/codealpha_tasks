import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("=== CODEALPHA TASK 3: DATA VISUALIZATION ===")

# 1. LOAD DATASET
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# 2. SET BEAUTIFUL STYLE
sns.set_style("whitegrid")
plt.figure(figsize=(15, 10))

# 3. CHART 1: Survival Rate by Gender
plt.subplot(2, 3, 1)
sns.barplot(x='Sex', y='Survived', data=df, palette='pastel')
plt.title('Survival Rate by Gender')
plt.ylabel('Survival Rate')
plt.ylim(0, 1)

# 4. CHART 2: Survival by Passenger Class
plt.subplot(2, 3, 2)
sns.barplot(x='Pclass', y='Survived', data=df, palette='muted')
plt.title('Survival Rate by Passenger Class')
plt.xlabel('Class: 1=Upper, 2=Middle, 3=Lower')
plt.ylabel('Survival Rate')
plt.ylim(0, 1)

# 5. CHART 3: Age Distribution by Survival
plt.subplot(2, 3, 3)
sns.histplot(data=df, x='Age', hue='Survived', bins=30, kde=True, palette='Set1')
plt.title('Age Distribution by Survival')
plt.xlabel('Age')

# 6. CHART 4: Fare vs Age Scatter Plot
plt.subplot(2, 3, 5)
sns.scatterplot(x='Age', y='Fare', hue='Survived', data=df, alpha=0.6, palette='coolwarm')
plt.title('Fare vs Age colored by Survival')
plt.xlabel('Age')
plt.ylabel('Fare ($)')

# 7. CHART 5: Correlation Heatmap
plt.subplot(2, 3, 6)
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Heatmap')

plt.tight_layout()
plt.savefig('visualization_dashboard.png', dpi=300)
print("\nDashboard saved as 'visualization_dashboard.png'")

print("\n=== VISUALIZATION COMPLETE ===")
print("5 Charts created successfully!")
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Step 1: Load dataset
df = pd.read_csv('Titanic_dataset_new.csv')
print("✅ Dataset Loaded Successfully!")
print(df.head())

# Step 2: Check for missing values
print("\n🔍 Missing values before cleaning:")
print(df.isnull().sum())

# Step 3: Handle missing values
df['Age'] = df['Age'].fillna(df['Age'].median())
df['Fare'] = df['Fare'].fillna(df['Fare'].mean())
df.dropna(subset=['Embarked'], inplace=True)

print("\n✅ Missing values handled!")
print(df.isnull().sum())

# Step 4: Encode categorical data
le = LabelEncoder()
df['Sex'] = le.fit_transform(df['Sex'])
df = pd.get_dummies(df, columns=['Embarked'], drop_first=True)

# Step 5: Normalize numerical columns
scaler = StandardScaler()
df[['Age', 'Fare']] = scaler.fit_transform(df[['Age', 'Fare']])

# Step 6: Visualize outliers
print("\n📈 Boxplot for Age")
sns.boxplot(x=df['Age'])
plt.show()

print("\n📈 Boxplot for Fare")
sns.boxplot(x=df['Fare'])
plt.show()

# Step 7: Save cleaned data
df.to_csv('titanic_cleaned.csv', index=False)
print("\n✅ Cleaned data saved as 'titanic_cleaned.csv'")

input("✅ Press Enter to exit...")

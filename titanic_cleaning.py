import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler

# Load the dataset with comma as separator
df = pd.read_csv('Titanic_dataset_new.csv', sep=",")  # <--- Add sep=","

# Continue your exploration
print(df.head())
print("Shape of data:", df.shape)
print(df.info())
print(df.isnull().sum())
print(df.describe())


#Label Encode 'Sex'
le = LabelEncoder()
df['Sex'] = le.fit_transform(df['Sex'])

# One-Hot Encode 'Embarked'
df = pd.get_dummies(df, columns=['Embarked'], drop_first=True)

# Let's check updated dataframe
print(df.head())


scaler = StandardScaler()
df[['Age', 'Fare']] = scaler.fit_transform(df[['Age', 'Fare']])

sns.boxplot(x=df['Age'])
plt.show()
sns.boxplot(x=df['Fare'])
plt.show()

df.to_csv('titanic_cleaned.csv', index=False)

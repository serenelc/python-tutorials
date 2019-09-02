import inline
import matplotlib
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
import seaborn as sns
import matplotlib.pyplot as plt

# Load the train and test datasets to create two DataFrames

train_url = "http://s3.amazonaws.com/assets.datacamp.com/course/Kaggle/train.csv"
train = pd.read_csv(train_url)
test_url = "http://s3.amazonaws.com/assets.datacamp.com/course/Kaggle/test.csv"
test = pd.read_csv(test_url)

# print("***** Train_Set *****")
# print(train.head())
# print("\n")
# print("***** Test_Set *****")
# print(test.describe())
#
# print(train.columns.values)

# See where values are missing for the data sets. K-Means does not support missing values in the data set we feed it
# print("*****In the train set*****")
# print(train.isna().sum())
# print("\n")
# print("*****In the test set*****")
# print(test.isna().sum())

# There are a couple of ways to handle missing values:
# Remove rows with missing values or Impute missing values
# Fill missing values with mean column values in the train set (Mean Imputation)
train.fillna(train.mean(), inplace=True)
# Fill missing values with mean column values in the test set
test.fillna(test.mean(), inplace=True)

# There are still missing values in the Cabin and Embarked columns because these values are non numeric

# Survival count with respect to the class
print(train[['Pclass', 'Survived']].groupby(['Pclass'], as_index=False).mean().sort_values(by='Survived',
                                                                                           ascending=False))
# Survival count with respect to gender
print(train[["Sex", "Survived"]].groupby(['Sex'], as_index=False).mean().sort_values(by='Survived', ascending=False))

# Plot age vs survival
g = sns.FacetGrid(train, col='Survived')
g.map(plt.hist, 'Age', bins=20)
# Plot class and age vs survival
grid = sns.FacetGrid(train, col='Survived', row='Pclass', height=2.2, aspect=1.6)
grid.map(plt.hist, 'Age', alpha=.5, bins=20)
grid.add_legend()

plt.show()

# We can drop these categories because they wouldn't affect the survival rate of the passengers so not relevant
train = train.drop(['Name', 'Ticket', 'Cabin', 'Embarked'], axis=1)
test = test.drop(['Name', 'Ticket', 'Cabin', 'Embarked'], axis=1)

# Now only sex remains as a non numeric field so we need to convert it into a numeric field.
# We will do this using LabelEncoder()
labelEncoder = LabelEncoder()
labelEncoder.fit(train['Sex'])
labelEncoder.fit(test['Sex'])
train['Sex'] = labelEncoder.transform(train['Sex'])
test['Sex'] = labelEncoder.transform(test['Sex'])

X = np.array(train.drop(['Survived'], 1).astype(float))
y = np.array(train['Survived'])

# We scale the data because the features in the data set contain different ranges so we scale
# the features to have the same range [0, 1]
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

# Want to cluster the passenger records into 2: Survived or Not survived
kmeans = KMeans(n_clusters=2, max_iter=600, algorithm='auto')
kmeans.fit(X_scaled)
KMeans(algorithm='auto', copy_x=True, init='k-means++', max_iter=600,
       n_clusters=2, n_init=10, n_jobs=1, precompute_distances='auto',
       random_state=None, tol=0.0001, verbose=0)

correct = 0
for i in range(len(X)):
    predict_me = np.array(X[i].astype(float))
    predict_me = predict_me.reshape(-1, len(predict_me))
    prediction = kmeans.predict(predict_me)
    if prediction[0] == y[i]:
        correct += 1

print(correct / len(X))

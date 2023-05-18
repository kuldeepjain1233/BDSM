import pandas as pd
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

data = pd.read_csv("C:/Users/cycob/Downloads/data.csv")

data.drop(["Unnamed: 32", "id"], axis=1, implace=True)

data.diagnosis = [1 if value == 'M' else 0 for value in data.diagnosis]

data["diagnosis"] = data['diagnosis'].astype("category",copy = False)
data["diagnosis"].value_counts().plot(kind="bar")

y = data["diagnosis"]
x = data.drop(["diagnosis"],axis=1)


scaler = StandardScaler()

x_scaled = scaler.fit_transform(x)

x_train, x_test, y_train, y_test = train_test_split(x_scaled, y, test_size=0.30, random_state=42)

lr = LogisticRegression()

lr.fit(x_train, y_train)

y_pred = lr.predict(x_test)

print(y_pred)
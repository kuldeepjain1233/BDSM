import pandas as pd
import seaborn as sns
import joblib
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from tkinter import *
from tkinter import filedialog
import matplotlib.pyplot as plt

def b_cancer():

    # data = pd.read_csv(".\CSV\\brest-dataset\data.csv")
    print("ENTER DATASET TO BE TESTED:")
    data= pd.read_csv(filedialog.askopenfilename(filetypes=(("Text files", "*.txt"), ("CSV files", "*.csv"), ("Image files", "*.png;*.jpg;*.jpeg"))))
    data.drop(["Unnamed: 32", "id"], axis=1, inplace=True)

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
    joblib.dump(lr, 'breast_can')

    y_pred = lr.predict(x_test)
    nm=0
    m=0
    for i in y_pred:
        if i==0:
            nm+=1
        if i==1:
            m+=1


    print(metrics.classification_report(y_pred,y_test))
    print("accuracy:"+str(lr.score(x_test,y_test)))

    x1=['malignant','non-malignant']
    h=[m,nm]
    c=['red','green']
    plt.bar(x1,h,width=0.5,color=c)
    plt.xlabel("Cancer diagnosis")
    plt.ylabel("Number")
    plt.title("Cancer Detection")
    plt.show()
# b_cancer()

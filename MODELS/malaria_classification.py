import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier,AdaBoostClassifier
from sklearn import metrics
from sklearn.metrics import accuracy_score,classification_report
import joblib
import cv2


##step 1 Load dataset

dataframe = pd.read_csv("csv/datasetmain.csv")
# print(dataframe.head())
dataframe2=pd.read_csv("csv/test.csv")
# print(dataframe2.head())

#step2: Split into train and test data

x=dataframe.drop(["Label"],axis=1)
x1=dataframe2.drop(["Label"],axis=1)
y=dataframe["Label"]
y1=dataframe2["Label"]
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)
x_test=x1
y_test=y1
# print(x_test)
# print(y_test)

##Step4: Build a model

model = RandomForestClassifier(n_estimators=100,max_depth=5)
model.fit(x_train,y_train)
joblib.dump(model,"rf_malaria_100_5")

##Step5: Make predictions and get classification report

predictions = model.predict(x_test)
# print(x_test.head(1))
print(metrics.classification_report(predictions,y_test))
print(model.score(x_test,y_test))
ii=0
p=0
for i in predictions:
    if i=='Parasitized':
        p+=1
    if i=='Uninfected':
        ii+=1
if ii>=p:
    print('Hence we can conclude that you are Uninfected')
else:
    print('Hence we can conclude that you are Parasitized')







# dataframe = pd.read_csv("csv/datasetmain.csv")
# # print(dataframe.head())
# dataframe2=pd.read_csv("csv/test.csv")
# # print(dataframe2.head())
# x=dataframe.drop(["Label"],axis=1)
# x1=dataframe2.drop(["Label"],axis=1)
# y=dataframe["Label"]
# y1=dataframe2["Label"]
# x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)

# x_train = x_train/255.0
# x_test = x_test/255.0
# model=RandomForestClassifier()
# model.fit(x_train,y_train)
# print(x_test)
# y_pred=model.predict(x_test)
# # print(y_pred)
# # accuracy_score(y_pred,y_test)
# # print(classification_report(y_pred,y_test))

# img_path="C:\Big_data\FC42-BDSM\Aashish\malaria\cell_images\Parasitized\C33P1thinF_IMG_20150619_114756a_cell_179.png"
# img_arr=cv2.imread(img_path)
# print(img_arr.shape)
# # img_arr=cv2.resize(img_arr,(32,32))
# nx, ny, nrgb = img_arr.shape
# img_arr2 = img_arr.reshape(1,(nx*ny*nrgb))
# print(img_arr2)
# # classes = ["Parasitized","Uninfected"]
# ans=model.predict(img_arr2)
# # print(ans[0])
import pandas as pd
import pickle
import numpy as np

data=pd.read_csv('C:\Big_data\FC42-BDSM\Aashish\house_price\csv\Cleaned_data.csv')
pipe=pickle.load(open("RidgeModel.pkl",'rb'))


locations=sorted(data['location'].unique())

for location in locations:
    print(location)
loc=int(input('enter choice:'))
bhk=float(input('enter bhk size required:'))
bath=float(input('enter number of bathrooms required:'))
sqft=int(input('enter the total square feet:'))

# print(locations[loc],bhk,bath,sqft)

input=pd.DataFrame([[locations[loc],bhk,bath,sqft]],columns=['location','total_sqft','bath','bhk'])

prediction=pipe.predict(input)[0]*10000

print("Rs."+str(np.round(abs(prediction),2)))
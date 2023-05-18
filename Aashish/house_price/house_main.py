import pandas as pd
import pickle
import numpy as np
from tkinter import *  

base = Tk()  
base.geometry("500x500")  
base.title("House Price Prediction")  

data=pd.read_csv('C:\Big_data\FC42-BDSM\Aashish\house_price\csv\Cleaned_data.csv')
pipe=pickle.load(open("RidgeModel.pkl",'rb'))


locations=sorted(data['location'].unique())

# for location in locations:
#     print(location)
# loc=int(input('enter choice:'))
# bhk=float(input('enter bhk size required:'))
# bath=float(input('enter number of bathrooms required:'))
# sqft=int(input('enter the total square feet:'))


lb1= Label(base, text="Enter Name", width=10, font=("arial",12))  
lb1.place(x=20, y=120)  
en1= Entry(base)  
en1.place(x=200, y=120)  
  
lb3= Label(base, text="Enter Email", width=10, font=("arial",12))  
lb3.place(x=19, y=160)  
en3= Entry(base)  
en3.place(x=200, y=160)  
  
lb4= Label(base, text="Contact Number", width=13,font=("arial",12))  
lb4.place(x=19, y=200)  
en4= Entry(base)  
en4.place(x=200, y=200)  
  
lb5= Label(base, text="Select Gender", width=15, font=("arial",12))  
lb5.place(x=5, y=240)  
vars = IntVar()  
Radiobutton(base, text="Male", padx=5,variable=vars, value=1).place(x=180, y=240)  
Radiobutton(base, text="Female", padx =10,variable=vars, value=2).place(x=240,y=240)  
Radiobutton(base, text="others", padx=15, variable=vars, value=3).place(x=310,y=240) 

cv = StringVar()  
drplist= OptionMenu(base, cv, *locations)  
drplist.config(width=15)  
cv.set("Shampura")  
lb2= Label(base, text="Select Location", width=13,font=("arial",12))  
lb2.place(x=14,y=280)  
drplist.place(x=200, y=275)  

Button(base, text="Register", width=10).place(x=200,y=400)  

base.mainloop()  



# print(locations[loc],bhk,bath,sqft)

# input=pd.DataFrame([[locations[loc],bhk,bath,sqft]],columns=['location','total_sqft','bath','bhk'])

# prediction=pipe.predict(input)[0]*10000

# print("Rs."+str(np.round(abs(prediction),2)))
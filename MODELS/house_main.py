import pandas as pd
import pickle
import numpy as np
from tkinter import *  

def house():
    base = Tk()  
    base.geometry("500x500")  
    base.title("House Price Prediction") 

    # data=pd.read_csv('C:\Big_data\MAIN_PROJ\FC42-BDSM\CSV\Bengaluru_Cleaned_data.csv')
    data=pd.read_csv('.\CSV\house-dataset\Bengaluru_Cleaned_data.csv')
    pipe=pickle.load(open("RidgeModel.pkl",'rb'))


    locations=sorted(data['location'].unique())

    # def click():
        # e.config(state=NORMAL)
        # e.delete(0,END)

    e=Entry(base,width=30,borderwidth=8)
    # e.insert(0,"Enter BHK")
    # e.config(state=DISABLED)
    # e.bind("<Button-1>",click)
    e.pack()
    e_placeholder=Label(base,text='Enter bhk:',fg='grey')
    e_placeholder.place(x=55,y=5)
    e2=Entry(base,width=30,borderwidth=8)
    e2.pack()
    e2_placeholder=Label(base,text='Enter bathrooms:',fg='grey')
    e2_placeholder.place(x=35,y=35)
    e3=Entry(base,width=30,borderwidth=8)
    e3.pack()
    e2_placeholder=Label(base,text='Enter total_sqft:',fg='grey')
    e2_placeholder.place(x=35,y=70)
    bhk,bath,sqft,loc='','','',''
    cv = StringVar()  
    drplist= OptionMenu(base, cv, *locations)
    drplist.pack()  
    cv_placeholder=Label(base,text='Select Location:',fg='grey')
    cv_placeholder.place(x=100,y=105)
    # drplist.config(width=25)  
    cv.set("Shampura")  
   

    def myClick():
        global bhk,bath,sqft,loc
        bhk=e.get()
        bath=e2.get()
        sqft=e3.get()
        loc=cv.get()

        input=pd.DataFrame([[loc,float(bhk),float(bath),int(sqft)]],columns=['location','total_sqft','bath','bhk'])
        prediction=pipe.predict(input)[0]*10000
        out="Rs."+str(np.round(abs(prediction),2))

        myLabel=Label(base,text=out)
        myLabel.pack()


    myButton = Button(base,text="Submit",command=myClick)
    myButton.pack()
    print(bhk)

    base.mainloop()  



    
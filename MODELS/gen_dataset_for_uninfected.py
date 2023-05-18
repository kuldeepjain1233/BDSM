import cv2,os
import numpy as np
import csv
import glob

dir_path2=r'C:\Big_data\FC42-BDSM\Aashish\malaria\cell_images\Uninfected/'
dirList2=[]
for path in os.listdir(dir_path2):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path2, path)):
        dirList2.append("cell_images/Uninfected/"+path)



label2="Unaffected"


file2 = open("C:\Big_data\FC42-BDSM\Aashish\malaria\csv\dataset2.csv","a")
dirList2.pop(13779)
for img_path in dirList2:
    im = cv2.imread(img_path)
    im=cv2.GaussianBlur(im,(5,5),2)
    im_gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    ret,thresh=cv2.threshold(im_gray,127,255,0)
    contours,_=cv2.findContours(thresh,1,2)

    file2.write(label2)
    file2.write(",")

    for i in range(5):
        try:
            area=cv2.contourArea(contours[i])
            file2.write(str(area))
        except:
            file2.write("0")
        file2.write(",")
    file2.write("\n")
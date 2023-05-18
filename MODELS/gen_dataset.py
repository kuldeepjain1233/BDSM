import cv2,os
import numpy as np
import csv
import glob

dir_path=r'C:\Big_data\FC42-BDSM\Aashish\malaria\cell_images\Parasitized/'
dirList=[]
for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        dirList.append("cell_images/Parasitized/"+path)

label="Parasitized"

file = open(".\csv\dataset.csv","a")

dirList.pop(13763)

for img_path in dirList:
    im = cv2.imread(img_path)
    im=cv2.GaussianBlur(im,(5,5),2)
    im_gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    ret,thresh=cv2.threshold(im_gray,127,255,0)
    contours,_=cv2.findContours(thresh,1,2)

    file.write(label)
    file.write(",")

    for i in range(5):
        try:
            area=cv2.contourArea(contours[i])
            file.write(str(area))
        except:
            file.write("0")
        file.write(",")
    file.write("\n")
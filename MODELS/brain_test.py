import numpy as np
import matplotlib.pyplot as plt
import os
import math
import shutil
import glob
import tensorflow.compat.v1 as tf
import keras
import joblib
import pickle

# from sklearn.externals import joblib
from keras.layers import Conv2D, MaxPool2D, Dropout, Flatten, Dense, BatchNormalization, GlobalAveragePooling2D
from keras.models import Sequential
from keras.preprocessing.image import ImageDataGenerator
from keras.callbacks import ModelCheckpoint, EarlyStopping
# from keras.preprocessing.image import load_img, img_to_array
# import tensorflow as tf
from tensorflow.keras.utils import load_img
from tensorflow.keras.utils import img_to_array
from tkinter import *
from tkinter import filedialog

# tf.disable_v2_behavior()

# config = tf.ConfigProto(device_count={'GPU':1,'CPU':4})
# sess = tf.Session(config=config)
# keras.backend.set_session(sess)

# with open('model_pickle','rb') as f:


def br_test():
    mf = joblib.load('brain_can')
    print("ENTER TESTING IMAGE:")
    # test_path = "D:/brain_tumor_data_set/Healthey/Not Cancer  (1).jpg"
    test_path = filedialog.askopenfilename(filetypes=(
        ("Text files", "*.txt"), ("CSV files", "*.csv"), ("Image files", "*.png;*.jpg;*.jpeg")))

    img_final = load_img(test_path, target_size=(224, 224))
    input_arr = img_to_array(img_final)/255

    # plt.imshow(input_arr)
    plt.show()

    input_arr.shape

    input_arr = np.expand_dims(input_arr, axis=0)

    pred = mf.predict(input_arr)[0][0]
    print(pred)

    if pred <= 0.5:
        print("The MRI is having a tumor")
    else:
        print("MRI is not having a tumor")
# br_test()

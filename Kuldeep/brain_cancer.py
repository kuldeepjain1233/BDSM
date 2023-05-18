import numpy as np
import matplotlib.pyplot as plt
import os
import math
import shutil
import glob
import tensorflow.compat.v1 as tf
import keras

from keras.layers import Conv2D, MaxPool2D, Dropout, Flatten, Dense, BatchNormalization, GlobalAveragePooling2D
from keras.models import Sequential
from keras.preprocessing.image import ImageDataGenerator
from keras.callbacks import ModelCheckpoint, EarlyStopping
# from keras.preprocessing.image import load_img, img_to_array

tf.disable_v2_behavior()

config = tf.ConfigProto(device_count={'GPU':1,'CPU':4})
sess = tf.Session(config=config)
keras.backend.set_session(sess)


import keras

ROOT_DIR = "C:/Users/cycob/Downloads/brain_tumor_data_set"
# test_dataset = a
number_of_images = {}

for dir in os.listdir(ROOT_DIR):
    number_of_images[dir] = len(os.listdir(os.path.join(ROOT_DIR, dir)))


def datafolder(p,split):
    if not os.path.exists("./Kuldeep"+p):
        os.mkdir("./Kuldeep"+p)

        for dir in os.listdir(ROOT_DIR):
            os.makedirs("./Kuldeep"+p+"./Kuldeep"+dir)
        
            for img in np.random.choice(a=os.listdir(os.path.join(ROOT_DIR,dir)), size = (math.floor(split*number_of_images[dir])-5),replace=False):
                o = os.path.join(ROOT_DIR,dir,img)
                d = os.path.join("./Kuldeep"+p,dir)
                shutil.copy(o, d)
                os.remove(o)

    else:
        print("folder exist's")

datafolder("train", 0.7)
datafolder("val", 0.15)
datafolder("test", 0.15)

model = Sequential()

model.add(Conv2D(filters = 16, kernel_size=(3,3), activation='relu',input_shape=(224,224,3)))

model.add(Conv2D(filters=36, kernel_size=(3,3), activation='relu'))
model.add(MaxPool2D(pool_size=(2,2)))

model.add(Conv2D(filters=64,kernel_size=(3,3),activation='relu'))
model.add(MaxPool2D(pool_size=(2,2)))

model.add(Conv2D(filters=128,kernel_size=(3,3),activation='relu'))
model.add(MaxPool2D(pool_size=(2,2)))

model.add(Dropout(rate=0.25))

model.add(Flatten())
model.add(Dense(units=64, activation='relu'))
model.add(Dropout(rate=0.25))
model.add(Dense(units=1, activation='sigmoid')) 

model.compile(optimizer='adam',loss=keras.losses.binary_crossentropy, metrics=['accuracy'])

def preprocessingImages1(path):
    image_data = ImageDataGenerator(zoom_range=0.2,shear_range=0.2,rescale=1/255,horizontal_flip=True)
    image = image_data.flow_from_directory(directory=path,target_size=(224,224),batch_size=32,class_mode='binary')

    return image


def preprocessingImages2(path):
    image_data = ImageDataGenerator(rescale=1/255)
    image = image_data.flow_from_directory(directory=path,target_size=(224,224),batch_size=32,class_mode='binary')

    return image

train_data = preprocessingImages1("C:/Users/cycob/Desktop/FC42-BDSM/Kuldeep/train")

val_data = preprocessingImages2("C:/Users/cycob/Desktop/FC42-BDSM/Kuldeep/val")

test_data = preprocessingImages2("C:/Users/cycob/Desktop/FC42-BDSM/Kuldeep/train")

es = EarlyStopping(monitor="val_accuracy", min_delta=0.01,patience=3,verbose=1,mode='auto')

mc = ModelCheckpoint(monitor="val accuracy", filepath="./Kuldeep/bestmodel.h5",verbose=1,save_best_only=True,mode='auto')

cd = [es,mc]

hs = model.fit_generator(generator=train_data,steps_per_epoch=8, epochs=10, verbose = 1,validation_data=val_data, validation_steps = 16, callbacks=cd)

h = hs.history

plt.plot(h['accuracy'])
plt.plot(h['val_accuracy'])

plt.title("acc vs val-acc")

# test_path = abc

# img_final = load_img(path,target_size=(224,224))
# input_arr = img_to_array(img_final)/255

# plt.imshow(input_arr)
# plt.show()

# input_arr.shape

# input_arr = np.expand_dims(input_arr,axis=0)

# pred = model.predict_classes(input_arr)[0][0]

# if pred == 0:
#     print("The MRI is having a tumor")
# else:
#     print("MRI doesnt have a tumor")


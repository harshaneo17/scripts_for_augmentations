###Author : Harsha Arya###
###Date   : 22-06-2020###

import numpy as np
import keras
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing.image import array_to_img
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import load_img
import os
import cv2

datagen = ImageDataGenerator(rotation_range =15, #function used to generate augmentaions of images from keras
                     width_shift_range = 0.2,
                     height_shift_range = 0.2,
                     rescale=1./255,
                     shear_range=0.2,
                     zoom_range=0.2,
                     horizontal_flip = True,
                     fill_mode = 'nearest',
                     data_format='channels_last',
                     brightness_range=[0.5, 1.5])

imgs = os.listdir('C:\\Users\\ASUS\\Documents\\project object detect\\data\\data3_basic') #path to your image directory

for img in imgs:
    img=cv2.imread('C:\\Users\\ASUS\\Documents\\project object detect\\data\\data3_basic'+"\\"+img)
    x = img_to_array(img)
    x = x.reshape((1,) + x.shape)

    i = 0
    for batch in datagen.flow (x, batch_size=1, save_to_dir =r'C:\\Users\\ASUS\\Documents\\project object detect\\data\\data3_basic', save_prefix ='aug', save_format='jpg'): #path to image directory
        i+=1
        if i>5:
            break

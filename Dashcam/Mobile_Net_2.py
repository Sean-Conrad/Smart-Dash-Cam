# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 01:28:41 2021

@author: Eric
"""
#https://www.youtube.com/watch?v=OO4HD-1wRN8
#https://stackoverflow.com/questions/56594290/how-to-add-class-to-existing-model
#https://pythonprogramming.net/introduction-use-tensorflow-object-detection-api-tutorial/
#https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/using_your_own_dataset.md
import numpy as np
import keras
from keras import backend as K
from keras.models import Sequential
from keras.layers import Activation
import sklearn
from keras.layers.core import Dense, Flatten
from keras.optimizers import Adam
from keras.metrics import categorical_crossentropy
from keras.preprocessing.image import ImageDataGenerator
from keras.layers.normalization import BatchNormalization
from keras.layers.convolutional import*

from keras.preprocessing import image
from keras.models import Model
from keras.applications import imagenet_utils
from sklearn.metrics import confusion_matrix
import itertools
from matplotlib import pyplot as plt
import matplotlib.pyplot as plt
from IPython.display import Image
import tensorflow as tf
from object_detection.utils import dataset_util
import cv2
import os
import shutil
import random
from sklearn.metrics import plot_confusion_matrix
import itertools



# path names in directory
train_path = 'Car-Dataset/train'
valid_path = 'Car-Dataset/valid'
test_path = 'Car-Dataset/test'

# pulling the pictures from each respective folder in path
train_batches = ImageDataGenerator(preprocessing_function=keras.applications.mobilenet.preprocess_input).flow_from_directory(train_path, target_size=(224,224), batch_size=10)
valid_batches = ImageDataGenerator(preprocessing_function=keras.applications.mobilenet.preprocess_input).flow_from_directory(valid_path, target_size=(224,224), batch_size=10)
test_batches = ImageDataGenerator(preprocessing_function=keras.applications.mobilenet.preprocess_input).flow_from_directory(test_path, target_size=(224,224), batch_size=10, shuffle = False)

# 
mobile = keras.applications.mobilenet.MobileNet()
mobile.summary()

# replace the last 6 layers of mobilenet with our layers
x = mobile.layers[-6].output
predictions = Dense(10, activation='softmax')(x)      # Dense to equal number of classes
model = Model(inputs=mobile.input, outputs=predictions)
model.summary()

for layer in model.layers[:-20]: # Change this value to tune accuracy
    layer.trainable = False
    
# Creates grid and maps accuracy
model.compile(Adam(lr=.0001), loss='categorical_crossentropy', metrics=['accuracy'])

model.fit_generator(
    train_batches, 
    steps_per_epoch = 120, # steps is total train images divided by batch size 
    validation_data = valid_batches, 
    validation_steps = 3, 
    epochs = 20, 
    verbose = 2)

def predict(input):
    try:
        x_prediction = tokenize.texts_to_matrix(input)
        q = model.predict(np.array([x_prediction[0],]))
        predicted_label = text_labels[np.argmax(q)]

        print("Prediction: " + predicted_label + "\n")

    except:
        return "Error"

"""
# *** Runs the epochs, gets the training and valid datasets and compares to the testing dataset
model.fit(
      x=train_batches
    , steps_per_epoch=len(train_batches)
    , validation_data=valid_batches
    , validation_steps=len(valid_batches)
    , epochs=10
    , verbose=2
)

"""
"""
model.fit_generator(
      train_batches
    , steps_per_epoch=len(train_batches)
    , validation_data=valid_batches
    , validation_steps=len(valid_batches)
    , epochs=10
    , verbose=2
)
"""

# putting back the updated layers  
test_labels = test_batches.classes
print(test_labels)
print(test_batches.class_indices)
#steps to equal total test images divided by test batch size
predictions = model.predict_generator(test_batches, steps=2, verbose=0)

q = model.predict(test_batches)
print("\nConfidence: ", q)

cm = confusion_matrix(test_labels, predictions.argmax(axis=1))
print(predictions.argmax(axis=1))
print(cm)
cm_plot_labels = ["Acura", "Aston Martin", "BMW", "Dodge"]
#plot_confusion_matrix(cm, cm_plot_labels)

model.save('Model')


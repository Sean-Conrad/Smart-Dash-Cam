# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 21:30:51 2021

@author: Eric
"""

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


def modelLoad():
    model = keras.models.load_model('Model')
    return model


def test(model):
    #model = keras.models.load_model('Model')
    test_path = 'Car-Dataset/test'
    test_batches = ImageDataGenerator(preprocessing_function=keras.applications.mobilenet.preprocess_input).flow_from_directory(test_path, target_size=(224,224), batch_size=10, shuffle = False)
    
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
    
    i = 0
    max = 0
    while i < len(q):
        if(q[0][i] > max):
            max = q[0][i]
        i = i + 1
    print(max)
    
    j = 0
    chosenMatch = -1
    if (max > 0.6):
        while j < len(cm):
            if cm[0][j] == 1:
                chosenMatch = j
            j = j + 1
    print("Match: ", chosenMatch)
    return chosenMatch

#model = modelLoad()
#test(model)


    
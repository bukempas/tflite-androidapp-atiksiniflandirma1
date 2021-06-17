# Install Model maker
!pip install -q tflite-model-maker

import os
 
import numpy as np
 
import tensorflow as tf
assert tf.__version__.startswith('2')
 
from tflite_model_maker import model_spec
from tflite_model_maker import image_classifier
from tflite_model_maker.config import ExportFormat
from tflite_model_maker.config import QuantizationConfig
from tflite_model_maker import image_classifier
from tflite_model_maker.image_classifier import DataLoader
 
import matplotlib.pyplot as plt
 
# Load input data specific to an on-device ML app (from Google Drive file - UygAtly_CompVsn_WasteClassification/atik_siniflandirma_veriseti)
data = DataLoader.from_folder('/content/drive/MyDrive/Colab Notebooks/UygAtly_CompVsn_WasteClassification/atik_siniflandirma_veriseti/train/')
training_data,validation_data = data.split(0.9)
test_data = DataLoader.from_folder('/content/drive/MyDrive/Colab Notebooks/UygAtly_CompVsn_WasteClassification/atik_siniflandirma_veriseti/test/')
print(len(training_data))
print(len(validation_data))
print(len(test_data))

model = image_classifier.create(training_data,shuffle=True,train_whole_model='True',model_spec='efficientnet_lite0',validation_data=validation_data, epochs=10)

# test the model with test_data 
loss, accuracy = model.evaluate(test_data)

# export the model in .tflite format
model.export(export_dir='/mm_ayiklama3')

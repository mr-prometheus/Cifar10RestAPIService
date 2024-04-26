from flask import Flask, render_template, request, redirect, url_for, send_from_directory,flash
# Keras
from keras.applications.imagenet_utils import preprocess_input, decode_predictions
from keras.models import load_model
from keras.preprocessing import image
from keras.utils import load_img, img_to_array
from keras.applications.mobilenet import MobileNet, preprocess_input
# Flask utils
from flask import Flask, redirect, url_for, request, render_template
from pickle import NONE
import numpy as np
import cv2
from flask_cors import CORS,cross_origin
import os

import tensorflow as tf
from tensorflow import keras
app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
MODEL_PATH = 'bestmodel.h5'
model = tf.keras.models.load_model('bestmodel.h5',compile = False)     
CLASS_NAMES = ["Airplane","Automobile","Bird","Cat","Deer","Dog","Frog","Horse","Ship","Truck"]
         
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/hello',methods = ['GET'])
def hello():
    return "Hello"

@app.route('/predict', methods=['GET', 'POST'])
@cross_origin(allow_headers=['Content-Type'])
def upload():
    if request.method == 'POST':

        """testing purpose"""
        filestr = request.files['file'].read()
        file_bytes = np.frombuffer(filestr, np.uint8)
        img = cv2.imdecode(file_bytes, cv2.IMREAD_UNCHANGED)
        img = cv2.resize(img,(32,32))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        x = img_to_array(img)
        x = preprocess_input(x)

   
        prediction = model.predict(x.reshape(1,32,32,3))
        output = np.argmax(prediction)
        predicted_class = CLASS_NAMES[output]
        max_prob = np.max(prediction)
        if max_prob >0.75:
            return {
            'class' : predicted_class,
            'confidence' : float(max_prob)
        }
        else:
            return NONE
    return None


if __name__ == '__main__':
   app.run(debug = True)


from app import app
from flask import request, jsonify
import cv2
from tensorflow.keras.models import load_model
from time import sleep
from keras.preprocessing.image import img_to_array
from keras.preprocessing import image
import numpy as np
import glob
import pandas as pd
import urllib.request
import os
from werkzeug.utils import secure_filename


UPLOAD_FOLDER = 'images/'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
classifier = load_model('model.h5')

emotion_labels = ['Senang ', 'Biasa ']

def predict(image):
    
    deteksi=[] 
    
    for i in range(len(image)):
        gray = cv2.cvtColor(image[i], cv2.COLOR_BGR2GRAY)
        faces = face_classifier.detectMultiScale(gray)
        for (x, y, w, h) in faces:
            cv2.rectangle(image[i], (x, y), (x + w, y + h), (0, 255, 255), 2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_gray = cv2.resize(roi_gray, (48, 48), interpolation=cv2.INTER_AREA)

            if np.sum([roi_gray]) != 0:
                roi = roi_gray.astype('float')/255.0
                roi = img_to_array(roi)
                roi = np.expand_dims(roi, axis=0)

                prediction = classifier.predict(roi)[0]
            
                label = emotion_labels[prediction.argmax()]
                label_position = (x, y)
                cv2.putText(image[i], label, label_position, cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                deteksi.append(label)
                print(label)
            else:
                cv2.putText(image[i], 'No Faces', (30, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    print(deteksi)
    return deteksi
    

def jumlah(deteksi):
    df = pd.DataFrame(deteksi)
    jumlah = pd.value_counts(df[0])
    jumlah

    persen = pd.value_counts(df[0], normalize = True).mul(100).round(1).astype(str)+'%'
    
    return persen

def load_gambar():
    return [cv2.imread(file) for file in glob.glob("images/*")]


def result():
    if 'image' not in request.files:
        resp = jsonify({'msg': "No body image attached in request"})
        resp.status_code = 501
        return resp
    images = request.files.getlist('image')
    
    for image in images:

        # print(image.filename)
        if image.filename == '':
            resp = jsonify({'msg': "No file image selected"})
            resp.status_code = 404
            return resp
        error = {}
        success = False


        if image and allowed_file(image.filename):
            filename = secure_filename(image.filename)
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            success = True
            print('ini filename', filename)
        else:
            error[image.filename] = "File type is not allowed"

        if success and error:
            error['Message'] = "File not uploaded"
            resp = jsonify(error)
            resp.status_code = 500
            return resp
        if success:
            try:
                img = load_gambar()

                deteksi = predict(img)
                print('ini deteksi')
                output= jumlah(deteksi)
                # print(output[0], output[1])
                # print(filename)
                os.remove(UPLOAD_FOLDER+'/'+filename)

                return jsonify({
                    'status': 200,
                    'msg': "Success get predict emotion",
                    'senang': output[0],
                    'biasa':output[1]
                })
            except Exception as e:
                resp = {

                    'status': 500,
                    'msg': "Failed get predict emotion",
                    'Error': "Image yang masukan bukan wajah"

                }
                error = jsonify(resp)
                error.status_code = 500
                return error
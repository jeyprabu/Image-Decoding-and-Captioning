import cv2
import os
from flask import Flask, request, render_template
from flask_uploads import UploadSet, configure_uploads, IMAGES
from utility import caption
from feature import detect_edges_and_corners
from anomaly import anomalies

path = 'static/img'
app = Flask(__name__)

photos = UploadSet('photos',IMAGES)
app.config['UPLOADED_PHOTOS_DEST'] = 'static/img'
configure_uploads(app,photos)

@app.route("/",methods=["GET", "POST"])
def homepage():
    return render_template('homepage.html')

@app.route("/upload",methods=["GET","POST"])
def upload():
    p=None
    result = None
    action = request.form.get('action', 'upload')  
    if request.method == "POST" and 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        file_path = os.path.join(path, filename)
        if action == 'upload':
            p = path+'/'+filename
            result = caption(file_path)
        elif action == 'feat':
            image = cv2.imread(file_path) 
            if image is None:
                return render_template('upload.html', cp="Error: Unable to load image", src=None)
            p = detect_edges_and_corners(image, filename)
            result = "Features"
        elif action == "ano" and 'photo2' in request.files:
            filename1 = photos.save(request.files['photo2'])
            file_path1 = os.path.join(path, filename1)
            p = anomalies(file_path1,file_path, filename1)
            result = "Anomalies"
    return render_template('upload.html', cp=result, src=p)

@app.route('/developer',methods=["GET","POST"])
def developer():
    return render_template('dev.html')

if __name__ == '__main__':
    app.run()

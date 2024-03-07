# Image-Decoding-and-Captioning
This project deals with image processing. It mainly revolves around generating captions for the uploaded image, detecting edges and corners with features and find anomalies based on comparison. Captioning is done using CNN and LSTM. Edges are detected using Canny Edge Detection algorithm, corners are found using Harris Corner Algorithm and anomalies are found using absolute pixel difference and thresholding.<br>
CNN and LSTM Model for captioning.
To download captioning dataset, visit<br>
<a href="https://github.com/jbrownlee/Datasets/releases/download/Flickr8k/Flickr8k_Dataset.zip">Flickr_8K Dataset</a>
<a href="https://github.com/jbrownlee/Datasets/releases/download/Flickr8k/Flickr8k_text.zip">Flickr_8K Text</a><br>
![cnn and lstm](https://github.com/jeyprabu/Image-Decoding-and-Captioning/assets/135853635/07e52e50-2b2d-4688-8ca9-ce75afdc136b)
<br>
To install the modules, run the following command.<br>
```pip install -r requirements.txt```<br>
Once installed, run<br>
```flask run``` <br>
to run ap.py
<br><br>


![Screenshot (152)](https://github.com/jeyprabu/Image-Decoding-and-Captioning/assets/135853635/27f5de09-7629-41ee-8833-22a3767b9a88)
![Screenshot (153)](https://github.com/jeyprabu/Image-Decoding-and-Captioning/assets/135853635/d0931379-47f8-49a9-9b88-c80cad94f873)
![Screenshot (154)](https://github.com/jeyprabu/Image-Decoding-and-Captioning/assets/135853635/9d441c68-fe8b-4198-bb29-af52215bec62)
![Screenshot (155)](https://github.com/jeyprabu/Image-Decoding-and-Captioning/assets/135853635/0c00c512-4478-40de-b8d7-7c4ee4266a86)
![Screenshot (156)](https://github.com/jeyprabu/Image-Decoding-and-Captioning/assets/135853635/c391fa1f-a41e-48a7-b1d8-91b6ff2ad485)


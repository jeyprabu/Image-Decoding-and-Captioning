# Image-Decoding-and-Captioning
This project deals with image processing. It mainly revolves around generating captions for the uploaded image, detecting edges and corners with features and find anomalies based on comparison. Captioning is done using CNN and LSTM. Edges are detected using Canny Edge Detection algorithm, corners are found using Harris Corner Algorithm and anomalies are found using absolute pixel difference and thresholding.<br>
CNN and LSTM Model for captioning.<br><br>
Python - 3.10<br><br>
To download captioning dataset, visit<br>
<a href="https://github.com/jbrownlee/Datasets/releases/download/Flickr8k/Flickr8k_Dataset.zip">Flickr_8K Dataset</a>
<a href="https://github.com/jbrownlee/Datasets/releases/download/Flickr8k/Flickr8k_text.zip">Flickr_8K Text</a><br>
![cnn and lstm](https://github.com/jeyprabu/Image-Decoding-and-Captioning/assets/135853635/07e52e50-2b2d-4688-8ca9-ce75afdc136b)
<br>
Before installing modules, create an environment. To create it run the command<br>
```python -m venv .env```<br>
Enter environment<br>
```cd .env```<br>
To clone repository, run<br>
```git clone https://github.com/jeyprabu/Image-Decoding-and-Captioning.git```<br>
Then, <br>
```cd Image-Decoding-and-Captioning```<br>
To install the modules, run the following command.<br>
```pip install -r requirements.txt```<br>
Once installed, run the app<br>
```flask run``` or ```python app.py```
<br><br>


![Screenshot (152)](https://github.com/jeyprabu/Image-Decoding-and-Captioning/assets/135853635/27f5de09-7629-41ee-8833-22a3767b9a88)
![Screenshot (153)](https://github.com/jeyprabu/Image-Decoding-and-Captioning/assets/135853635/d0931379-47f8-49a9-9b88-c80cad94f873)
![Screenshot (210)](https://github.com/jeyprabu/Image-Decoding-and-Captioning/assets/135853635/d79ee1fb-712b-4c4e-bf8b-ca9b4d06026d)
![Screenshot (211)](https://github.com/jeyprabu/Image-Decoding-and-Captioning/assets/135853635/77e21e6d-ab65-4ecf-b1c0-6d68706eb64c)



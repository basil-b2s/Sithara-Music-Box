![BFH Banner](https://trello-attachments.s3.amazonaws.com/542e9c6316504d5797afbfb9/542e9c6316504d5797afbfc1/39dee8d993841943b5723510ce663233/Frame_19.png)
# Sithara Song Generator
<h1>" സിത്താര ചേച്ചീടെ പാട്ടുപെട്ടി "</h1>
This is basically a lyrics generator build using NLP, that will provide you the lyrics of famous singer predominant in the malayalam industry Ms.Sithara Krishnakumar using the pre-trained model. Enter the first few words of the song and lyrics will be displayed to you. Click <a href="https://sithara-lyrics-generator.herokuapp.com/">here</a> to view the website.

## Team members
1. <a href="https://github.com/basil-b2s">Basil Saji</a>
2. <a href="https://github.com/SurabhiSuresh22">Surabhi S</a>
 
## Team Id
BFH/rec57gyR9gEQFKfqU/2021

## Link to product walkthrough
[link to video]

## How it Works ?
This project was build as part of Tinkerhub Build From Home learning initiative.<br>
The model is built using LSTM architecture. Code written in Python language. For collecting the dataset, we downloaded the lyrics (in manglish) of Sitara songs from the internet. Flask framework is used to deploy this machine learning model. Code can be found <a href="https://github.com/basil-b2s/Sithara-Music-Box/blob/master/app.py">here</a>.The github repository containing files of this project was connected to Heroku Platform. The link to completely deployed web application can be found by checking below.The frontend of web page is created using simple HTML and CSS. Source code for the frontend is present <a href="https://github.com/basil-b2s/Sithara-Music-Box/tree/master/templates">here</a> in the folder. Data preprocessed using keras tokenizer and sequence padding to feed into the model. And the model was trained using LSTM architecture and tensorflow. The notebook for text preprocessing can be found <a href="https://github.com/basil-b2s/Sithara-Music-Box/blob/master/Text%20Preprocessing.ipynb">here</a> and for the model training <a href="https://github.com/basil-b2s/Sithara-Music-Box/blob/master/Lyrics%20Generator.ipynb">here</a>.

Check out the deployed web app by clicking <a href="https://sithara-lyrics-generator.herokuapp.com/">this</a> link. Enter first few words of the Sithara'S song and the model will generate its lyrics. Hope you'll like it.<br>

1. On loading the web page, in the input box, enter the first few words of the song you want the lyrics of. Then click the Generate button , this will direct you to another page in the same tab that shows the lyrics of the song. 

2. To get back to the initial page(home.html) press the Back button. Now you can search for some other songs you want. This is the predict.html page.


## Live Demo
![Screenshot (568)](https://user-images.githubusercontent.com/63139488/119367812-f6cfd580-bccf-11eb-8a5c-639104d15668.png)

## Libraries used
* pandas - 1.2.4

* numpy - 1.19.5

* flask - 2.0.0

* gunicorn - 20.1.0

* regex - 2020.11.13

* keras

* tensorflow-cpu

## How to configure
To run the project, load the python jupyter notebook found <a href="https://github.com/basil-b2s/Sithara-Music-Box/blob/master/Text%20Preprocessing.ipynb">here</a> in a Google Colab. Run this to check the steps, this file is imported as a module in the main notebook <a href="https://github.com/basil-b2s/Sithara-Music-Box/blob/master/Lyrics%20Generator.ipynb">Lyrics Generator</a> that contains the steps of model creation and training. Then upload the zip file found <a href="https://github.com/basil-b2s/Sithara-Music-Box/tree/master/Data">here</a> into the Google Colab. The project is now configured and is ready for running.

## How to Run
After configuring the project as told above, Run every single cell of the notebook in that order. Use the comments to understand when the model is training, validation and prediction script.

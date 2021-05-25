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
<a href="https://drive.google.com/file/d/1I1qvkrQjoVHvS1b73geUG1ND1TsPs1zz/view?usp=sharing">Code Explanation</a><br>

## How it Works ?

Web App  - <a href="https://sithara-lyrics-generator.herokuapp.com/">Sithara Song Generator</a><br>
 On loading the web page, in the input box, enter the first few words of the song you want the lyrics of. Then click the Generate button, this will direct you to another page in the same tab that shows the generated lyrics.<br>
The model is built using Bidirectional LSTM architecture. Code written in Python language. For collecting the dataset, we downloaded the lyrics (in manglish) of Sitara songs from the internet. Flask framework is used to deploy this machine learning model. Code can be found <a href="https://github.com/basil-b2s/Sithara-Music-Box/blob/master/app.py">here</a>.The github repository containing files of this project was connected to Heroku Platform. The frontend of web page is created using simple HTML and CSS. Source code for the frontend is present <a href="https://github.com/basil-b2s/Sithara-Music-Box/tree/master/templates">here</a> in the folder. And the Bidirectional LSTM architecture is created using tensorflow. The data which is preprocessed in the <a href="https://github.com/basil-b2s/Sithara-Music-Box/blob/master/Text%20Preprocessing.ipynb">Text Preprocessing notebook</a> is then provided to model training followed by tokenization using keras tokenizer  and sequence padding. You can find the Model training notebook <a href="https://github.com/basil-b2s/Sithara-Music-Box/blob/master/Lyrics%20Generator.ipynb">here</a> 

## Live Demo
Click the image below.
<a href="https://drive.google.com/file/d/11O2E2WpngtQo3OdwB3q3LIiz6Td_Lp_m/view?usp=sharing">![Screenshot (568)](https://user-images.githubusercontent.com/63139488/119367812-f6cfd580-bccf-11eb-8a5c-639104d15668.png)</a><br>

## Libraries used
* pandas - 1.1.4

* numpy - 1.19.5

* Flask - 1.1.2

* gunicorn - 20.1.0

* regex - 2020.11.13

* keras - 2.4.3

* tensorflow - 2.2.0+cpu

## How to configure
Download the above github repository in a colab notebook and unzip it. Install the files in requirements.txt. Then Load the Lyrics generator Notebook.

## How to Run
After configuring the project as told above, Run every single cell of the notebook in that order.

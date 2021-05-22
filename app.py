from flask import Flask, request, render_template
import numpy as np
import pickle
import keras
import tensorflow
import re


app = Flask(__name__)

tokenizer = pickle.load(open("Models/tokenizer.pkl", "rb"))
model = tensorflow.keras.models.load_model('Models/model.h5')


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/predict", methods=["POST"])
def predict():

    if request.method == "POST":
        lyrics = request.form["lyrics"]
        lyrics = lyrics.lower()
        lyrics = re.sub("[^a-z ]", "", lyrics)

        for _ in range(35):

            tokenized = tokenizer.texts_to_sequences([lyrics])[0]
            padded_list = tensorflow.keras.preprocessing.sequence.pad_sequences(
                [tokenized], maxlen=7, padding="pre")
            prediction = model.predict_classes(padded_list, verbose=0)

            for word, index in tokenizer.word_index.items():
                if index == prediction:
                    pred_word = word
                    break
            lyrics += " " + pred_word

    return render_template("prediction.html", pred=lyrics)


if __name__ == "__main__":
    app.run(debug=True)

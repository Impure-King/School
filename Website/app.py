from flask import Flask, render_template, request
from model import load_save
import tensorflow as tf


app = Flask(__name__)

# Creating the home directory:
@app.route('/')
def home():
    return render_template('home.html', title="Home Page")


@app.route('/predict', methods = ["GET", "POST"])
def predict():
    if request.method == "POST":
        load_save()
        return render_template('predict.html', posts = '\static\generated.jpg', title = "Prediction Page", home = '/')
    else:
        return render_template('predict.html', title = 'Prediction Page', posts = '\static\generated.jpg', home = '/')

if __name__ == '__main__':
    app.run(debug = True)
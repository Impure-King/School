from flask import Flask, render_template, request
from model import load_save
import tensorflow as tf

# Resolving TensorFlow GPU issues:
devices = tf.config.list_physical_devices("GPU")
tf.config.experimental.set_memory_growth(devices[0], True)

app = Flask(__name__)

# Creating the home directory:
@app.route('/')
def home():
    return render_template('home.html')


@app.route('/predict', methods = ["GET", "POST"])
def predict():
    if request.method == "POST":
        load_save()
        return render_template('predict.html', posts = '\static\generated.jpg')
    else:
        return render_template('predict.html', title = 'Prediction Page', posts = '\static\generated.jpg')

if __name__ == '__main__':
    app.run(debug = True)
from flask import Flask, render_template, request
from model import generate_faces
import tensorflow as tf

# Resolving TensorFlow GPU issues:
devices = tf.config.list_physical_devices("GPU")
tf.config.experimental.set_memory_growth(devices[0], True)

app = Flask(__name__)
model = tf.keras.models.load_model(r'Website/weights/generator')

# Creating the home directory:
@app.route('/')
def home():
    return render_template('home.html')


@app.route('/predict', methods = ["GET", "POST"])
def predict():
    if request.method == "POST":
        generate_faces(model)
        return render_template('predict.html', posts = '\static\generated.jpg')
    else:
        return render_template('predict.html', title = 'Prediction Page', posts = '\static\generated.jpg')

if __name__ == '__main__':
    app.run(debug = True)
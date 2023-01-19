from flask import Flask, render_template, request
from model import build_generator, generate_faces

app = Flask(__name__)
model = build_generator(seed_size = 128)

# Creating the home directory:
@app.route('/')
def home():
    return render_template('home.html')

def load_save(model = model):
    model.load_weights("generator_weights-test.h5")
    generate_faces(model)

@app.route('/predict', methods = ["GET", "POST"])
def predict():
    if request.method == "POST":
        load_save(model)
        return render_template('predict.html', posts = '\static\generated.jpg')
    else:
        return render_template('predict.html', title = 'Prediction Page', posts = '\static\generated.jpg')

if __name__ == '__main__':
    app.run(debug = True)
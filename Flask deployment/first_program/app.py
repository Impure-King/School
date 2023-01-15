from flask import Flask

app = Flask(__name__)


# We are using the decorator to define the site and a function to show text.
@app.route('/')
@app.route('/home')
def hello():
    return "Hello World!"


if __name__ == "__main__":
    app.run(debug=True)

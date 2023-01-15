from flask import Flask

app = Flask(__name__)


# Having access to url elements while routing:
@app.route('/home/<string:name>/posts/<string:identity>', methods=["POST"])
def hello(name, identity):
    return "Welcome, " + name + ". In case you forgot, your id is " + identity + '.'


# Changing the request permissions:
@app.route('/only-get', methods=['GET'])
def get_req():
    return "You can only get the specific website."


if __name__ == "__main__":
    app.run(debug=True)

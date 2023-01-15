from flask import Flask, render_template

app = Flask(__name__)


#browsers can usually interpret any type of text. Including HTML texts.
@app.route('/')
def index():
    return render_template('home.html')


# Running the Debugging server
if __name__ == "__main__":
    app.run(debug=True)

# Normally you would use a template file to actually alter the code.
# Therefore, create a new folder and have a HTML code.

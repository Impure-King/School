from flask import Flask, render_template

app = Flask(__name__)

# Creating some dummy data in a list of dictionaries:
all_posts = [
    {
        'title': 'Welcome message',
        'content': 'Finding this site is quite a coincidence',
        'author': '~ Impure King'
    },

    {
        'title': 'What to do next',
        'content': "Leave immediately."
    }
]


@app.route('/')
def index():
    return render_template('home.html')


# Adding data using the post method:
@app.route('/messages')
def posts():
    return render_template('posts.html', posts=all_posts)


if __name__ == '__main__':
    app.run(debug=True)

# Using the templates we can extend HTML and pass some data.

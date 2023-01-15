from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
# Three slashes is relative path and 4 slashes is absolute path.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'

# Creating a database:
db = SQLAlchemy(app)

# Creating some model:
class UserBase(db.Model):
    
    # Creating an id with a distinct ids
    id = db.Column(db.Integer, primary_key=True)
    receiver = db.Column(db.String(30), nullable = False)
    title = db.Column(db.String(100), nullable = False, default = 'Impure King')
    message = db.Column(db.Text, nullable = False)
    
    # If nothing is provided, then the default is 'NA'
    sender = db.Column(db.String(20), nullable=False, default='N/A')
    date_posted = db.Column(db.DateTime, nullable=False, default = datetime.utcnow)

    def __repr__(self) -> str:
        return 'Blog Post' + str(self.id)


# Having a create all:
@app.before_first_request
def create_tables():
    db.create_all()

# Routings:

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/users/<string:name>', methods = ["GET"])
def index(name):
    return render_template('index.html', post=name)

# Allowing Posting:
@app.route('/posts', methods=['GET', 'POST'])
def posts():
    if request.method == 'POST':
        post_to = request.form['receiver']
        post_title = request.form['title']
        post_message = request.form['message']
        post_sender = request.form['sender']
        new_post = UserBase(receiver = post_to, title = post_title, message = post_message, sender = post_sender)
        db.session.add(new_post)
        db.session.commit()
        return redirect('/posts')
    else:
        all_posts = UserBase.query.order_by(UserBase.date_posted).all()
        return render_template('posts.html', posts = all_posts)

if __name__ == '__main__':
    app.run(debug=True)

# To run the database:
# $ python
# >>> from app import db, app
# >>> app.app_context().push()
# >>> db.create_all()

# To query:
# >>> from python import class_name
# >>> class_name.query.all()[i]

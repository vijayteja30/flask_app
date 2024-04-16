from flask import Flask,render_template
import os

app = Flask(__name__)

posts = [
    {
        "author" : "Corey Schafer",
        "title" : "Blog Post 1",
        "content" : "First Post Content",
        "date_posted" : "April 20 2021"
    },
    {
        "author" : "Jane Doe",
        "title" : "Blog Post 2",
        "content" : "Second Post Content",
        "date_posted" : "April 21 2021"
    }
]


@app.route('/home')
@app.route('/',methods = ['GET'])
def root_page():
    return render_template('home.html', posts = posts, title = "Home Page")

@app.route('/about')
def about():
    return render_template('about.html', title = "About Page")

@app.route('/hello/<string:value>')
def hello_world(value):
    return f'Hello World Value {value}'

@app.route('/live',methods = ['GET'])
def root_page():
    return "Api Trigger Success"

if __name__ == "__main__":
    app.run(debug=True)

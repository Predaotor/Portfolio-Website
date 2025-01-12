from flask import Flask, render_template, request, redirect, url_for
import logging 
from .config import Config

app = Flask(__name__)

app.config.from_object(Config)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')



if __name__ == '__main__':
    app.run(debug=True)
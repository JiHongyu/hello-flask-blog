from flask import Flask, render_template
from jinja2 import Template
from flask_pymongo import PyMongo
from flask_bootstrap import Bootstrap

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'web_db'

mongo = PyMongo(app)
bootstrap = Bootstrap(app)


@app.route('/')
@app.route('/home')
@app.route('/index')
def hello():
    return render_template('index.html')


@app.route('/contents')
def show_contents():
    contents = mongo.db.web_db.find()

    return render_template('conetents.html', contents=contents)


@app.route('/article/<index>')
def show_article(index):
    article = mongo.db.web_db.find_one_or_404({'id': index})

    return render_template('article.html', title=article['name'], content=article['content'])


@app.route('/new')
def new_article():

    return None


@app.route('/about')
def about():
    at = 'LALALA'
    return render_template('raw_message.html', message=at)


if __name__ == '__main__':
    app.run(debug=True)

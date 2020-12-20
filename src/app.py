import sys

from flask import Flask, render_template
from flask_frozen import Freezer

app = Flask(__name__)
freezer = Freezer(app)


@app.route('/')
def home():
    return render_template('pages/index.html')


@app.route('/about')
def about():
    return render_template('pages/about.html')


@app.route('/careers')
def careers():
    return render_template('pages/careers.html')


@app.route('/contact')
def contact():
    return render_template('pages/contact.html')


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'build':
        freezer.freeze()
    else:
        app.run(host='0.0.0.0', port=8001)

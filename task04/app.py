import os
import sys
import flask
import copy
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
                                        os.path.join(basedir, 'database.db')
db = SQLAlchemy(app)


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    if len(sys.argv) >= 2:
        print(f'port = {sys.argv[1]}')
        app.run(debug=True, port=sys.argv[1])
    else:
        app.run(debug=True, port=5000)

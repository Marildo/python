from flask import Flask, render_template, jsonify
from flask_cors import CORS

from datetime import datetime

app = Flask('Flask_AND_VUE', static_folder='static', template_folder='templates')
app.config['CORS_HEADERS'] = 'application/json'

"""
cors = CORS(app,
            resources={
                r"*": {
                    "origins": "*"
                }
            })

"""

@app.route('/')
def index():
    # return jsonify(msg='Server is running', data=datetime.now())
    return render_template('index.html')


@app.route('/todos')
def all():
    return render_template('all.html')


@app.route('/favoritos')
def favorites():
    return render_template('favorites.html')




@app.route('/test/')
def test():
    print('chegou até aqui')
    return jsonify(msg='Server is running', data=datetime.now())

if __name__ == '__main__':
    app.run(debug=True, port=3000)

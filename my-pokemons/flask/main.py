from flask import Flask, render_template, redirect,url_for

app = Flask('Flask_AND_VUE', static_folder='../vue/dist', template_folder='templates')


@app.route('/')
def index():
    # return jsonify(msg='Server is running', data=datetime.now())
    return render_template('index.html')


@app.route('/js/about.js')
def all():
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True, port=3000)

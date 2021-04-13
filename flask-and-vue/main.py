from flask import Flask, render_template, redirect, url_for, request, abort
app = Flask('VoooHelp', static_folder='front/static', template_folder='front')


@app.route('/')
def index():
    # return jsonify(msg='Server is running', data=datetime.now())
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=3000)

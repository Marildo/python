from flask import Flask, redirect, url_for, render_template, request, abort, session
import os
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import  Column, Integer, String

app = Flask(__name__, static_folder='public', template_folder='public')
app.secret_key = '123456789'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///estudantes.sqlite3'
db = SQLAlchemy(app)


class Estudante(db.Model):
    id = Column(Integer, primary_key=True)
    nome = Column(String(150))
    idade = Column(Integer)

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


UPLOAD_FOLDER = os.path.join(os.getcwd(), 'upload')


def teste():
    return '<h1>Testa de Rota</h1>'


app.add_url_rule('/test', 'test', teste)


# Modo com decorate
@app.route('/hello/')
@app.route('/hello/<nome>')
def hello(nome='usuario'):
    message = f'Hello {nome.capitalize()}!'
    return render_template('index.html', message=message)


@app.route('/')
def index():
    query = request.args.to_dict()
    username = session['username'] if 'username' in session else None
    return render_template('index.html', query=query, username=username)
    # return redirect(url_for('hello'))
    # return 'Index'


@app.route('/city/<int:id>')
def loadCity(id):
    return f'<h1>City id: {id}</h1>'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        session['username'] = username

        if username == 'admin' and password == 'admin':
            return redirect(url_for('index'))
        else:
            abort(401)
    else:
        abort(403)


@app.route('/logout/')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


@app.route('/calculo/', methods=['GET', 'POST'])
def calculo():
    notas = request.form.to_dict().values()
    total = sum([int(v) for v in notas])
    print(notas, total)
    return render_template('calculo.html', total=total, notas=notas)


@app.route('/upload/', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['image']
        os.mkdir(UPLOAD_FOLDER)
        savePath = os.path.join(UPLOAD_FOLDER, secure_filename(file.filename))
        file.save(savePath)

    return render_template('uploader.html')


@app.route('/estudantes/', methods=['GET', 'POST'])
def estudantes():
    if request.method == 'POST':
        form = request.form
        estudante = Estudante(form['nome'], form['idade'])
        db.session.add(estudante)
        db.session.commit()

    estudantes = Estudante.query.all()
    return render_template('estudantes.html', estudantes=estudantes, estudante=None)

@app.route('/edit/<int:id>', methods=['GET','POST'])
def edit(id):
    estudante = Estudante.query.get(id)
    if request.method == 'POST':
        form = request.form
        estudante.nome = form['nome']
        estudante.idade = form['idade']
        db.session.commit()
        return redirect(url_for('estudantes'))
    else:
        estudantes = Estudante.query.all()
        return render_template('estudantes.html', estudantes=estudantes, estudante=estudante)

@app.route('/delete/<int:id>')
def delete(id):
    estudante = Estudante.query.get(id)
    db.session.delete(estudante)
    db.session.commit()
    return redirect(url_for('estudantes'))

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, port=3000)

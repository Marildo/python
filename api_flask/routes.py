from flask import Flask, request,jsonify, make_response
from dao.Model import configureMash, User, UserSchema
from dao.Dao import save,load


app = Flask('API_Cotacao')


@app.route('/', methods=['GET'])
def index():
    return  jsonify(msg='Server is running...')

@app.route('/users/', methods=['GET'])
def users():
    bs = UserSchema(many=True)
    result = load()
    response = bs.jsonify(result)
    return  make_response(response, 200)


@app.route('/users/add', methods=['POST'])
def usersAdd():
    try:
        body = request.get_json()

        user = User()
        user.name = body['name']
        save(user)
        return { 'MSG': 'Salvo com sucesso' }
    except Exception as e:
        print(e)
        return  {'Error'}


configureMash(app)
app.run()
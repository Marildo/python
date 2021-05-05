from flask import Flask, request,jsonify, make_response
from dao.Model import configureMash, User, UserSchema
from dao.Dao import save,load
import json

app = Flask('API_Cotacao')


@app.route('/', methods=['GET'])
def index():
    return jsonify(msg='Server is running...')

@app.route('/users/', methods=['GET'])
def users():
    bs = UserSchema(many=True)
    result = load()
    response = bs.jsonify(result)
    return make_response(response, 200)


@app.route('/users/add', methods=['POST'])
def usersAdd():
    try:
        json_dict = request.get_json()
        #user = User(**json_dict)
        #new = save(user)
        return make_response(json_dict, 200)
    except Exception as e:
        print(e)
        return  {'Error'}


#configureMash(app)
app.run()
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from Database import Database




app = Flask(__name__)
app.config['SECRET_KEY'] = 'selya shop'
app.config['CORS_HEADERS'] = 'Content-Type'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

db = Database("database.db")

cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/api/auth", methods=['POST'])
@cross_origin(supports_credentials=True)
def auth():
    if db.userExists(request.get_json()["username"]):
        if db.checkPassword(request.get_json()["username"], request.get_json()["password"]):
            return jsonify({"status": "OK", "session_id": db.getCookie(request.get_json()["username"])})
        else:
            return jsonify({"status": "Error", "msg": "Не верный пароль!"})
    else:
        return jsonify({"status": "Error", "msg": "Такого администратора не существует"})


@app.route("/api/user", methods=['GET'])
@cross_origin(supports_credentials=True)
def getUser():
    if "hash" in request.args:
        user = db.getUserByHash(request.args['hash'])
        return jsonify({
            "status": "OK",
            "info": {
                "username": user[0][1],
            }
        })
    return jsonify({})


@app.route("/api/addclient", methods=['POST'])
@cross_origin(supports_credentials=True)
def addClient():
    data = request.get_json()
    seller = db.getUserByHash(data['seller_hash'])[0][1]
    try:
        db.addClient(name=data['fio'], phone=data['phone'], street=data['street'], subscription_type=data['sub_type'], subscription_seller=seller, birthday=data['birthday'])
        return jsonify({"status": "OK"})
    except Exception as e:
        print(str(e))
        return jsonify({"status": "Error", "msg": str(e)})


@app.route("/api/clients", methods=['GET'])
@cross_origin(supports_credentials=True)
def clients():
    sub_types = {
        1: "1 месяц",
        3: "3 месяца",
        6: "6 месяцев",
        12: "1 год"
    }
    if "name" in request.args:
        return jsonify({"status": "OK", "count_clients": len(db.sortByName(request.args['name'])),"clients": db.sortByName(request.args['name'])})
    clients = db.getAllClients()

    users = [{"fio": a[0], "phone": a[1], "street": a[2], "sub_type": sub_types[a[3]], "birthday": a[6]} for a in clients]
    return jsonify({"status": "OK", "count_clients": len(users) ,"clients": users})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
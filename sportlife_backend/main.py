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


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
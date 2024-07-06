from flask import Flask, jsonify, request
from utils.User import UserProfile
from utils.Register import process_registration


app = Flask(__name__)


@app.route("/user", methods=["POST"])
def manage_user():
    data = request.get_json()
    user_profile = UserProfile(data)
    request_id = data["requestID"]

    if request_id == "add":
        result = user_profile.add_user()
        return result
    return {"status":"091", "message":"unknown id"}


# Endpoint to get all users
@app.route("/", methods=["GET"])
def get_all_users():

    user_profile = UserProfile()
    result = user_profile.get_all_users()

    return result

@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    result = process_registration(data)
    return jsonify(result)

if __name__ == "__main__":
    app.run(port=5000, debug=True)

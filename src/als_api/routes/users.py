from flask import Blueprint, jsonify, request
from .enviroment import table_managers

users_blueprint = Blueprint("users", __name__, url_prefix="/users")

@users_blueprint.route("/login", methods=["POST"])
def user_login():
	data = request.get_json()

	identity: str = data.get("identity")
	password: str = data.get("password")

	if not identity or not password:
			return jsonify({"response": "Invalid informations"}), 401
	
	type = "email" if "@" in identity else "tel" if identity.isnumeric() else "name"
	
	(result, data) = table_managers.users.check_login_information_without_error_handler(identity, type, password)

	if not result:
		return jsonify({"response": "Login unsuccessful"}), 401

	token = table_managers.connections.create_new_connection(data.id)

	return jsonify({"response": "Login successfull", "token": token}), 200

@users_blueprint.route("/get_self", methods=["POST"])
def get_user_with_token():
	data = request.get_json()

	token: str = data.get("token")

	if token is None:
		return jsonify({"response": "Insert token field at your request"}), 401

	user_id = table_managers.connections.get_user_id(token)

	if user_id is None:
		return jsonify({"response": "Invalid token"}), 401

	user_infos = table_managers.users.get_user_using_id(user_id)

	return jsonify(user_infos.dict), 200

@users_blueprint.route("/logout", methods=["POST"])
def user_logout():
	data = request.get_json()

	token: str = data.get("token")

	if token is None:
		return jsonify({"response": "Insert token field at your request"}), 401

	rows_affects = table_managers.connections.destroy_connection_using_token(token)

	if rows_affects < 1:
		return jsonify({"response": "Invalid token"}), 401

	return jsonify({"response": "Logout sucessfull"}), 200
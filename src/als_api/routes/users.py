import os
from flask import Blueprint, jsonify, request

from .table_managers import TableManagers

users_blueprint = Blueprint("users", __name__, url_prefix="/users")

table_managers = TableManagers()

@users_blueprint.route("/login", methods=["POST"])
def list_users():
	data = request.get_json()

	identity: str = data.get("identity")
	type = "email" if "@" in identity else "tel" if identity.isnumeric() else "name"
	password: str = data.get("password")
	
	if not identity or not password:
		return jsonify({"response": "Informe sua identidade e sua senha"}), 401
	
	(result, data) = table_managers.users.check_login_information_without_error_handler(identity, type, password)

	if not result:
		return jsonify({"response": "Login unsuccessful"}), 401

	print(data)
	token = table_managers.connections.create_new_connection(data.id)

	return jsonify({"response": "Login successfull", "token": token}), 200
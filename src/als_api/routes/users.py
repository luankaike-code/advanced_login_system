from flask import Blueprint, jsonify, request

users_bp = Blueprint("users", __name__, url_prefix="/users")

@users_bp.route("/login", methods=["POST"])
def list_users():
	data = request.get_json()
	print(data)
	identity = data.get("identity")
	password = data.get("password")
	print(identity, password)
	if not identity or not password:
		return jsonify({"response": "Informe sua identidade e sua senha"}), 401

	if identity != "root" or password != "root":
		return jsonify({"response": "Acesso negado"}), 401

	return jsonify({"response": "Acesso permitido"}), 200
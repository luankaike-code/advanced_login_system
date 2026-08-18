from flask import Flask
from routes import users_blueprint

app = Flask(__name__)

app.register_blueprint(users_blueprint)

app.run(debug=True)
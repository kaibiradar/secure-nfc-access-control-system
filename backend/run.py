from flask import Flask

from app.database.db import db
from app.api.users import users_bp
from app.api.nfc_cards import nfc_cards_bp
from app.api.nfc_auth import nfc_auth_bp
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///access_control.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

app.register_blueprint(users_bp)
app.register_blueprint(nfc_cards_bp)
app.register_blueprint(nfc_auth_bp)

@app.route("/")
def home():
    return "Secure NFC Access Control System is running!"


if __name__ == "__main__":
    app.run(debug=True)
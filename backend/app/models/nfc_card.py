from app.database.db import db


class NFCCard(db.Model):
    __tablename__ = "nfc_cards"

    id = db.Column(db.Integer, primary_key=True)
    card_uid = db.Column(db.String(100), unique=True, nullable=False)
    card_name = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    is_active = db.Column(db.Boolean, default=True)

    user = db.relationship("User", backref="nfc_cards")
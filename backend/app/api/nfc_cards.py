from flask import Blueprint, request, jsonify

from app.database.db import db
from app.models.nfc_card import NFCCard
from app.models.user import User


nfc_cards_bp = Blueprint("nfc_cards", __name__)


@nfc_cards_bp.route("/api/nfc-cards", methods=["POST"])
def register_nfc_card():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Request body is required"}), 400

    card_uid = data.get("card_uid")
    card_name = data.get("card_name")
    user_id = data.get("user_id")

    if not card_uid or not card_name or not user_id:
        return jsonify({
            "error": "card_uid, card_name and user_id are required"
        }), 400

    existing_card = NFCCard.query.filter_by(card_uid=card_uid).first()

    if existing_card:
        return jsonify({
            "error": "NFC card with this UID already exists"
        }), 409

    user = User.query.get(user_id)

    if not user:
        return jsonify({
            "error": "User not found"
        }), 404

    card = NFCCard(
        card_uid=card_uid,
        card_name=card_name,
        user_id=user_id,
        is_active=True
    )

    db.session.add(card)
    db.session.commit()

    return jsonify({
        "message": "NFC card registered successfully",
        "card": {
            "id": card.id,
            "card_uid": card.card_uid,
            "card_name": card.card_name,
            "user_id": card.user_id,
            "is_active": card.is_active
        }
    }), 201
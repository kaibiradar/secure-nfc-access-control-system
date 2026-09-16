from flask import Blueprint, request, jsonify

from app.database.db import db
from app.models.nfc_card import NFCCard
from app.models.access_log import AccessLog


nfc_auth_bp = Blueprint("nfc_auth", __name__)


@nfc_auth_bp.route("/api/nfc-scan", methods=["POST"])
def nfc_scan():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Request body is required"}), 400

    card_uid = data.get("card_uid")

    if not card_uid:
        return jsonify({"error": "card_uid is required"}), 400

    card = NFCCard.query.filter_by(card_uid=card_uid).first()

    if not card:
        access_log = AccessLog(
            card_uid=card_uid,
            access_status="DENIED",
            reason="Unknown NFC card"
        )

        db.session.add(access_log)
        db.session.commit()

        return jsonify({
            "access": "DENIED",
            "reason": "Unknown NFC card"
        }), 403

    if not card.is_active:
        access_log = AccessLog(
            card_uid=card_uid,
            user_id=card.user_id,
            access_status="DENIED",
            reason="NFC card is inactive"
        )

        db.session.add(access_log)
        db.session.commit()

        return jsonify({
            "access": "DENIED",
            "reason": "NFC card is inactive"
        }), 403

    access_log = AccessLog(
        card_uid=card_uid,
        user_id=card.user_id,
        access_status="GRANTED",
        reason="Valid and active NFC card"
    )

    db.session.add(access_log)
    db.session.commit()

    return jsonify({
        "access": "GRANTED",
        "message": "Access granted",
        "card": {
            "card_uid": card.card_uid,
            "card_name": card.card_name,
            "user_id": card.user_id
        }
    }), 200
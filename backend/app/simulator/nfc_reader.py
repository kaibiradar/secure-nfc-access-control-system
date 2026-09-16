import requests

from app.simulator.virtual_card import VirtualNFCCard


API_URL = "http://127.0.0.1:5000/api/nfc-scan"


def scan_card(card):
    card.display()

    response = requests.post(
        API_URL,
        json={"card_uid": card.get_uid()}
    )

    print("\n--- NFC SCAN RESULT ---")
    print(response.json())


if __name__ == "__main__":
    card_uid = input("Enter virtual NFC card UID: ")

    virtual_card = VirtualNFCCard(
        card_uid=card_uid,
        card_name="Virtual Access Card"
    )

    scan_card(virtual_card)
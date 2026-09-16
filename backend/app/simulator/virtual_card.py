class VirtualNFCCard:
    def __init__(self, card_uid, card_name):
        self.card_uid = card_uid
        self.card_name = card_name

    def get_uid(self):
        return self.card_uid

    def display(self):
        print("\n--- VIRTUAL NFC CARD ---")
        print(f"Card Name : {self.card_name}")
        print(f"Card UID  : {self.card_uid}")
from datetime import datetime

NOW = datetime.now()

class Promo:
    def __init__(self, name, expires):
        self.expires = expires

    def get_expired(self):
        if NOW < self.expires:
            return False
        else:
            return True
    expired = property(get_expired)
######################################
#  voice-assistant  >  Greeter.py
#  Created by Uygur Kiran on 2021/4/16
######################################
from datetime import datetime
from configurator import get_config
######################################

class Greeter:
    keywords = [
        "merhaba", "günaydın", "tünaydın", "iyi akşamlar", "iyi geceler",
        "naber", "ne haber", "nasılsın"
    ]

    def __init__(self):
        self.name = get_config("personalization", "user", "name")

    def get_greeting(self):
        hour = datetime.now().hour
        if hour >= 5 and hour < 12:
            return f"Günaydın {self.name}."
        elif hour >= 12 and hour < 18:
            return f"Tünaydın {self.name}."
        else:
            return f"İyi akşamlar {self.name}."
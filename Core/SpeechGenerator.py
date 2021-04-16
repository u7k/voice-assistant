######################################
#  voice-assistant  >  SpeechGenerator.py
#  Created by Uygur Kiran on 2021/4/16
######################################
import os
from gtts import gTTS
from playsound import playsound
from configurator import get_config
######################################
FILENAME = "temp.mp3"

class SpeechGenerator:
    def __init__(self):
        self.lang = get_config("speechGeneration", "language")
        self.tld = get_config("speechGeneration", "tld")
        self.slow_talk = get_config("speechGeneration", "slow_talk")

    def say(self, text):
        try:
            tts = gTTS(text=text, lang=self.lang, tld=self.tld, slow=self.slow_talk)
            tts.save(FILENAME)
        except UnicodeDecodeError as err:
            print(err)
        else:
            playsound(FILENAME)
        finally:
            os.remove(FILENAME)

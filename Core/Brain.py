######################################
#  voice-assistant  >  Brain.py
#  Created by Uygur Kiran on 2021/4/16
######################################
import types
from Core.SpeechGenerator import SpeechGenerator
from Skills.Calendar import Calendar
from Skills.Greeter import Greeter
from Skills.Traffic import Traffic
from Skills.Weather import Weather
######################################

class Brain:
    def __init__(self):
        self.speak = SpeechGenerator().say

    def __check(self, input, keywords):
        return bool(any(key in input for key in keywords))

    def __try_to(self, get_result, for_context):
        if isinstance(get_result, types.FunctionType):
            res = get_result()
        else:
            res = get_result
        ## TRY
        if not res or isinstance(res, Exception):
            self.speak(f"{for_context} bilgisine ulaşılamadı.")
        else:
            self.speak(res)

    def make_sense(self, input):
        if not input:
            return

        i = input.casefold()

        if self.__check(i, Calendar.time_keywords):
            self.speak(Calendar().get_time())
        elif self.__check(i, Calendar.date_keywords):
            self.speak(Calendar().get_date()[0])
        elif self.__check(i, Greeter.keywords):
            self.speak(Greeter().get_greeting())
        elif self.__check(i, Traffic.keywords):
            self.__try_to(Traffic().get_traffic_density(), "Trafik Yoğunluğu")
        elif self.__check(i, Weather.keywords):
            self.__try_to(Weather().get_current_weather(), "Hava Durumu")

        else:
            ## TODO: log to csv
            self.speak("Ne söylediğini anlayamadım.")
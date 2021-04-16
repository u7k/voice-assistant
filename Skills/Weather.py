######################################
#  voice-assistant  >  Weather.py
#  Created by Uygur Kiran on 2021/4/16
######################################
import os
import requests
from configurator import get_config
import random
######################################

class Weather:
    def __init__(self):
        self.TOKEN = os.environ.get("WEATHER_TOKEN")
        self.cityName = get_config("services", "weather", "cityName")
        self.lat = get_config("services", "weather", "latitude")
        self.lon = get_config("services", "weather", "longitude")

    def get_current_weather(self):
        ENDPOINT = "https://api.openweathermap.org/data/2.5/weather"

        params = self.__get_params()
        if params is None:
            return "Hava durumuna ulaşabilmek için konfigürasyon dosyasında" \
                   " bir şehir ismi ya da enlem ve boylam belirtiniz."

        try:
            res = requests.get(url=ENDPOINT, params=params)
            res.raise_for_status()
        except requests.HTTPError as err:
            if err.response.status_code == 401:
                return "Hava durumuna ulaşabilmek için ey pi ay anahtarınızı yapılandırınız."
        except requests.exceptions.RequestException:
            return None
        else:
            weather = res.json()
            city = weather.get("name")

            # UPDATE LAT & LON
            if not self.lat and not self.lon:
                self.lat = weather.get("coord").get("lat")
                self.lon = weather.get("coord").get("lon")

            # DEGREES
            temp = int(weather.get("main").get("temp"))

            # DESC
            temp_lbl = weather.get("weather")
            if len(temp_lbl) == 0: return None
            temp_lbl = temp_lbl[0].get("description")

            result = self.__create_str(city, temp, temp_lbl)

            if "yağmur" not in result and self.__get_future_rain() == True:
                result += ". Önümüzdeki saatlerde yağmur bekleniyor."

            return result


    def __get_params(self):
        if self.lat != None and self.lon != None:
            p = {
                "appid": self.TOKEN,
                "units": "metric",
                "lang": "tr",
                "lat": self.lat,
                "lon": self.lon
            }
            return p
        elif self.cityName is not None:
            p = {
                "appid": self.TOKEN,
                "units": "metric",
                "lang": "tr",
                "q": self.cityName
            }
            return p
        else:
            return None

    def __create_str(self, city, temp, temp_lbl):
        # ADD TURKISH SUFFIXES (de, da, te, ta)
        if city:
            with_suffix = city
            if city[len(city)-1] in ["f", "s", "t", "k", "ç", "ş", "h", "p"]:
                with_suffix += "'t"
            else:
                with_suffix += "'d"

            if city[len(city) - 2] in ["i", "e", "ö", "ü"]:
                with_suffix += "e"
            else:
                with_suffix += "a"
            city = with_suffix

        new_sentence = city if city else ""
        sentences = [
            f"hava durumu {temp} derece, {temp_lbl}",
            f"hava {temp} derece ile {temp_lbl}",
            f"hava {temp_lbl}, {temp} derece"
        ]
        # MERGE CITY NAME
        new_sentence += " " + random.choice(sentences)
        return new_sentence


    def __get_future_rain(self):
        if not self.lat and not self.lon: return None
        ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
        params = {
            "appid": self.TOKEN,
            "lat": self.lat,
            "lon": self.lon,
            "exclude": "current,minutely,daily"
        }

        try:
            response = requests.get(url=ENDPOINT, params=params)
            response.raise_for_status()
        except requests.exceptions.RequestException:
            return None
        else:
            weather = response.json()
            ## SLICE DATA FOR NEXT 8 HOURS
            weather_slice = weather.get("hourly")[:8]

            for hour_data in weather_slice:
                condition_code = hour_data.get("weather")[0].get("id")
                if condition_code < 700:
                    # WILL RAIN
                    return True

######################################
#  voice-assistant  >  Traffic.py
#  Created by Uygur Kiran on 2021/4/16
######################################
import requests
import random
######################################

class Traffic:
    keywords = [
        "trafik", "trafik yoğunluğu", "trafik seviyesi",
        "trafik nasıl", "trafik ne durumda", "yollar açık mı",
        "trafik durumu nedir", "trafik yoğunluğu nasıl",
        "trafik var mı"
    ]

    def __init__(self):
        pass

    def get_traffic_density(self):
        IBB_ENDPOINT = "https://api.ibb.gov.tr/tkmservices/api/TrafficData/v1/TrafficIndexHistory/1/5M/"

        try:
            res = requests.get(url=IBB_ENDPOINT)
            res.raise_for_status()
        except requests.exceptions.RequestException:
            return None
        else:
            t_density = res.json()
            if len(t_density) == 0:
                return None
            else:
                t_density = t_density[0].get("TrafficIndex")
                return self.__create_str(t_density)

    def __create_str(self, val):
        if val <= 30:
            val_eval = "düşük"
        elif val > 30 and val <= 44:
            val_eval = "orta"
        else:
            val_eval = "yüksek"

        sentences = [
            f"Şu anda trafik yoğunluğu yüzde {val} ile {val_eval} seviyede.",
            f"İstanbul'da trafik yüzde {val} ile {val_eval} seviyede.",
            f"Trafik yüzde {val} ile {val_eval} seviyede."
        ]
        return random.choice(sentences)
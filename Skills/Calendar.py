######################################
#  voice-assistant  >  Calendar.py
#  Created by Uygur Kiran on 2021/4/16
######################################
from datetime import datetime
import random
######################################

class Calendar:
    time_keywords = [
        "saat", "saat kaç", "saat ne", "hangi saat",
        "hangi saatteyiz", "saat kaç oldu",
        "saatin var mı", "saat kaçı gösteriyor"
    ]

    date_keywords = [
        "tarih", "bugünün tarihi ne", "ayın kaçı", "bugün ayın kaçı",
        "hangi gündeyiz", "bugün hangi gün", "ayın kaçındayız",
        "hangi gün", "tarihi söyler misin", "hangi aydayız",
        "hangi yıldayız."
    ]

    def __init__(self):
        # TODO: config
        pass

    def get_time(self):
        hour = datetime.now().hour
        min = str(datetime.now().minute)

        if hour in [1, 11, 21, 5, 15, 8, 18]:
            hour = str(hour) + " i"
        elif hour in [2, 12, 22, 7, 17, 20]:
            hour = str(hour) + " yi"
        elif hour in [6, 16]:
            hour = str(hour) + " yı"
        elif hour in [9, 19, 10]:
            hour = str(hour) + " u"
        elif hour in [4, 14, 3, 13, 23, 24]:
            hour = str(hour) + " ü"
        elif hour in [0, 00]:
            hour = str(hour) + " ı"
        else:
            hour = str(hour)

        sentences = [
            f"Saat, {hour} {min} geçiyor.",
            f"Şu anda saat {hour} {min} geçiyor.",
            f"{hour} {min} geçiyor.",
            f"Şu anda {hour} {min} geçiyor."
        ]
        return random.choice(sentences)

    def get_date(self):
        month_names = [
            "Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran",
            "Temmuz", "Ağustos", "Eylül", "Ekim", "Kasım", "Aralık"
        ]
        day_names = [
            "Pazartesi", "Salı", "Çarşamba", "Perşembe",
            "Cuma", "Cumartesi", "Pazar"
        ]

        day_num = datetime.now().day
        month = datetime.now().month
        year = datetime.now().year
        is_important = self.is_an_important_date(day_num, month)

        ## CREATE STR
        day = day_names[datetime.now().weekday()]
        month = month_names[month - 1]
        sentences = [
            f"Bugün {day_num} {month}, {day}",
            f"{day_num} {month} {year}, {day}.",
            f"{day_num} {month}, bugün günlerden {day}."
        ]

        return (random.choice(sentences), is_important)

    def is_an_important_date(self, day, month):
        # TODO: read from a csv
        # return sentence & func or None
        return None

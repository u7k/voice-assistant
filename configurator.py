######################################
#  voice-assistant  >  configurator.py
#  Created by Uygur Kiran on 2021/4/16
######################################
import json

######################################
# CONSTS
######################################
FILENAME = "configuration.json"
DEFAULT_CONFIG = {
    "personalization": {
        "user": {
            "name": "Uygur"
        }
    },
    "speechRecognition": {
        "language": "tr_TR"
    },
    "speechGeneration": {
        "language": "tr",
        "tld": "com.tr",
        "slow_talk": "false"
    },
    "debug_mode": "true",
    "services": {
        "weather": {
            "cityName": "Sisli, TR",
            "latitude": None,
            "longitude": None,
        }
    }
}

######################################
# CONFIG FETCH
######################################
def __create_config_file():
    with open(FILENAME, "w") as new_config_file:
        json.dump(DEFAULT_CONFIG, new_config_file, indent=4)
    print("*** New config file has been created. ***")


def __return_default(param: str, *args):
    def_config = DEFAULT_CONFIG.get(param)

    for arg in args[0]:
        new_value = def_config.get(arg)

        if new_value:
            if new_value == "true" or new_value == "false":
                def_config = bool(new_value == "true")
            else:
                def_config = new_value

    if isinstance(def_config, dict):
        return None
    else:
        return def_config


def get_config(param: str, *args):
    try:
        with open(FILENAME, "r") as config_file:
            config_data = json.load(config_file)
    except FileNotFoundError:
        __create_config_file()
        return __return_default(param, args)
    else:
        found_config = config_data.get(param)

        for arg in args:
            new_value = found_config.get(arg)
            if new_value:
                if new_value == "true" or new_value == "false":
                    found_config = bool(new_value == "true")
                else:
                    found_config = new_value

        return found_config if found_config and not isinstance(found_config, dict) \
            else __return_default(param, args)
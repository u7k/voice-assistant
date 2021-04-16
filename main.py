######################################
#  voice-assistant  >  main.py
#  Created by Uygur Kiran on 2021/4/16
######################################
from Core.Asistan import Asistan
from configurator import get_config
######################################

## PROPS
asistan = Asistan()

######################################
# DEBUG
######################################
if get_config("debug_mode"):
    asistan.print_devices()

######################################
# INIT
######################################
asistan.start_ui()


######################################
#  voice-assistant  >  Asistan.py
#  Created by Uygur Kiran on 2021/4/16
######################################
import speech_recognition as sr
from Core.UI import UI
from Core.Brain import Brain
from playsound import playsound
######################################

class Asistan(sr.Recognizer):
    def __init__(self):
        super().__init__()
        ## UI
        self.window = UI()
        self.speak_button = self.window.setup_ui_contents(command = self.init_manuel_awake)
        self.brain = Brain()

    def start_ui(self):
        self.window.mainloop()

    def print_devices(self):
        from prettytable import PrettyTable

        table = PrettyTable()
        table.title = "AVAILABLE MICROPHONES"
        table.field_names = ["Index", "Device Name"]
        table.add_rows(enumerate(sr.Microphone.list_microphone_names()))
        table.align = "l"
        print(table)

    def __update_btn_lbl(self, is_listening):
        new_text = "Dinliyorum..." if is_listening else "Konuşmak için Bas"
        self.speak_button.config(text=new_text)
        self.speak_button.update()

    def __detect_speech(self):
        try:
            with sr.Microphone() as source:
                self.__update_btn_lbl(True)
                playsound("boop.wav")

                audio = self.listen(source)
                try:
                    new_input = self.recognize_google(audio_data=audio, language="tr_TR")
                except sr.UnknownValueError:
                    print("Google Speech Recognition could not understand audio")
                except sr.RequestError as e:
                    print("Could not request results from Google Speech Recognition service; {0}".format(e))
                else:
                    return new_input
        except:
            self.window.show_mic_error()
        finally:
            self.__update_btn_lbl(False)

    def awake_assistant(self):
        input = self.__detect_speech()
        self.brain.make_sense(input)
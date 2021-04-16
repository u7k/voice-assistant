######################################
#  voice-assistant  >  UI.py
#  Created by Uygur Kiran on 2021/4/16
######################################
from tkinter import *
from tkinter import messagebox
######################################
TITLE_FONT = ("Avenir", 25, "bold")
BTN_FONT = ("Avenir", 18, "bold")

class UI(Tk):
    def __init__(self):
        super().__init__()
        self.title("Asistan")
        self.config(padx=50, pady=50)

    def setup_ui_contents(self, command):
        ## TITLE
        title_lbl = Label(text="Asistan")
        title_lbl.config(pady=20, font=TITLE_FONT)
        title_lbl.pack()

        ## SPEAK BTN
        speak_btn = Button(text="Konuşmak için Bas", command=command)
        speak_btn.config(width=40, pady=40, font=BTN_FONT)
        speak_btn.pack()
        return speak_btn

    def show_mic_error(self):
        messagebox.showinfo(title="Hata", message="Bir mikrofona erişim sağlayamadım.")
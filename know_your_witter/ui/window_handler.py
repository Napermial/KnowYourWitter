from tkinter import *
from tkinter.ttk import *
from threading import Thread
import logging, os
from know_your_witter.typer import guess


class GUI:
    def __init__(self):
        self.window = Tk()
        self.frm_entry = Frame(master=self.window)
        self.lbl_type = Label(master=self.frm_entry, text="Your type is:")
        self.progress_bar = Progressbar(master=self.frm_entry, orient=HORIZONTAL, mode='determinate')
        self.btn_typer = Button(master=self.frm_entry, text="Type me", command=self.load)
        self.ent_username = Entry(master=self.frm_entry, width=20)
        self.predicted_type = None

    def prepare_screen(self):
        logging.info( "Screen created")
        self.window.title = "Know Your Witter"
        self.ent_username.grid(row=0, column=0, sticky="e")
        self.lbl_type.grid(row=0, column=1, sticky="w")

        self.frm_entry.grid(row=0, column=0, padx=10)
        self.btn_typer.grid(row=0, column=1, pady=10)
        self.lbl_type.grid(row=0, column=2, padx=10)
        self.progress_bar.grid(row=1, columnspan=3, sticky="nesw")

    def read_username(self):
        user_name = self.ent_username.get()
        logging.info(f"Username read {user_name}")
        return_value = guess.guess_personality(user_name)
        self.display_type(return_value)
        self.predicted_type = return_value

    def display_type(self, type):
        self.lbl_type["text"] = "Your type is: " + type

    def load(self):
        reader = Thread(target=self.read_username, daemon=True)

        def parallel_load():
            reader.start()
            while self.predicted_type is None:
                for _ in range(10):
                    self.window.update()
                    self.progress_bar.after(200)
                    self.progress_bar.step(10)
            reader.join()
            logging.info(f"type : {self.predicted_type} is predicted")
            self.predicted_type = None
        Thread(target=parallel_load()).start()


def load_threads():
    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
    gui = GUI()
    gui.prepare_screen()
    gui.window.mainloop()


if __name__ == '__main__':
    load_threads()

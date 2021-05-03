from tkinter import *
from tkinter.ttk import *
from threading import Thread
import concurrent.futures
from know_your_witter.typer import guess


class GUI:
    def __init__(self):
        self.window = Tk()
        self.window.title = "Know Your Witter"
        self.frm_entry = Frame(master=self.window)
        self.lbl_type = Label(master=self.frm_entry, text="Your type is:")
        self.progress_bar = Progressbar(master=self.frm_entry, orient=HORIZONTAL, mode='determinate')
        self.btn_typer = Button(master=self.frm_entry, text="Type me", command=self.load)
        self.ent_username = Entry(master=self.frm_entry, width=10)
        self.predicted_type = None

    def prepare_screen(self):
        self.ent_username.grid(row=0, column=0, sticky="e")
        self.lbl_type.grid(row=0, column=1, sticky="w")

        self.frm_entry.grid(row=0, column=0, padx=10)
        self.btn_typer.grid(row=0, column=1, pady=10)
        self.lbl_type.grid(row=0, column=2, padx=10)
        self.progress_bar.grid(row=1, columnspan=3, sticky="nesw")

    def read_username(self):
        user_name = self.ent_username.get()
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future = executor.submit(guess.guess_personality(user_name))
            return_value = future.result()
            self.display_type(future.result())
            self.predicted_type = return_value
            print(return_value)

    def display_type(self, type):
        self.lbl_type["text"] = "Your type is: " + type

    def load(self):
        def parallel_load():
            while self.predicted_type is None:
                for _ in range(10):
                    self.window.update()
                    self.progress_bar.after(200)
                    self.progress_bar.step(10)

        Thread(target=parallel_load()).start()


if __name__ == '__main__':
    gui = GUI()
    gui.prepare_screen()
    gui.window.mainloop()

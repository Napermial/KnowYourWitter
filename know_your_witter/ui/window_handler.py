from tkinter import *
from tkinter.ttk import *
import time
from threading import Thread


def create_window():
    def read_username():
        user_name = ent_username.get()
        # TODO access api

    def display_type(type):
        lbl_type["text"] = "Your type is: " + type

    def load():
        loading = True
        while loading:
            for i in range(6):
                progress_bar['value'] = 20 * i
                window.update_idletasks()
                time.sleep(0.5)
            loading = False

    window = Tk()
    window.title = "Know Your Witter"

    frm_entry = Frame(master=window)
    ent_username = Entry(master=frm_entry, width=10)
    lbl_type = Label(master=frm_entry, text="Your type is:")

    ent_username.grid(row=0, column=0, sticky="e")
    lbl_type.grid(row=0, column=1, sticky="w")

    btn_typer = Button(master=frm_entry, text="Type me", command=load)

    progress_bar = Progressbar(master=frm_entry, orient=HORIZONTAL, mode='determinate')

    frm_entry.grid(row=0, column=0, padx=10)
    btn_typer.grid(row=0, column=1, pady=10)
    lbl_type.grid(row=0, column=2, padx=10)
    progress_bar.grid(row=1, columnspan=3, sticky="nesw")

    window.mainloop()


if __name__ == '__main__':
    create_window()

from tkinter import *
from know_your_witter.typer import guess

def create_window():
    def read_username():
        user_name = ent_username.get()

        lbl_type["text"] = "Your type is: " + user_name

    window = Tk()
    window.title = "Know Your Witter"

    frm_entry = Frame(master=window)

    ent_username = Entry(master=frm_entry, width=10)
    lbl_type = Label(master=frm_entry, text="Your type is:")

    ent_username.grid(row=0, column=0, sticky="e")
    lbl_type.grid(row=0, column=1, sticky="w")

    btn_typer = Button(master=window, text="Type me", command=read_username)

    frm_entry.grid(row=0, column=0, padx=10)
    btn_typer.grid(row=0, column=1, pady=10)
    lbl_type.grid(row=0, column=2, padx=10)

    window.mainloop()


if __name__ == '__main__':
    create_window()

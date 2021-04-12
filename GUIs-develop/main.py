import tkinter as tk
from tkinter import ttk


def greet():
    print(f"Hello {user_name.get()}!")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    root = tk.Tk()
    root.title("Hello")

    user_name = tk.StringVar()

    frame1 = tk.Frame()
    frame1.pack(side="top", pady=(5, 5), fill="x")

    name_label = ttk.Label(frame1, text="Name: ")
    name_label.pack(side="left", padx=(5, 5))
    name_entry = ttk.Entry(frame1, width=15, textvariable=user_name)
    name_entry.pack(side="left", fill="x", expand=True)
    name_entry.focus()

    frame2 = tk.Frame()
    frame2.pack(side="top", pady=(0, 5), fill="x")

    greet_button = ttk.Button(frame2, text="Greet", command=greet)
    greet_button.pack(side="left")
    quit_button = ttk.Button(frame2, text="Quit", command=root.destroy)
    quit_button.pack(side="left")

    root.mainloop()

import tkinter as tk

root = tk.Tk()

#root.geometry("444*233")

q="""READY."""
label = tk.Label(text=q, bg='red', padx=10, pady=20, relief='sunken', borderwidth=3, font="times 15 bold").pack(side="bottom",anchor="s", fill='x' )

root .mainloop()
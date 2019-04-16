import tkinter as tk

root = tk.Tk()
root.geometry("400x400")
root.title("Event")

button1 = tk.Button(root, text='Click Me')
button1.pack()
button1.bind("<Double-1>", quit)

def hello(event):
    print("Hello World")
button1.bind('<Button-1>', hello)



root.mainloop()

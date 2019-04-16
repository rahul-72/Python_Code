import tkinter as tk

root=tk.Tk()
root.geometry("400x400")


frame1 = tk.Frame(root, bg='grey', relief='sunken', borderwidth=9)
frame1.pack(side='left', anchor='nw')

def hello():
    print("HELLO WORLD")

button1 = tk.Button(frame1, fg='red', bg='lightblue',text='Print', command=hello)
button1.pack(side='left',padx=15)

def bye():
    print("BYE WORLD")

button2 = tk.Button(frame1, fg='red', bg='lightblue', text='Open', command=bye)
button2.pack(side='left', padx=15)

label1=tk.Label(frame1, text='HELLO WORLD')
label1.pack(side='left', padx=30)

root.mainloop()
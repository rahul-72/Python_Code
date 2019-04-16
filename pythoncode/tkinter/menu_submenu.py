import tkinter as tk
import tkinter.messagebox as tmsg

root = tk.Tk()
root.geometry("400x400")
root.title("Menu")

def hello():
    print("Hello World")


def my_help():
    ask = tmsg.askokcancel(title='Help', message='Want help-->>>>')
    print(ask)
    if ask == True:
        tmsg.showinfo('ok we will help you out ')

mainmenu = tk.Menu(root)
m1 = tk.Menu(mainmenu, tearoff=0)
m1.add_command(label='save', command=hello)
m1.add_command(label='Print',command=hello)
m1.add_command(label='Exit', command=quit)
m1.add_command(label='help', command=my_help)
root.config(menu=mainmenu)
mainmenu.add_cascade(label='File', menu=m1)



root.mainloop()

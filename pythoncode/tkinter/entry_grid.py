import tkinter as tk

root = tk.Tk()
root.geometry("400x400")
root.title("Entry_Grid")


user = tk.Label(root, text='Username')
user.grid(row=0, column=0)

password = tk.Label(root, text='Password')
password.grid(row=1, column=0)

uservalue = tk.StringVar()
passvalue = tk.StringVar()

userentry = tk.Entry(root, textvariable=uservalue)
passentry = tk.Entry(root, textvariable=passvalue)
userentry.grid(row=0, column=1)
passentry.grid(row=1, column=1)


def getvalues():
    print(f"Username is {uservalue.get()}")
    print(f"Password is {passvalue.get()}")

buttom1 = tk.Button(root, text='Submit', command=getvalues)
buttom1.grid()




root.mainloop()
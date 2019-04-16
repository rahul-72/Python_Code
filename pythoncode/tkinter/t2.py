import tkinter as tk

root = tk.Tk()
root.geometry("400x400")


f1=tk.Frame(root, bg='grey', borderwidth=9, relief='sunken')
f1.pack(side='left', padx=20)

f2=tk.Frame(root, bg='red', borderwidth=9, relief='sunken')
f2.pack(side='top')

l1=tk.Label(f1, text='hello world')
l1.pack(padx=20, pady=200,anchor='nw')

l2=tk.Label(f2, text='bye world')
l2.pack(padx=400,pady=30)



root.mainloop()
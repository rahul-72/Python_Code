import tkinter as tk

root = tk.Tk()
root.geometry("400x400")
root.title("Newspaper")


def line_breaker(data):
    text = ""
    for i in range(0,len(data)):
        text+=data[i]
        if i%100==0 and i!=0:
            text+="\n"
    return text

f=open("D:\\tkinter\\data\\text\\1.txt")
data = f.read()
f.close()

data = line_breaker(data)





frame1 = tk.Frame(root, bg='grey', relief='sunken', borderwidth=9, width=900, height= 200)
frame1.pack(anchor='nw')

label1 = tk.Label(frame1, text="News", font="times 33 bold", bg='lightblue').pack()

label2 = tk.Label(frame1, text=data, font="times 12 bold")
label2.pack(side='left')
logo = tk.PhotoImage(file="data/image/2.png")
label3 = tk.Label(frame1, image=logo).pack()






root.mainloop()
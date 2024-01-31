import tkinter as tk
from tkinter import messagebox
import base64

#screen
screen=tk.Tk()
screen.title("MSK ENCRYPTION")
screen.geometry('500x300')
screen.resizable(False,False)

tk.Label(screen, text="ENCODE AND DECODE",font=("Arial",12,"bold")).pack()

Text=tk.StringVar()
Key=tk.StringVar()
Mode=tk.StringVar()
Result=tk.StringVar()

def Encode(text, key):
    en=[]
    for i in range(len(text)):
        a_key=key[i%len(key)]
        en.append(chr((ord(text[i])+ ord(a_key))%256))
    return base64.urlsafe_b64encode("".join(en).encode()).decode()

def Decode(text, key):
    de=[]
    text=base64.urlsafe_b64decode(text).decode()
    for i in range(len(text)):
        a_key=key[i%len(key)]
        de.append(chr((ord(text[i])-ord(a_key))%256))
    return "".join(de)

def Res():
    if Mode.get()=="e":
        Result.set(Encode(Text.get(),Key.get()))
    elif Mode.get()=="d":
        Result.set(Decode(Text.get(),Key.get()))
    else:
        messagebox.showerror("MSK ERROR","Invalid Mode! \nEnter mode again.")
        Mode.set("")

def Exit():
    screen.destroy()

def Reset():
    Text.set("")
    Key.set("")
    Mode.set("")
    Result.set("")

tk.Label(screen, text="Message",font=("Arial",10,"bold")).place(x=60,y=60)
tk.Label(screen, text="Key",font=("Arial",10,"bold")).place(x=60,y=100)
tk.Label(screen, text="Mode",font=("Arial",10,"bold")).place(x=60,y=140)

tk.Entry(screen, textvariable=Text, font=("Arial",10,"normal"), bg="lightgreen",fg="black").place(x=200,y=60)
tk.Entry(screen, textvariable=Key, font=("Arial",10,"normal"), bg="lightgreen", fg="black").place(x=200,y=100)
tk.Entry(screen, textvariable=Mode, font=("Arial",10,"normal"), bg="lightgreen", fg="black").place(x=200,y=140)
tk.Entry(screen, textvariable=Result, font=("Arial",10,"normal"), bg="lightgreen", fg="black").place(x=200,y=180)

tk.Button(screen, text="Result", font=("Arial",10,"bold"), command=Res, bg="white", padx=2).place(x=60,y=180)
tk.Button(screen, text="Reset", font=("Arial",10,"bold"), command=Reset, bg="white", padx=2).place(x=60,y=220)
tk.Button(screen, text="Exit", font=("Arial",10,"bold"),command=Exit, bg="white", padx=2).place(x=200,y=220)

screen.mainloop()

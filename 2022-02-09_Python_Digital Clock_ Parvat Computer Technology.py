#Make a Clock using Python | Python Project
#Coding With Evan- Oct 11,2020

from tkinter import *
from tkinter.ttk import *
from time import strftime

ernie = Tk()
ernie.title("Digital Clock")

def myclock():
    text = strftime("%H:%M:%S %p")
    #string = strftime("%I:%M:%S %p")   # AM
    label.config(text=text)
    label.after(1000,myclock)


label = Label(ernie,font=("ds - digital",80),background="black",foreground="cyan")
#label = Label(ernie,font=("digital-7",80,"bold"),background="white",foreground="blue")
label.pack(anchor="center")
myclock()

mainloop()

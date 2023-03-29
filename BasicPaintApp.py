#Paint uygulaması

from tkinter import *
from tkinter.colorchooser import *

window=Tk()
window.geometry("800x600")

window.title(" \t PAINT APP")


#kalem boyutunun seçilmesi
kalemBoyutu=5
def secilenKalemValue(value):
    global kalemBoyutu
    deger=value
    if deger=="Small Pencil":
        kalemBoyutu=5
    elif deger=="Medium Pencil":
        kalemBoyutu=10
    elif deger=="Big Pencil":
        kalemBoyutu=15  

secilenKalem=StringVar()
menuPencil=OptionMenu(window,secilenKalem,"Small Pencil","Medium Pencil","Big Pencil",command=secilenKalemValue)
menuPencil.pack()
secilenKalem.set("Choose Pen Size")


renk=["","Black"]
#color askcolor ile renginin alınması
def renkAl():
    global renk
    renk=askcolor()

Button(text="Choose Color",command=renkAl).pack()

#Mevcut mouse koordinatlarının alınması
def koordinatlar(koordinat):
    global x,y
    x=koordinat.x
    y=koordinat.y

#Mouse koordinatlarını takip ederek çizim işlemlerinin gerçekleşmesi
def cizim(ciz):
    global x,y,renk    
    canvas.create_line((x,y,ciz.x,ciz.y),fill=renk[1], width=kalemBoyutu)
    x=ciz.x
    y=ciz.y


#Çizim işlemlerinin gerçekleşmesi
canvas=Canvas(window,bg="white")
canvas.pack(anchor="s",fill="both",expand=1)

canvas.bind("<Button-1>",koordinatlar)
canvas.bind("<B1-Motion>",cizim)

window.mainloop()
from tkinter import *
import fonction as fct
import time


fen = Tk()
fen.geometry("400x300")

canevas = Canvas(fen)
photo = PhotoImage(file="bg1.png")
canevas.create_image(0, 0, anchor=NW, image=photo)
canevas.grid(column=0)

liste = []
x1= 5
x2 = 25

y1 = 5
y2= 25
liste.append(canevas.create_rectangle(x1,y1,x2,y2,fill="brown"))
liste.append(canevas.create_rectangle(x1+35,y1,x2+35,y2,fill="brown"))

# marche pour les deplacements
for i in range(10):
    for j in liste :
        
        canevas.move(j,5,0)
        
liste = [1,2,3]
for i in liste :
    print(liste)
    liste.pop(0)
    print(liste)

fen.mainloop()
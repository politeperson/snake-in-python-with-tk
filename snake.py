from juego import *
from Tkinter import *
from os import *

def sacar1(event):
    global serp
    if serp.posicion[len(serp.posicion)-1][1]-1!=serp.posicion[len(serp.posicion)-2][1] and serp.direccion!="derecha":
        serp.direccion="izquierda"
def sacar2(event):
    global serp
    if serp.posicion[len(serp.posicion)-1][1]+1!=serp.posicion[len(serp.posicion)-2][1] and serp.direccion!="izquierda":
        serp.direccion="derecha"
def sacar3(event):
    global serp
    if serp.posicion[len(serp.posicion)-1][0]-1!=serp.posicion[len(serp.posicion)-2][0] and serp.direccion!="abajo":
        serp.direccion="arriba"
def sacar4(event):
    global serp
    if serp.posicion[len(serp.posicion)-1][0]+1!=serp.posicion[len(serp.posicion)-2][0] and serp.direccion!="arriba":
        serp.direccion="abajo"
def task():
    sleep(0.1)
    global serp
    global space
    global pera
    global dif
    if serp.estado=="ganar":
        return 0
    if movimiento(serp,space,pera,dif)==False:
        system("clear")
        print "You Lose"
        return 0
    root.after(1,task)
cont=5
system("clear")
while(cont>0):
    print "el juego comienza en...",cont
    sleep(1)
    system("clear")
    cont -= 1
    
space=espacio()
space.x=20
space.y=20
serp=serpiente()
serp.direccion="derecha"
serp.posicion=[[space.x/2,0],[space.x/2,1],[space.x/2,2]]
pera=fruta()
dif=obstaculos()

aparecer_fruta(serp,space,pera,dif)
dibujar(serp,space,pera,dif)

root=Tk()

root.bind('<Left>',sacar1)
root.bind('<Right>',sacar2)
root.bind('<Up>',sacar3)
root.bind('<Down>',sacar4)

root.bind('<a>',sacar1)
root.bind('<d>',sacar2)
root.bind('<w>',sacar3)
root.bind('<s>',sacar4)

root.bind('<A>',sacar1)
root.bind('<D>',sacar2)
root.bind('<W>',sacar3)
root.bind('<S>',sacar4)

root.after(1 , task)
root.mainloop()

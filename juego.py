from random import *
from os import *
from time import *
#Clases
class espacio:
    x=0
    y=0

class serpiente:
    tamano=0
    direccion="derecha"
    posicion=[[0,0],[0,1],[0,2]]
    puntaje=0
    nivel=1
    estado="perder"

class obstaculos:
    posicion=[]

class fruta:
    x=0
    y=10

def avanzar(a):
    g=a.posicion
    l=[1,2]
    if a.direccion=="izquierda":
        l[0]=g[len(g)-1][0]
        l[1]=g[len(g)-1][1]-1
        a.posicion.append(l)
    elif a.direccion=="derecha":
        l[0]=g[len(g)-1][0]
        l[1]=g[len(g)-1][1]+1
        a.posicion.append(l)
    elif a.direccion=="arriba":
        l[0]=g[len(g)-1][0]-1
        l[1]=g[len(g)-1][1]
        a.posicion.append(l)
    elif a.direccion=="abajo":
        l[0]=g[len(g)-1][0]+1
        l[1]=g[len(g)-1][1]
        a.posicion.append(l)
    a.posicion.pop(0);

def limite(a,space):
    o=[]
    t=0
    t=len(a.posicion)-1
    o=a.posicion
    #si choca con el borde superior 
    if o[t][0]<0:
        return 4
    #sichoca con el borde inferior
    elif o[t][0]>=space.y:
        return 2
    #si choca con el borde izquierdp
    elif o[t][1]<0:
        return 1
    #si choca con el borde derecho
    elif o[t][1]>=space.x:
        return 3
    return 0

def ganar(a,space,manzana,dif):
    if a.puntaje>=100 and a.nivel == 1:
        dibujar(a,space,manzana,dif)
        sleep(0.5)
        u=[[space.x/2,0],[space.x/2,1],[space.x/2,2]]
        a.posicion=u
        system("clear")
        x=5
        while(x>0):
            print "nivel 2 en....",x
            sleep(1)
            system("clear")
            x-=1
        a.direccion="derecha"
        a.nivel=2
        a.puntaje = 0
        return True
    elif a.puntaje >= 200 and a.nivel == 2:
        #dibujar(a,space,manzana,dif)
        sleep(0.5)
        u=[[space.x/2,0],[space.x/2,1],[space.x/2,2]]
        dif.posicion=[[space.y-4,space.x-4],[space.y-5,space.x-4],[space.y-4,space.x-5],[space.y-4,3],[space.y-5,3],[space.y-4,4],[3,3],[4,3],[3,4],[3,space.x-4],[3,space.x-5],[4,space.x-4]]
        aparecer_fruta(a,space,manzana,dif)
        for i in range((space.x/4)):
            dif.posicion.append([0,i])
            dif.posicion.append([0,space.x-i-1])
            dif.posicion.append([space.y-1,i])
            dif.posicion.append([space.y-1,space.x-i-1])
        for i in range(1,(space.x)/4):
            dif.posicion.append([i,0])
            dif.posicion.append([space.y-i-1,0])
            dif.posicion.append([i,space.x-1])
            dif.posicion.append([space.y-i-1,space.x-1])
        a.posicion=u
        system("clear")
        x=5
        while(x>0):
            print "nivel 3 en....",x
            sleep(1)
            system("clear")
            x-=1
        a.direccion="derecha"
        a.nivel=3
        a.puntaje=0
        return True
    elif a.puntaje>=300:
        dibujar(a,space,manzana,dif)
        sleep(0.5)
        system("clear")
        print "usted ha ganado el juego con",a.puntaje,"puntos"
        a.estado="ganar"
        return True
    return False

def movimiento(a,space,manzana,dif):
    x=True
    r=[1,2]
    r=a.posicion[0]
    avanzar(a)
    for i in range(len(a.posicion)-1):
        if(a.posicion[i]==a.posicion[len(a.posicion)-1]):
            return ganar(a,space,manzana,dif)
    if a.nivel == 3:
        for i in dif.posicion:
            if i == a.posicion[len(a.posicion)-1]:
                return ganar(a,space,manzana,dif)
    z=limite(a,space)
    if a.nivel == 2:
        if z != 0:
            if a.puntaje >= 200:
                return ganar(a,space,manzana,dif)
            else:
                return False
    else:
        if z!=0:
            if z==1:
                a.posicion[len(a.posicion)-1][1]=space.x-1
            elif z==2:
                a.posicion[len(a.posicion)-1][0]=0
            elif z==3:
                a.posicion[len(a.posicion)-1][1]=0
            elif z==4:
                a.posicion[len(a.posicion)-1][0]=space.y-1

    p_comiofruta(a,space,manzana,r,dif)
    if x==False:
        return False
    if x:
        dibujar(a,space,manzana,dif)
    return x

def aparecer_fruta(a,space,manzana,dif):
    x=0
    y=0
    b=True
    while(b):
        y=randrange(0,space.y)
        x=randrange(0,space.x)
        b=False
        for i in a.posicion:
            if(i==[y,x]):b=True
        for i in dif.posicion:
            if(i==[y,x]):b=True
    manzana.x = x
    manzana.y = y
    
def comer_fruta(a,space,manzana,dif):
    a.puntaje += 10
    aparecer_fruta(a,space,manzana,dif)

def p_comiofruta(a,space,manzana,r,dif):
    l=[manzana.y,manzana.x]
    if(a.posicion[len(a.posicion)-1] == l):
        a.posicion.insert(0,r)
        comer_fruta(a,space,manzana,dif)
        return True
    return False

def dibujar(a,space,manzana,dif):
    system("clear")
    print "puntaje:",a.puntaje,"          ","nivel",a.nivel
    l=[]
    u=[]
    for i in range(space.x+2):
        if(a.nivel==2):
            print "X",
        else:
            print '.',
    print ""
    for i in range(space.y):
        for i in range(space.x):
            u.append(' ')
        l.append(u)
        u=[]
    for i in range(len(dif.posicion)):
        l[dif.posicion[i][0]][dif.posicion[i][1]]="X"
    for i in range(len(a.posicion)):
        l[a.posicion[i][0]][a.posicion[i][1]]='o'
    l[manzana.y][manzana.x]="*"
    for i in range(len(l)):
        if(a.nivel==2):
            print"X",
        else:
            print'.',
        for j in range(len(l[i])):
            print l[i][j],
        if(a.nivel == 2):
            print "X"
        else:
            print '.'
            
    for i in range(space.x+2):
        if(a.nivel==2):
            print 'X',
        else:
            print '.',
    print ""

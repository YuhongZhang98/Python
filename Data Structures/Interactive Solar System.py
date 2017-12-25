#Yuhong Zhang
import turtle
import math
import random
class Sun:
    def __init__(self,center,size,color):
        self.center=center
        self.size=size
        self.color=color
        self.radius=0
        self.angle=0
        self.location=center
    def draw(self):
        drawPlanet(self.center,self.size,self.color,self.radius,self.angle)
    def move(self):
        self.location = [x + self.radius * f(angle)
                    for x, f in zip(self.center, (math.sin, math.cos))]
    def setColor(self,color):
        self.color=color
    def inside(self,location):
        if (location[0]-self.location[0])**2+(location[1]-self.location[1])**2<=self.size**2:
            return True
    def onClick(self,location):
        if self.inside(location)==True:
            self.setColor(randomColor())
            global on
            on=self

class Planet(Sun):
    def __init__(self,orbitAround,orbitRadius,size,color,speed):
        self.center=orbitAround.center
        self.location=orbitAround.center
        self.orbitAround=orbitAround
        self.radius=orbitRadius
        self.size=size
        self.color=color
        self.speed=speed
        self.angle=0
    def move(self):
        self.center=self.orbitAround.location
        self.location = [x + self.radius * f(self.angle)
                    for x, f in zip(self.center, (math.sin, math.cos))]
        self.angle+=self.speed


class SolarSystem():
    def __init__(self):
        self.system=[]
        sun=Sun((0,0),40,'red')
        numPlanet=2+int(random.random()*3)
        numMoon=3+int(random.random()*4)
        for i in range(numPlanet):
            planet=Planet(sun,70+random.random()*200,20+random.random()*20,randomColor(),0.005+random.random()*0.005)
            self.system.append(planet)
        moons=[]
        for i in range(numMoon):
            moon=Planet(self.system[int(random.random()*numPlanet)-1],30+random.random()*50,10+random.random()*20,randomColor(),0.01+random.random()*0.005)
            self.system.append(moon)
        self.system.append(sun)
    def draw(self):
        for p in self.system:
            p.move()
            p.draw()
    def onClick(self,location):
        for p in self.system:
            p.onClick(location)

def randomColor():
    return [random.random() for i in range(3)]

def drawPlanet(center,size,color,orbitRadius,angle):
    location=[x+orbitRadius*f(angle)
              for x,f in zip(center, (math.sin,math.cos))]
    turtle.penup()
    turtle.goto(*location)
    turtle.dot(size*2,color)
def draw():
    turtle.clear()
    turtle.tracer(0,0)
    solar.draw()
    screen.ontimer(draw,0)
def onClick(x,y):
    solar.onClick((x,y))
def keyUp():
    on.size+=10
def keyDown():
    if on.size>10:
       on.size-=10
def keyLeft():
    on.radius+=10
def keyRight():
    on.radius-=10
def keyRSB():
    on.speed+=0.05
def keyLSB():
    on.speed-=0.05
def keyN():
    solar.system.append(Planet(on, 70 + random.random() * 200, 20 + random.random() * 20, randomColor(),0.005 + random.random() * 0.005))
def keySpace():
    on.setColor(randomColor())
solar=SolarSystem()
angle=0
turtle.tracer(0,0)
turtle.ht()
screen=turtle.Screen()
screen.onkey(turtle.bye,"q")
screen.ontimer(draw,0)
screen.onclick(onClick)
screen.onkey(keyRight,'Right')
screen.onkey(keyLeft,'Left')
screen.onkey(keyUp,'Up')
screen.onkey(keyDown,'Down')
screen.onkey(keyN,'n')
screen.onkey(keySpace,' ')
screen.onkey(keyLSB,'[')
screen.onkey(keyRSB,']')
screen.listen()
turtle.mainloop()


'''Yuhong Zhang
moving mouse to sway the tree 
up and down make the tree grow bigger or smaller 
"[" and "]" to change the angles between branches
"l" to remove leaves
'''


import sys
import random
import math


def setup():
    global recurNum,angle,A
    size(1920, 2080)
    background(255)
    pixelDensity(displayDensity())
    recurNum=4
    angle=0
    A=30
def drawLeaves(n,color, start, angle, length,width=0):
    if n==0:
        return
    end = (start[0] + math.sin(math.radians(angle+180)) * length,
           start[1] + math.cos(math.radians(angle+180)) * length)
    n-=1
    global count
    count+=1
    if width:
        strokeWeight(width)
    else:
        noStroke()
    line(*(start + end))
    if leaf:
       drawLeaf(end)
    if number:
       drawNumber(end,count-1)
    drawLeaves(n,color,end,angle+A,length*0.8,width=0)
    drawLeaves(n,color,end,angle-A,length*0.8,width=0)
    return end

def drawLineAngle(n,color, start, angle, length,width=24):
    if n==0:
        return
    end = (start[0] + math.sin(math.radians(angle+180)) * length,
           start[1] + math.cos(math.radians(angle+180)) * length)
    stroke(*color)
    if width:
        strokeWeight(width)
    else:
        noStroke()
    line(*(start + end))
    n-=1

    drawLineAngle(n,color,end,angle+A,length*0.8,width*0.7)
    drawLineAngle(n,color,end,angle-A,length*0.8,width*0.7)
    
    return end

def drawLeaf(location):
        stroke(0, 50, 0)
        fill(100, 255, 100)
        strokeWeight(0.5)
        ellipse(location[0],location[1],40,40)
def drawNumber(location,num):        
        fill(0,0,0)
        text(num,location[0],location[1])
        textSize(24)
        textAlign(CENTER,CENTER)

    
def drawTree(start):
    angle=(960-mouseX)/15
    drawLineAngle(recurNum,(0,0,0),start,angle,200,30)
    drawLeaves(recurNum,(0,0,0),start,angle,200)


def keyPressed():
    global leaf,number,recurNum,angle,A
    if key==CODED:
        if keyCode==UP:
            recurNum+=1
        if keyCode==DOWN:
            if recurNum>1:
                recurNum-=1
        if keyCode==LEFT:
            angle+=10
        if keyCode==RIGHT:
            angle-=10
    if key=="[":
        A+=10
    if key=="]":
        A-=10
             
            
    if key=="l":
        leaf = not leaf
        number=not number
def setup():
    global leaf,count,number,recurNum,angle,A
    count=0
    leaf=True
    number=True
    recurNum=4
    angle=0
    A=30
def draw():

    global count
    count=0
    
    clear()
    
    background(255)
    drawTree((960,1080))
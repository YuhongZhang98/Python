import copy

w = 30 # width of each cell

def setup():
    frameRate(5)
    global grid,size,numSet,play,countGrid,newGrid
    size=15
    play=True
    numSet = [-1, 1]
    countGrid = [ [0]*size  for n in range(size)]
    newGrid=[ [0]*size  for n in range(size)]
    grid = [ [-1]*size  for n in range(size)] # list comprehension
    for row in range(size):
        for col in range(size):
            grid[row][col]=numSet[int(random(2))]
    size(800,600)
    
def draw():
 global grid,countGrid,play,newGrid
 if play:
     newGrid=copy.deepcopy(grid)
     for i in range(size):
        for j in range(size):
            count=0
            if i >0 and j >0:
                if grid[i-1][j-1]==1:
                    count+=1
            if i>0:
                if grid[i-1][j]==1:
                    count+=1
            if i>0 and j<size-1:
                if grid[i-1][j+1]==1:
                    count+=1
            if j>0:
                if grid[i][j-1]==1:
                    count+=1
            if j<size-1:
                if grid[i][j+1]==1:
                    count+1
            if i<size-1 and j>0:
                if grid[i+1][j-1]==1:
                    count+=1
            if i<size-1:
                if grid[i+1][j]==1:
                    count+=1
            if i<size-1 and j<size-1:
                if grid[i+1][j+1]==1:
                    count+=1
            if grid[i][j]==1 and count<2:
                newGrid[i][j]=-1
            if grid[i][j]==1 and count>3:
                newGrid[i][j]=-1
            if grid[i][j]==-1 and count==3:
                newGrid[i][j]=1
            countGrid[i][j]=count
     grid=copy.deepcopy(newGrid)
     for i in range(size):
        for j in range(size):
            count=0
            if i >0 and j >0:
                if grid[i-1][j-1]==1:
                    count+=1
            if i>0:
                if grid[i-1][j]==1:
                    count+=1
            if i>0 and j<size-1:
                if grid[i-1][j+1]==1:
                    count+=1
            if j>0:
                if grid[i][j-1]==1:
                    count+=1
            if j<size-1:
                if grid[i][j+1]==1:
                    count+1
            if i<size-1 and j>0:
                if grid[i+1][j-1]==1:
                    count+=1
            if i<size-1:
                if grid[i+1][j]==1:
                    count+=1
            if i<size-1 and j<size-1:
                if grid[i+1][j+1]==1:
                    count+=1
            countGrid[i][j]=count
     x,y = 0,0 # starting position

     for row in range(size):
        for col in range(size):
            if grid[row][col] == 1:
                count=countGrid[row][col]
                if count==1:
                    fill(250,0,0)
                if count==2:
                    fill(0,250,0)
                if count==3:
                    fill(0,0,250)
                if count==4:
                    fill(250,250,0)
                if count==5:
                    fill(0,250,250)
                if count==6:
                    fill(250,0,250)
                if count==7:
                    fill(125,0,0)
                if count==8:
                    fill(0,125,0)
                if count==0:
                    fill(0,0,125)
            else:
               fill(255)
            rect(x, y, w, w)
            x = x + w  # move right
        y = y + w # move down
        x = 0 # rest to left edge

def clearGrid():
    global grid
    print('a')
    for i in range(size):
        for j in range(size):
            grid[i][j]=-1
    
def randomGrid():
    global grid
    for i in range(size):
        for j in range(size):
            grid[i][j]=numSet[int(random(2))]            
                
def keyPressed():
    global play
    if key==" ":
        if play:
            play=False
        else:
            play=True
    if key=="n":
        clearGrid()        
    if key=="r":
        randomGrid()
            
def mousePressed():
    global grid,newGrid
    print('a')
    newGrid[mouseY/w][mouseX/w] = -1 * grid[mouseY/w][mouseX/w]
    grid[mouseY/w][mouseX/w] = -1 * grid[mouseY/w][mouseX/w]  
    # integer division is good here!
class TextBox:
    TEXTSIZE = 30

    def __init__(self, text, x=0, y=0):
        self._text, self._x, self._y = text, x, y

    def replaceText(self, text):
        self._text = text

    def setLocation(self, x, y):
        self._x, self._y = x, y

    def draw(self):
        textAlign(LEFT, TOP)
        textSize(TextBox.TEXTSIZE)
        rectMode(CORNER)
        fill(255)
        stroke(0)
        strokeWeight(1)
        rect(self._x, self._y, self.width(), self.height())
        fill(0)
        text(self._text, self._x + textWidth(" ") //
             2, self._y - textDescent() // 2)

    def width(self):
        textSize(TextBox.TEXTSIZE)
        return textWidth(self._text + " ")

    def height(self):
        textSize(TextBox.TEXTSIZE)
        return textAscent() + textDescent()

    def drawLineToOtherBoxBelow(self, otherBox):
        stroke(0)
        textSize(TextBox.TEXTSIZE)
        strokeWeight(1)
        line(self._x + self.width() / 2, self._y + self.height(),
             otherBox._x + otherBox.width() / 2, otherBox._y)


class suffixTrie:
    
    class Node:
        def __init__(self):
            self.children={}
        
        def draw(self,c,x,y):
            textbox=TextBox(c,x,y)
            textbox.draw()
            endx=x
            for c in self.children:
                endx,child=self.children[c].draw(c,endx,y+50)
                textbox.drawLineToOtherBoxBelow(child)
                endx+=20
            return endx,textbox  
        
        
        def recur(self,node,string):
            if len(node.children.keys())==0 or len(node.children.keys())>1:
                return (node,string)
            else:
                return recur(node.children[node.children.keys[0]],string+node.children.keys[0])
            
        def print_console(self,level):
            for val in self.children:
                print str(level)+val,self.children[val].print_console(level+1)
            print
        '''def findKeyFirst(self,S):
            for i in range(len(S)): 
                cur=[]
                for c in t[i:]:  
                    if c not in cur:
                        cur[c]={}
                    cur=cur[c]
        def findKey(self,S,key):
            char=[]
            for i in range(1,len(S)):
                findKey=False
                if S[i-1]==key:
                    findKey=True
                for j in char:
                    if S[i]==j:
                        findKey=False
                if findKey:
                    char.append(S[i])
            for i in char:
                self.children=None
            if len(S)>1:
                if len(char)==0:
                    self.children[S[0]]=S[1:]
                else:
                    for i in self.children.keys():
                        for j in range(len(S)):
                            if s[j]==i:
                                self.children[i]=s[(j+1):]
                                break
            else:
                self.children['$']=''
                '''
    def __init__(self,S):
        self._root=self.Node()
        for i in range(len(S)):
            temp=self._root
            for j in S[i:]:
                if j not in temp.children:
                    temp.children[j]=self.Node()
                temp=temp.children[j]
    
        
    
                    
    '''def build(self,node):
        for i in node.children.keys():
            if i != '$':
                node.children[i]=self.Node(node.children[i],False)
                self.build(node.children[i])'''
    def print_console(self,x):
        self._root.print_console(x)
    def draw(self,x,y):
        self._root.draw('',x,y)

def keyPressed():
    global S
    if key==u'\x08':
        S=S[:-1]
    elif key!=65535:
        S+=key
    redraw()
def setup():
    global S
    S=""
    size(1200, 1000)
    pixelDensity(displayDensity())
    noLoop()
def draw():
    background(200,150,200)
    TextBox(S,10,10).draw()
    ST=suffixTrie(S)
    ST.draw(50,100)
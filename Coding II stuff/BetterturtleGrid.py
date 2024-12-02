from turtle import*

hideturtle()
speed(10000)

penup()
goto(-400, 200)
pendown
write("Colors:", True, align="left")
goto(-400,190)
write("color red = r ", True, align="left")
goto(-400,180)
write("color green = g ", True, align="left")
goto(-400,170)
write("color blue = b ", True, align="left")
goto(-400,160)
write("color black = B ", True, align="left")
goto(-400,150)
write("color orange = o ", True, align="left")
goto(-400,140)
write("color yellow  = y ", True, align="left")
goto(-400,130)
write("color lime  = l ", True, align="left")
goto(-400,120)
write("color gold  = G ", True, align="left")
goto(-400,110)
write("color pink  = p ", True, align="left")
goto(-400,100)
write("RAINBOW  = SPACE (NOT WORKING) ", True, align="left")

num = int(numinput("lol ur traped goofy:", "Enter a random number goofy goober :p", default=None,minval=None,maxval=None))
pencolors = ['red', 'purple', 'blue', 'green', 'orange', 'white', 'black']
randomcolors = ['red', 'lime', 'purple', 'blue', 'green', 'orange', 'yellow', 'white', 'black']

#draws the gird
def gridBox(TL=(0,0),scale=25):
    #TL=TL
    TR=(TL[0]+scale,TL[1])
    BL=(TL[0],TL[1]-scale)
    BR=(TL[0]+scale,TL[1]-scale)
    goto(TL)
    pendown()
    begin_fill()
    goto(TR)
    goto(BR)
    goto(BL)
    goto(TL)
    end_fill()
    penup()
    
def drawGrid(num,scale=25):
    for x in range(0,(scale * num),scale):
        for y in range(0,(scale * num),scale):  
            gridBox((x,y))

def redcolor():
    fillcolor('red')
    pencolor('red')

def greencolor():
    fillcolor('green')
    pencolor('green')

def blackcolor():
    fillcolor('black')
    pencolor('black')

def orangecolor():
    fillcolor('orange')
    pencolor('orange')

def bluecolor():
    fillcolor('blue')
    pencolor('blue')

def yellowcolor():
    fillcolor('yellow')
    pencolor('yellow')

def limecolor():
    fillcolor('lime')
    pencolor('lime')

def pinkcolor():
    fillcolor('pink')
    pencolor('pink') 

def goldcolor():
    fillcolor('gold')
    pencolor('gold')   

def rainbowcolor():
    fillcolor('red')
    pencolor('red')
    
    fillcolor('orange')
    pencolor('orange')
    
    fillcolor('yellow')
    pencolor('yellow')
    
    fillcolor('green')
    pencolor('green')
    
    fillcolor('blue')
    pencolor('blue')
    
    fillcolor('purple')
    pencolor('purple')

onkeypress(redcolor,"r")
onkeypress(greencolor,"g")
onkeypress(bluecolor,"b")
onkeypress(blackcolor,"B")
onkeypress(orangecolor,"o")
onkeypress(yellowcolor,"y")
onkeypress(limecolor,"l")
onkeypress(pinkcolor,"p")
onkeypress(goldcolor,"G")
onkeypress(rainbowcolor," ")

listen("r")
listen("g")
listen("b")
listen("B")
listen("o")
listen("y")
listen("l")
listen("p")
listen("G")
listen(" ")

drawGrid(num)

#gridColor()
mainloop()
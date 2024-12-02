# Animal Drawing Here:
# Rules 900 x 900 canvas size
#       pensize: 4
# Single Function called "Draw_(Animal Name Here)"

from turtle import*

pensize(4)
screensize(900, 900)
speed(15)
#bgpic('C:\\Users\\Landon Russell\\Desktop\\Coding Folders\\Coding II\\Deer.png')

def draw_deer():
    # Skull
    penup()
    goto(0,-100)
    pendown()
    forward(30) 
    left(45)
    forward(40)
    left(60)
    forward(60)
    right(35)
    forward(70)
    right(20)
    forward(40)
    right(50)
    forward(25)
    left(60)
    forward(30)
    right(65)
    forward(45)
    left(40)
    forward(80)
    left(25)
    forward(55)
    left(140)
    forward(105)
    left(180)
    forward(105)
    left(165)
    forward(100)
    left(25)
    forward(60)
    right(165)
    forward(60) #
    right(40)
    forward(120)
    left(25)
    forward(60)
    left(60)
    forward(160)
    left(170)
    forward(130)#
    right(30)
    forward(55)#
    right(125)
    forward(90)
    left(160)
    forward(90)
    right(80)
    forward(60)
    right(65)
    forward(65)#
    right(35)
    forward(50)
    left(160)
    forward(60)
    left(55)
    forward(60)
    right(115)
    forward(55)
    left(60)
    forward(65)
    right(65)
    forward(80)

    penup()
    goto(0,-100)
    pendown()
    forward(30) #
    right(45)
    forward(40) #
    right(60)
    forward(60) #
    left(35)
    forward(70) #
    left(20)
    forward(40) #
    left(50)
    forward(25) #
    right(60)
    forward(30) #
    left(65)
    forward(45) #
    right(40)
    forward(80) #
    right(25)
    forward(55) #
    right(140)
    forward(105)#
    right(180)
    forward(105)#
    right(165)
    forward(100)#
    right(25)
    forward(60)#
    left(165)
    forward(60)#
    left(40)
    forward(120)#
    right(25)
    forward(60) #
    right(60)
    forward(160)#
    right(170)
    forward(130)#
    left(30)
    forward(55)#
    left(125)
    forward(90)#
    right(160)
    forward(90)#
    left(80)
    forward(60)#
    left(65)
    forward(65)#
    left(35)
    forward(50)
    right(160)
    forward(60)
    right(55)
    forward(60)
    left(115)
    forward(55)
    right(60)
    forward(65)
    left(65)
    forward(80)

    # Nostrils
    penup()
    goto(-40,-55)
    pendown()
    right(20)
    forward(20)

    penup()
    goto(40,-55)
    right(180)
    pendown()
    left(40)
    forward(20)

    # Eyes
    penup()
    goto(-117, 85)
    pendown()
    left(100)
    forward(30)
    left(63)
    forward(27)

    penup()
    goto(117, 85)
    pendown()
    right(120)
    forward(30)
    right(65)
    forward(30)

    # Jawline
    penup()
    goto(-117,85)
    pendown()
    left(105)
    forward(130)
    left(50)
    forward(38)

    penup()
    goto(117,85)
    pendown()
    right(75)
    forward(130)
    right(50)
    forward(40)

    # Mouth
    penup()
    goto(-25,-100)
    pendown()
    left(90)
    forward(30)
    left(65)
    forward(15)

    penup()
    goto(25,-100)
    pendown()
    right(120)
    forward(30)
    right(65)
    forward(15)
    
    
draw_deer()

mainloop()
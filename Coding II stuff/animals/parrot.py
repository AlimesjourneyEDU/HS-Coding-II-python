#LEVIS PARROT
from turtle import*


# Rules: 900 x 900 canvas
pensize(4)
screensize(900,900)
speed(999)

def draw_parrot():
    #First Half
    hideturtle()
    penup()
    goto(0,350)
    pendown()
    goto(-100,300)
    goto(-160,150)
    goto(-230,50)
    goto(-180,0)
    goto(-180,-50)
    goto(-90,-40)
    goto(-40,-80)
    goto(0,-20)
    penup()
    goto(0,250)
    pendown()
    goto(-40,230)
    goto(-60,150)
    goto(0,0)
    end_fill()
    penup()
    goto(-75,270)
    pendown()
    goto(-30,270)
    goto(-40,250)
    goto(-85,250)
    goto(-75,270)

#Second half
    clone()
    hideturtle()
    penup()
    goto(0,350)
    pendown()
    goto(100,300)
    goto(160,150)
    goto(230,50)
    goto(180,0)
    goto(180,-50)
    goto(90,-40)
    goto(40,-80)
    goto(0,-20)
    penup()
    goto(0,250)
    pendown()
    goto(40,230)
    goto(60,150)
    goto(0,0)
    end_fill()
    penup()
    goto(75,270)
    pendown()
    goto(30,270)
    goto(40,250)
    goto(85,250)
    goto(75,270)
    
    
   


draw_parrot()
mainloop()
#END OF LEVIS PARROT
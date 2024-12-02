from turtle import*
hideturtle()
speed(10000)

num = int(numinput("lol ur traped goofy:", "Enter a random num ber goofy goober :p", default=None,minval=None,maxval=None))





def gridBox(TL=(0,0),scale=25):
    #TL=TL
    TR=(TL[0]+scale,TL[1])
    BL=(TL[0],TL[1]-scale)
    BR=(TL[0]+scale,TL[1]-scale)
    goto(TL)
    pendown()
    goto(TR)
    goto(BR)
    goto(BL)
    goto(TL)
    penup()

    
def drawGrid(num,scale=25):
    for x in range(0,(scale * num),scale):
        for y in range(0,(scale * num),scale):  
            gridBox((x,y))


    
        

drawGrid(num)
mainloop()
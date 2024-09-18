
    #TurtleGraphics.py
#Name:
#Date:
#Assignment:

import turtle #needed generally but not in CodeHS
hideturtle() #hides the default turtle in CodeHS

def drawSquare(t, size):
    for i in range(4):
        t.forward(size)
        t.right(90)


def main():
    t = turtle.Turtle()
    # drawPolygon(myTurtle, 5) #draws a pentagon
    # drawPolygon(myTurtle, 8) #draws an octogon
    def drawPolygon(t,sides):
        for i in range(sides):
            forward(40)
            right(360/sides)
    #drawPolygon(t, 8) #draws an octogon
    # fillCorner(myTurtle, 2) #draws a square with top right corner filled in.
    # fillCorner(myTurtle, 3) #draws a square bottom left corner filled in.
    def fillcorner(t,corner):
        t.penup()
        t.goto(-150,150)
        t.pendown()
        for i in range(4):
            t.forward(300)
            t.right(90)
        quad=corner
        if (quad=="1"):
            t.penup()
            t.goto(0,0)
            t.pendown()
        elif (quad=="2"):
            t.penup()
            t.goto(-150,0)
            t.pendown()
        elif (quad=="3"):
            t.penup()
            t.goto(0,-150)
            t.pendown()
        elif (quad=="4"):
            t.penup()
            t.goto(-150,-150)
            t.pendown()
        t.begin_fill()
        for i in range(4):
            t.forward(150)
            t.left(90)
        t.end_fill()
    # squaresInSquares(myTurtle, 5) #draws 5 concentric squares
    # squaresInSquares(myTurtle, 3) #draws 3 concentric squares
    def squaresInSquares(t,squ):
        t.penup()
        t.goto(-150,150)
        t.pendown()
        len=300
        for i in range(squ):
            drawSquare(t,len)
            t.penup()
            t.forward(100/squ)
            t.right(90)
            t.forward(100/squ)
            t.left(90)
            t.pendown()
            len=len-(200/squ)
    #squaresInSquares(t, 10) #draws 3 concentric squares
          
            

main()

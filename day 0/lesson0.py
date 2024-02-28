from turtle import* 

#we want to paint a house 

#step 1: draw a square 

width(5)


color("blue")

forward(200)
left(90)
    
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door

forward(70)
color("yellow")
begin_fill()
left(90)
forward(100)    # height of  the door
right(90)
forward(60)
right(90)
forward(100)
end_fill()

penup()
goto(200,200)
pendown() 

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

# drawing a window
color("blue")
left(120)
color("")
forward(200)
right(90)

forward(70)

right(90)

forward(20)
color("GREEN")
begin_fill()
right(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
end_fill()
right(180)
color("")
forward(120)
color("GREEN")
begin_fill()
right(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
end_fill()
exitonclick()

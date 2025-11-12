import turtle
t1 = turtle.Turtle ()
t2 = turtle.Turtle ()
t3 = turtle.Turtle ()

t1.penup()
t1.goto (-90,0)
t1.pendown()
t1.color("dark magenta")
turtle.Screen().bgcolor("pink")
t1.speed (10)
# i changed where my shape was so it could be more in the middle instead of upper left
for i in range (100):
    t1.forward(200 + i)
    t1.left(150) 

t2.penup()
t2.goto (-90,0)
t2.pendown()
t2.color("peach puff")
t2.speed (9)

for i in range (100):
    t2.forward(200 - i)
    t2.left(150) 

t3.penup()
t3.goto (-80,0)
t3.pendown()
t3.color("MediumAquamarine")
t3.speed (10)
#i changed the white color to Medium Auquamaine because people said the white was too hard to see


for i in range (100):
    t3.forward(200 + i)
    t3.left(170) 
    






turtle.exitonclick ()




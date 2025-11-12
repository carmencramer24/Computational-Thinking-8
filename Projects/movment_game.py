# Section 1 - Helper functions (DON'T CHANGE!!)
import turtle, math, time, random
def set_background(image_filename):
	screen = turtle.Screen()
	try:
		screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.png")
	except:
		screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.gif")

def set_image(sprite, image_filename):
    image_file = f"./Images/{image_filename}.gif"
    screen = turtle.Screen()
    screen.register_shape(image_file)
    sprite.shape(image_file)

def create_sprite(image_filename, x=0, y=0):
    sprite = turtle.Turtle()
    set_image(sprite, image_filename)
    sprite.penup()
    sprite.goto(x,y)
    window.update()
    return sprite

def get_distance(s1, s2):
	dx = s1.xcor() - s2.xcor()
	dy = s1.ycor() - s2.ycor()
	return math.sqrt(dx*dx + dy*dy)

def draw_rectangle( color="black",x=0,y=0, width=100, height=100,):
	sprite = turtle.Turtle()
	sprite.speed(0)
	sprite.pencolor(color)
	sprite.color(color)
	sprite.penup()
	sprite.goto(x - (width*0.5), y + (height*0.5))
	sprite.pendown()
	sprite.begin_fill()
	for i in range(2):
		sprite.forward(width)
		sprite.right(90)
		sprite.forward(height)
		sprite.right(90)
	sprite.end_fill()
	sprite.hideturtle()


window = turtle.Screen()
window.tracer(0)


# Section 2: Setup
#spotlight

lives = 3

# TODO - create your player character
s2 = create_sprite("Spotlight",0,-130 )
s1 = create_sprite("sugar_plum",0,-130)

# TODO - set your background
set_background("Stage")
# TODO - set the starting value for your variable

# Section 3: Controls
# TODO - define your controls
def move_up():
	s1.setheading(90)
	s1.forward(10)

def move_down():
	s1.setheading(270)
	s1.forward(10)

def move_left():
	s1.setheading(180)
	s1.forward(10)

def move_right():
	s1.setheading(0)
	s1.forward(10)

# pick keys for each control
window.onkeypress(move_up, "w")
window.onkeypress(move_down, "s")
window.onkeypress(move_left, "a")
window.onkeypress(move_right, "d")

s1.speed(10)


# Section 4: Game Loop
window.listen()
timer = 0
while True:
	time.sleep(1.0)
	timer += 1  

	 
    
 	#  code for automatic actions
	s2.setheading(random.randint(30, 360))
	s2.forward(10)
	s2.speed(4)

	

	#what happens if not touching spotlight
	if get_distance(s1, s2) >80:
		lives -= 1





	window.update()

	# if :
	if lives == 0:
		draw_rectangle("light pink", 200, 200, 200, 200)
		message1 = create_sprite("alien",200,200)
		message1.color("black")
		message1.write("YOU LOSE",font = ("Arial", 40, "normal"))
		message1.hideturtle()

		break 


	

print(f"Game Over, your score is {timer}")
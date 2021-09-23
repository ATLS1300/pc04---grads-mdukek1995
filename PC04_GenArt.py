"""
Created on Thu Sep 15 11:39:56 2020
PC04 start code
@author: Megan

"""
import turtle
import math, random

turtle.colormode(255)
# turtle.tracer(0) # uncomment this line to turn off turtle's animation. You must update the image yourself using panel.update() (line 42)

# Create a panel to draw on. 
panel = turtle.Screen()
w = 600 # width of panel
h = 600 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making 
image= "pine.gif"
panel.bgcolor("black")
panel.bgpic(image)

palette = ((0,18,25),(0,95,115),(10,147,150),(148,210,189), (233,216,166),(238,155,0),(202,103,2),(187,62,3),(174,32,18),(155,34,38))


# set first turtle's attributes- this turtle will move vertically
turtleVertical = turtle.Turtle()
turtleVertical.pensize(10)
turtleVertical.penup()
turtleVertical.speed(8)
# set second turtle's attributes- this turtle will move across horizontal axis
turtleHorizontal = turtle.Turtle()
turtleHorizontal.pensize(10)
turtleHorizontal.penup()
turtleHorizontal.speed(8)
# set third turtle's attributes- this turtle will make clusters that mimic pine
clusterTurtle = turtle.Turtle()
clusterTurtle.pensize(3)
clusterTurtle.penup()


for i in range(-300,-100, 10):
     turtleVertical.color(random.choice(palette))  # turtle will select a random color from the list
     turtleVertical.goto(i,300)  # turtle will go to random location along x-axis at top of image
     turtleVertical.setheading(270)  # turns turtle south
     turtleVertical.pendown()
     turtleVertical.forward(600)
     turtleVertical.penup()
       
for i in range(200):
     turtleHorizontal.color(random.choice(palette))
     turtleHorizontal.goto(-300,random.randint(-300,300)) # turtle will go to random location along y-axis
     turtleHorizontal.setheading(turtleHorizontal.towards(0,0)) # turtle will angle itself to move towards origin 
     turtleHorizontal.pendown()
     turtleHorizontal.forward(200)
     turtleHorizontal.penup()

# shortcut for creating cluster shape since I will do multiple in different locations.
def cluster():
    clusterTurtle.color(random.choice(palette))
    clusterTurtle.goto(random.randint(-100,200),random.randint(-150,150))
    length= random.randint(10,35)
    for i in range(20):
        clusterTurtle.pendown()
        clusterTurtle.forward(length)
        clusterTurtle.right(180)
        clusterTurtle.forward(length)
        clusterTurtle.right(18) #360/20
        clusterTurtle.penup()
        
for i in range(4):
    cluster()
    
#built from Kaily Fox's pseudocode
# enter code below
turtle.penup()
turtle.goto (100,100)
turtle.setheading(90)
turtle.color(palette[5])
turtle.pendown()
turtle.circle(55)
turtle.color(palette[1])
turtle.setheading(270)
for i in range(36):
    turtle.circle(20)
    turtle.right(10)
    turtle.forward(10)

    

# You must use 2 for loops (a nested for loop counts as 2!)
# You must use at least 1 random element (something from the random library)
# Don't forget to comment your code! (what does each for loop do? What does the random function you'll use do?)

# =============== ADD YOUR CODE BELOW! =================




# panel.update() # uncomment this if you've turned off animation (line 26). I recommend leaving this outside of loops, for now.
# =================== CLEAN UP =========================
# uncomment the line below when you are finished with your code (before you turn it in)
# turtle.done()

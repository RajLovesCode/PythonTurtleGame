import turtle
import random
'''
# create the arena
# create 2 separate sides w/ tunnell access
# create 2 separate teams of 10 turtles each, red and blue
# have them start on separate sides
# turtles bounce off all barriers accept the tunnell
# first to consume all of opposing team's turtles wins, you get one point for eating a turtle, 2 points #for eating a bigger turtle, 4 points for eating a really big turtle, 
# Game ends when screen turns from black to green
'''
#background
background=turtle.Screen() 
background.tracer(0)
r= 20
g= 20 
b= 20 

#arena
arena=turtle.Turtle()
arena.pensize(10)
arena.color("pink")
arena.speed(1000000)
arena.penup()
arena.goto(340,-200)
arena.pendown()
arena.left(90)
arena.forward(450)
arena.left(90)
arena.forward(676)
arena.left(90)
arena.forward(450)
arena.left(90)
arena.forward(676)
 
# barriers
barriers=turtle.Turtle()
barriers.pensize(10)
barriers.color("pink")
barriers.penup()
barriers.goto(0,200)
barriers.pendown()  
barriers.setheading(270) 
barriers.forward(150)
barriers.penup()
barriers.forward(75)
barriers.pendown()
barriers.forward(150)

#red and blue

red=turtle.Turtle()
red.color("dark red") 
red.shape("turtle")
red.penup()
red.goto(-200,0)
def right():
  red.right(5)

def left():
  red.left(5)
  
blue=turtle.Turtle() 
blue.color(" dark blue")
blue.shape("turtle")
blue.setheading(180)
blue.penup()
blue.goto(200,0)
def blueright ():
  blue.right(5)
 
def blueleft():
   blue.left(5)
 
 
background.onkey(right,"right")
background.onkey(left,"left") 
 
background.onkey(blueright,"d")
background.onkey(blueleft,"a") 
 
 
background.listen()
 
# turtle lists
bluet=[]

for i in range (9):
  bluet.append(turtle.Turtle())
  bluet[i].color(" blue")
  bluet[i].shape("turtle")
  bluet[i].penup()
  bluet[i].speed(1000000)
  bluet[i].right(random.randint(1,360))
#  bluet[i].setheading(270)
  bluet[i].goto(random.randint(50,250),random.randint(-180,240))
 

redt=[] 
 
for i in range(9):
  redt.append(turtle.Turtle())
  redt[i].color("red")
  redt[i].shape("turtle")
  redt[i].penup()
  redt[i].speed(0)
  redt[i].right(random.randint(0,360))
 # redt[i].setheading(270)
  redt[i].goto(random.randint(-270,1),random.randint(-180,240))



all_t = redt + bluet
#bouncing off walls part
def redb():
  if red.xcor() < -317 or red.xcor() > 320 or red.ycor() > 237  or red.ycor() < -180:
       red.right(180) 
def blueb():
  if blue.xcor() < -317 or blue.xcor() > 320 or blue.ycor() > 237  or blue.ycor() < -180:
       blue.right(180) 


def arena():
  for i in range(18):
    if all_t[i].xcor() < -317 or all_t[i].xcor() > 320 or all_t[i].ycor() > 237  or all_t[i].ycor() < -180:
        all_t[i].right(180) 

red_t_eaten=0
blue_t_eaten=0
green = 0.9
rscore=turtle.Turtle()
rscore.penup()
rscore.color("white")
rscore.goto(-310,227)

bscore=turtle.Turtle()
bscore.penup()
bscore.color("white")
bscore.goto(280,227)

# eating turtles
def checkBlueCollision():
  global blue_t_eaten
  global green
  for i in range(9):
   if abs(red.xcor()-bluet[i].xcor()) < 10 and abs(red.ycor()-bluet[i].ycor()) < 10:
    bluet[i].ht()
    bluet[i].goto(-1000,0)
    blue_t_eaten=blue_t_eaten+1
    green=green-0.1
    rscore.clear()
    rscore.write("Red Score: " + str(blue_t_eaten))
#redscore


def checkRedCollision():
  global red_t_eaten
  global green
  for i in range(9):
   if abs(blue.xcor()-redt[i].xcor()) < 10 and abs(blue.ycor()-redt[i].ycor()) < 10:
    redt[i].ht()
    redt[i].goto(1000,0)
    red_t_eaten=red_t_eaten+1
    green=green-0.1
    bscore.clear()
    bscore.write("Blue Score:"  +  str(red_t_eaten))
    
'''
re=0
be=0
green=0.9
rscore=turtle.Turtle()
rscore.penup()
rscore.goto(-310,227)
'''

gameclose=turtle.Turtle()
gameend=turtle.Turtle()

while True:

  background.update()
  checkBlueCollision()
  checkRedCollision()

  redb()
  blueb()

  g=g+0.07
  '''
  if checkRedCollision():
    re=re+1
    rscore.clear()
    rscore.write("score: "+ str(re))
    green=green-0.1
    
  if checkBlueCollision():  
    be=be+1
    green=green-0.1
  '''
  background.bgcolor(r,g,b)
  background.update()
  if g > 256:
    gameend.color("red")
    gameend.goto(0,0)
    gameend.write("GAME OVER", font=("Lobster", 20, "normal"))
    background.bgcolor("black")
 
    break
  blue.forward(5)
  red.forward(5)
  background.update()
  for t in redt:
    t.forward(5)
#    background.update()
   # bouncyredarena()
  for t in bluet:
    t.forward(5)
#    background.update()
  arena()
  background.update()
  if red_t_eaten==9:
    gameclose.color("pink")
    gameclose.write("BLUE WINS", font=("Lobster", 20, "normal"))
    break
  elif blue_t_eaten==9:
    gameclose.color("pink")
    gameclose.write("RED WINS", font=("Lobster", 20, "normal"))
    break
   
#  bouncypurplearena()
   # bouncybluearena()

 
 
 
 
 
 
 
 
 
 
  
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

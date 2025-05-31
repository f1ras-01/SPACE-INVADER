


import turtle
import time
import math
import random
import os
os.chdir(r'C:\Users\firas\OneDrive\Desktop\pythonprojects\SPACE INVADER\items')

delay = 0.01
#set screen
wn = turtle.Screen()
wn.title("space invader by fj")
wn.bgcolor("blue")
wn.setup(height=650,width=650)
wn.tracer(0)
wn.bgpic("bg1.gif")
#register shapes
turtle.register_shape("en1.gif")
turtle.register_shape("spi_pl1.gif")

#draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

#set score 0
score = 0
high_score = 0
#draw score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290,276) 
score_pen.write("Score : 0  High Score : 0",align="left",font=("Arial",14,"normal"))
score_pen.hideturtle()

#create player
pl = turtle.Turtle()
pl.speed(0)
pl.penup()
pl.shape("spi_pl1.gif")
pl.goto(0,-250)
pl.setheading(90)
pl.direction = "stop"
pl_speed = 6.5

#number of enemies
enemies_numbers = random.randint(9,15)
#enemy list
enemies = []
 
for i in range(enemies_numbers):
    #create the enenmy
    enemies.append(turtle.Turtle())
for enemy in enemies : 
    enemy.penup()
    enemy.speed(0)
    enemy.shapesize(38,38)
    enemy.shape("en1.gif")
    enemy.goto(random.randint(-200,200),random.randint(100,250))

enemy_speed = 1 

#create the bullet
bullet = turtle.Turtle()
bullet.speed(0)
bullet.shape("circle")
bullet.color("blue")
bullet.shapesize(0.5,0.5)
bullet.penup()
bullet.setheading(90)
x = pl.xcor()
y = pl.ycor()
bullet.goto(x,y)
bullet_speed = 15
bullet_state = "ready"

#functions
def move_left():
    pl.direction = "left"
def move_right():
    pl.direction = "right"
def move():
    if pl.direction == "right" and pl.xcor()<270:
        x = pl.xcor() 
        pl.setx(x+pl_speed)
    if pl.direction == "left" and pl.xcor()>-270:
        x = pl.xcor()
        pl.setx(x-pl_speed)

def bullet_firing():
    global bullet_state 
    if bullet_state == "ready" :
        bullet_state = "fire"

def isCollision(t1,t2) : 
    if math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2)) < 15 :
        return True
    else : 
        return False  




         
#keybinding
wn.listen()
wn.onkeypress(move_left,"Left")
wn.onkeypress(move_right,"Right")
wn.onkeypress(bullet_firing,"space")



while True : 
    wn.update()
    for enemy in enemies : 
        #move the enemy
        x = enemy.xcor()
        x += enemy_speed
        enemy.setx(x)
        #move the enemy back and down
        if enemy.xcor() > 280:
            #move down all enemies
            for e in enemies :
                y = e.ycor()
                y -=40           
                e.sety(y)
            #change all enemies direction
            enemy_speed *= -1   
        if enemy.xcor()  < -280 :
            #move down all enemies
            for e in enemies :
                y = e.ycor()
                y -=40                
                e.sety(y)
            #change all enemies direction
            enemy_speed *= -1
        # check for bullet and enemy collision
        if (isCollision(enemy,bullet) == True) and (enemy.ycor()> -240) : 
            bullet_state = "ready"
            #reset the enemy
            enemy.goto(random.randint(-200,200),random.randint(100,250))
            #update the score
            score += 10
            if score> high_score:
                high_score = score
            score_pen.clear()
            score_pen.write( "Score :{}  High Score : {}" .format(score,high_score),align="left",font=("Arial",14,"normal"))
        #check for collision between enemies
        if isCollision(enemy,enemy) == True :
                for eni in enemies :
                    eni.xcor() + 30
                    eni.ycor() + 30

        #check for player and enemy collision 
        if (isCollision(enemy,pl) == True) or (enemy.ycor()<-250):   
            time.sleep(1)
            #reset the player and the enemies to their initial positions
            pl.goto(0,-250)
            for en in enemies :
                en.goto(random.randint(-200,200),random.randint(100,250))
            #reset the score
            score = 0
            score_pen.clear()
            score_pen.write( "Score :{}  High Score : {}" .format(score,high_score),align="left",font=("Arial",14,"normal"))
    move()      
    #firing bullets
    if bullet_state == "ready":
        bullet.hideturtle()
        bullet.setx(pl.xcor())
        bullet.sety(pl.ycor())
    if bullet_state == "fire":
        bullet.showturtle()
        y = bullet.ycor()
        y += bullet_speed 
        bullet.sety(y)
    if bullet.ycor() > 280:
        bullet_state = "ready"

        
    time.sleep(delay)
wn.mainloop()

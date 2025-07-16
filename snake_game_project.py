import turtle
import time
import random
from sqlite3 import*
import sqlite3
delay=0.100
score=0
highscore=0

#snake bodies
bodies=[]

#main screen
main_Screen=turtle.Screen()
main_Screen.title('Snake Game')
main_Screen.bgcolor('aqua')
main_Screen.setup(width=700,height=700)


#ask for usernamebefire strting the game
username=input('enter your username:')

#database connection
conn=sqlite3.connect('snake_score.db')
c=conn.cursor()

#create table if not exists
c.execute("CREATE TABLE scores(username TEXT,score INTEGER)")
# c.execute("insert into scores ()")
c.execute('INSERT INTO scores VALUES(?,?)',(username,score))
conn.commit()

#close the database connection
conn.close()
    
#snake headss
head =turtle.Turtle()
head.speed(0)
head.shape('circle')
head.color('black')
head.fillcolor('blue')
head.penup()
head.goto(0,0)
head.direction='stop'


#snake food
food =turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('green')
food.fillcolor('red')
food.penup()
food.ht()
food.goto(0,100)
food.st()#show turtle


#score board
sb=turtle.Turtle()
sb.shape('circle')
sb.fillcolor('black')
sb.penup()
sb.ht()
sb.goto(0,260)
sb.write('Score=0  | Highscore=0',font=('arial',15,'bold'))
                  

#function declaration
def moveup():
    if head.direction!='down':
        head.direction='up'

def movedown():
    if head.direction!='up':
        head.direction='down'

def moveleft():
    if head.direction!='right':
        head.direction='left'

def moveright():
    if head.direction!='left':
        head.direction='right'

def movestop():
    head.direction='stop'

def move():
    if head.direction=='up':
        y=head.ycor()
        head.sety(y+20)

    if head.direction=='down':
        y=head.ycor()
        head.sety(y-20)

    if head.direction=='left':
        x=head.xcor()
        head.setx(x-20)

    if head.direction=='right':
        x=head.xcor()
        head.setx(x+20)


#Event Handling
main_Screen.listen()
main_Screen.onkey(moveup,'Up')
main_Screen.onkey(movedown,'Down')
main_Screen.onkey(moveleft,'Left')
main_Screen.onkey(moveright,'Right')
main_Screen.onkey(movestop,'space')


#main loop
while True:
    main_Screen.update()

#check collision with border
    '''if head.xcor()>280:
        head.setx(-280)
    if head.xcor()<-280:
        head.setx(280)


    if head.ycor()>280:
        head.sety(-280)
    if head.ycor()<-280:
        head.sety(280)'''
    if head.xcor()>280 or head.xcor()<-280 or head.ycor()>280 or head.ycor()<-280 :
        print("GAME OVER-Border collision")
        break
    #break
#check collision with food
    if head.distance(food)<20:
            x=random.randint(-290,290)
            y=random.randint(-290,290)
            food.goto(x,y)

#increase the length of snake
            body=turtle.Turtle()
            body.speed(0)
            body.penup()
            body.shape('circle')
            x=random.randint(-290,290)
            body.color('red')
            body.fillcolor('darkred')
            #append new body
            bodies.append(body)

            #increase the score
            score=score+1

            #change delay
            delay-=0.01

            #updatethe high score
            if score>highscore:
                highscore=score
            sb.clear()
            sb.write('Score={} |Highscore={}'.format(score,highscore),font=('arial',15,'bold'))


    #move the snake bodies
    for i in range(len(bodies)-1,0,-1):
         x=bodies[i-1].xcor()
         y=bodies[i-1].ycor()
         bodies[i].goto(x,y)


    if len(bodies)>0:
        x=head.xcor()
        y=head.ycor()
        bodies[0].goto(x,y)
    move()


    #check collision with snake body
    for body in bodies[1:]:
        if body.distance(head)<20:
            print('GAME OVER-self collision')
            break
            ''' time.sleep(1)
            head.goto(0,0)
            head.direction='stop'

            #hide bodies
            for body in bodies:
                body.ht()
            bodies.clear()


            score=0
            delay=0.1

           #update score board
            sb.clear()
            sb.write('Score={} |Highscore={}'.format(score,highscore),font=('arial',15,'bold'))'''
    time.sleep(delay)

#insert the username and score into the database
# c.execute('INSERT INTO scores VALUES(?,?)',(username,score))
# conn.commit()

# #close the database connection
# conn.close()
    
main_Screen.mainloop()
          





















                  

import turtle
import random

from numpy import square
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Bouncing Ball Simulator")
wn.setup(width=800, height=600)
wn.tracer(0)

balls =[]

#初始化
for x in range(25) :
    balls.append(turtle.Turtle())

colors = ["red","white","yellow","blue","green","orange","purple","grey"]
shapes = ["circle","square","triangle"]
for ball in balls :
    ball.shape(random.choice(shapes))
    ball.color(random.choice(colors))
    ball.penup()
    ball.speed(0)    #動畫的速度
    x = random.randint(-290,290)
    y = random.randint(-200,300)
    ball.goto(x,y)  
    ball.dy = 0     #位置變化 == 速度
    ball.dx = random.randint(-4,4)
    ball.da = 2
    gravit = 0.3

#控制球，加速減速
def messdown():
    for ball in balls:
        ball.dy -= 20

def messup():
    for ball in balls:
        ball.dy = 20

def messleft():
    for ball in balls:
        ball.dx = -20

def messright():
    for ball in balls:
        ball.dx = 20

def slowdown():
    for ball in balls:
        ball.dx *= 0.5
        ball.dy *= 0.5
        ball.da *= 0.5
def speedup():
    for ball in balls:
        ball.dx *= 1.1
        ball.dy *= 1.1
        ball.da *= 1.1

wn.listen()
wn.onkeypress(messdown,"Down")
wn.onkeypress(messup,"Up")
wn.onkeypress(messleft,"Left")
wn.onkeypress(messright,"Right")
wn.onkeypress(slowdown,"q")
wn.onkeypress(speedup,"w")
while True :
    wn.update()
   
    for ball in balls:
        ball.rt(ball.da)
        ball.dy -= gravit
        ball.sety(ball.ycor()+ball.dy)
        ball.setx(ball.xcor()+ball.dx)
        
        
        #check wall collision(inelastic)
        if ball.xcor() > 400 or ball.xcor() < -400:
            ball.dx *= -0.9
            ball.da *= -0.9

        #check for a bounce
        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -0.9
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -0.9
            # if ball.dy < 0.1 :
            #     ball.sety(-290)

        #check for collision betwween the balls
        for i in range(0,len(balls)):
            for j in range(i+1,len(balls)):  #each ball 20pixel 
                if balls[i].distance(balls[j])<25:
                    temp_dx = balls[i].dx
                    temp_dy = balls[i].dy
                    temp_rt = balls[i].rt

                    balls[i].dx = balls[j].dx
                    balls[i].dy = balls[j].dy
                    balls[i].rt = balls[j].rt

                    balls[j].dx = temp_dx
                    balls[j].dy = temp_dy
                    balls[j].rt = temp_rt
    
    # wn.onkeypress(,"d")

        
wn.mainloop()
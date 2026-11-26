import turtle;


window = turtle.Screen()
window.bgcolor("black")
window.setup(width=1000, height= 600)
window.tracer(0)




paddle1 = turtle.Turtle()
paddle1.speed(0)
paddle1.shape("square")
paddle1.color("white")
paddle1.shapesize(stretch_wid = 5, stretch_len = 1)
paddle1.penup()
paddle1.goto(-350, 0)

paddle2 = turtle.Turtle()
paddle2.speed(0)
paddle2.shape("square")
paddle2.color("white")
paddle2.shapesize(stretch_wid = 5, stretch_len = 1)
paddle2.penup()
paddle2.goto(350, 0)

line1 = turtle.Turtle()
line1.color("white")
line1.shape("square")
line1.shapesize(stretch_wid = 0.1, stretch_len = 100)
line1.penup()
line1.goto(375 , 290 )
line1.setheading(270)
line1.pendown()
line1.forward(580)
line1.hideturtle

line2 = turtle.Turtle()
line2.color("white")
line2.shape("square")
line2.shapesize(stretch_wid = 0.1, stretch_len = 100)
line2.penup()
line2.goto(-375 , 290 )
line2.setheading(270)
line2.pendown()
line2.forward(580)
line2.hideturtle

def GameUI(p1n, p2n, p1s, p2s):

    # Player 1 name
    lbl1 = turtle.Turtle()
    lbl1.speed(0)
    lbl1.color("white")
    lbl1.penup()
    lbl1.hideturtle()
    lbl1.goto(-425, 250)
    lbl1.write(p1n, align="center", font=("Arial", 16, "normal"))

    # Player 1 wins
    lbl2 = turtle.Turtle()
    lbl2.speed(0)
    lbl2.color("white")
    lbl2.penup()
    lbl2.hideturtle()
    lbl2.goto(-425, 220)
    lbl2.write("Wins: " + str(p1s), align="center", font=("Arial", 14, "normal"))

    # Player 2 name
    lbl3 = turtle.Turtle()
    lbl3.speed(0)
    lbl3.color("white")
    lbl3.penup()
    lbl3.hideturtle()
    lbl3.goto(425, 250)
    lbl3.write(p2n, align="center", font=("Arial", 16, "normal"))

    # Player 2 wins
    lbl4 = turtle.Turtle()
    lbl4.speed(0)
    lbl4.color("white")
    lbl4.penup()
    lbl4.hideturtle()
    lbl4.goto(425, 220)
    lbl4.write("Wins: " + str(p2s), align="center", font=("Arial", 14, "normal"))

def paddle1_up():
    y = paddle1.ycor()
    if y<250:
        paddle1.sety(y+20)

def paddle1_down():
    y= paddle1.ycor()
    if y>-250:
        paddle1.sety(y-20)

def paddle2_up():
    y = paddle2.ycor()
    if y<250:
        paddle2.sety(y+20)

def paddle2_down():
    y= paddle2.ycor()
    if y>-250:
        paddle2.sety(y-20)


window.listen()
window.onkeypress(paddle1_up,"w")
window.onkeypress(paddle1_down,"s")
window.onkeypress(paddle2_up,"Up")
window.onkeypress(paddle2_down,"Down")
global player_name1
global player_name2
global player1_score
global player2_score

def globals(p1n, p2n, p1s, p2s):
    player_name1=p1n
    player_name2=p2n
    player1_score=p1s
    player2_score=p2s
    
GameUI(player_name1,player_name2, player1_score, player2_score)
while True:
    window.update()



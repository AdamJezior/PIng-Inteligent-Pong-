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
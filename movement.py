def player1_up():
    y = player.ycor()
    if y<250:
        player.sety(y+20)

def player1_down():
    y= player.ycor()
    if y>-250:
        player.sety(y-20)

def player2_up():
    y = player.ycor()
    if y<250:
        player.sety(y+20)

def player2_down():
    y= player.ycor()
    if y>-250:
        player.sety(y-20)

window.listen()
window.onkeypress(move_up,"w")
window.onkeypress(move_down,"s")
window.onkeypress(move_up,"Up")
window.onkeypress(move_down,"Down")
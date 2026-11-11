class score:
    player1_score = 0
    player2_score = 0

def player1_score():
    global player1_score
    player1_score += 1

def player2_score():
    global player2_score
    player2_score += 1

player1_score()
player1_score()
player2_score()

print("player 1:", player1_score)
print("Player 2:", player2_score)
import tkinter as tk
global player_name1
global player_name2
global player1_score
global player2_score

def GameUI(p1n, p2n, p1s, p2s):
    root = tk.Tk()
    root.title("My Game")
    root.geometry("350x250")

    player_name1 = p1n
    player_name2 = p2n
    player1_score = p1s 
    player2_score = p2s

    lbl = tk.Label(root,text = player_name1)
    lbl.place(x=10, y=10)

    
    lbl = tk.Label(root,text = "Wins: ")
    lbl.place(x=10, y=35)

    lbl = tk.Label(root,text =  player1_score)
    lbl.place(x=10, y=50)
    
    lbl = tk.Label(root,text = player_name2)
    lbl.place(x=500, y=10)

    lbl = tk.Label(root,text = "Wins: ")
    lbl.place(x=500, y=35)

    lbl = tk.Label(root,text = player2_score)
    lbl.place(x=500, y=50)

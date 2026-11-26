import tkinter as tk

root = tk.Tk()

root.title("My Game")
root.geometry("350x250")



def playerstat():
    global player_name1 
    global player_name2

    global player1_score
    global player2_score

    player_name1 = "Ryan"
    player_name2 = "Adam"
    player1_score = 1
    player2_score = 0


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

playerstat()
root.mainloop()
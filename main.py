"""
This is a comment
written in
more than just one line
"""
#this is a single line comment

"""
types of variables in python
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
"""
"""     text menu
def on_click():
    lbl.config(text=f"Hello, {entry.get()}!")

root = tk.Tk()
root.title("UI title")
root.geometry('350x200')

lbl = tk.Label(root, text="Enter your name:")
lbl.pack(pady=5)

entry = tk.Entry(root)
entry.pack(pady=5)

btn = tk.Button(root, text="Greet", command=on_click)
btn.pack(pady=5)
"""
import tkinter as tk

from UI import GameUI

root = tk.Tk()

# root window title and dimension
root.title("PIng-Intelligent-Pong")

#root.geometry('1880x980')  max
root.geometry('280x180')
global player_name1
global player_name2



def Start():
   GameUI(player_name1, player_name2, 0, 0)


def settings():
    root = tk.Tk()
    root.title("Settings")
    root.geometry('350x350')
    
    def start_player_names():
        root.destroy()
        player_names()
    def start_player_colors():
        root.destroy()
        player_colors()
    def start_score_limit():
        root.destroy()
        score_limit()
    def start_ball_speed():
        root.destroy()
        ball_speed()
    def return_to_main_menu():
        root.destroy()
        main_menu()

    lbl = tk.Label(root, text = "Settings\n")
    lbl.pack(pady=5)
    btn = tk.Button(root,text = "Enter player names",fg = "black", command=start_player_names)
    btn.pack(pady=5)
    btn = tk.Button(root,text ="Enter player colors",fg = "black", command=start_player_colors)
    btn.pack(pady=5)
    btn = tk.Button(root,text ="Enter score limit",fg = "black", command=start_score_limit)
    btn.pack(pady=5)
    btn = tk.Button(root,text ="Enter game speed",fg = "black", command=start_ball_speed)
    btn.pack(pady=5)
    btn = tk.Button(root,text ="Enter match time",fg = "black", command=start_match_time)
    btn.pack(pady=5)
    btn = tk.Button(root,text ="Back to main menu",fg = "black", command=return_to_main_menu)
    btn.pack(pady=5)

# button widget with red color text
# inside
def main_menu():
    lbl = tk.Label(root,text = "Main menu\n\n")
    lbl.grid(column=0, row=0)
    btn = tk.Button(root, text = "1. Start Game" ,fg = "red", command=Start)
    btn.grid(column=0, row=1)
    btn = tk.Button(root, text = "2. Settings" ,fg = "red", command=settings)
    btn.grid(column=0, row=2)
    btn = tk.Button(root, text = "3. Exit Game" ,fg = "red", command=exit)
# set Button grid
    btn.grid(column=0, row=3)

def player_names():
    global player_name2
    global player_name1
    root = tk.Tk()
    root.title("Player names")
    root.geometry('350x250')
    lbl = tk.Label(root,text = "Enter player names:\n")
    lbl.pack(pady=5)

    lbl = tk.Label(root,text = "Player 1: \n")
    lbl.pack(pady=5)
    p1n = tk.Entry(root)
    p1n.pack(pady=5)


    lbl = tk.Label(root,text = "Player 2: \n")
    lbl.pack(pady=5)
    p2n = tk.Entry(root)
    p2n.pack(pady=5)


    def start_display_player_names():
        global player_name1
        global player_name2
        player_name1 = p1n.get()
        player_name2 = p2n.get()
        root.destroy()
        dispPlayerNames()
    btn = tk.Button(root, text="Submit", command=start_display_player_names)
    btn.pack(pady=5)

def dispPlayerNames():
    global player_name1
    global player_name2
    root = tk.Tk()
    root.title("confirmation screen")
    root.geometry('350x200')
    def start_settings():
        root.destroy()
        settings()
    def start_player_names():
        root.destroy()
        player_names()
    lbl = tk.Label(root, text = "Player 1:"+ player_name1 + ", Player 2: " + player_name2)
    lbl.pack(pady=5)
    btn = tk.Button(root, text="Confirm", command=start_settings)
    btn.pack(pady=5)
    btn = tk.Button(root, text="Cancel", command=start_player_names)
    btn.pack(pady=5)
    
def player_colors():
    global player_color1
    global player_color2
    root = tk.Tk()
    root.title("Player colors")
    root.geometry('350x250')
    lbl = tk.Label(root,text = "Enter player colors:\n")
    lbl.pack(pady=5)

    lbl = tk.Label(root,text = "Player 1: \n")
    lbl.pack(pady=5)
    p1c = tk.Entry(root)
    p1c.pack(pady=5)

    lbl = tk.Label(root,text = "Player 2: \n")
    lbl.pack(pady=5)
    p2c = tk.Entry(root)
    p2c.pack(pady=5)

    def start_display_player_colors():
        global player_color1
        global player_color2
        player_color1 = p1c.get()
        player_color2 = p2c.get()
        root.destroy()
        dispPlayerColors()
    btn = tk.Button(root, text="Submit", command=start_display_player_colors)
    btn.pack(pady=5)

def score_limit():
    root = tk.Tk()
    root.title("Score Limit")
    root.geometry('350x200')
    lbl = tk.Label(root, text="Enter score limit:")
    lbl.pack(pady=5)
    score_entry = tk.Entry(root)
    score_entry.pack(pady=5)

    def set_score_limit():
        global score_limit
        score_limit = int(score_entry.get())
        root.destroy()
        settings()
    btn = tk.Button(root, text="Submit", command=set_score_limit)
    btn.pack(pady=5)

def dispPlayerColors():
    global player_color1
    global player_color2
    root = tk.Tk()
    root.title("Player Colors")
    root.geometry('350x250')
    lbl = tk.Label(root, text="Player 1 Color: " + player_color1)
    lbl.pack(pady=5)
    lbl = tk.Label(root, text="Player 2 Color: " + player_color2)
    lbl.pack(pady=5)
    

def ball_speed():
    global speed_entry
    root = tk.Tk()
    root.title("Ball Speed")
    root.geometry('350x200')
    lbl = tk.Label(root, text="Enter ball speed:")
    lbl.pack(pady=5)
    speed_entry = tk.Entry(root)
    speed_entry.pack(pady=5)

    def set_ball_speed():
        global ball_speed
        ball_speed = int(speed_entry.get())
        root.destroy()
        settings()
    btn = tk.Button(root, text="Submit", command=set_ball_speed)
    btn.pack(pady=5)

def start_match_time():
    global match_time_entry
    root = tk.Tk()
    root.title("Match Time")
    root.geometry('350x200')
    lbl = tk.Label(root, text="Enter match time (in seconds):")
    lbl.pack(pady=5)
    match_time_entry = tk.Entry(root)
    match_time_entry.pack(pady=5)

    def set_match_time():
        global match_time
        match_time = int(match_time_entry.get())
        root.destroy()
        settings()
    btn = tk.Button(root, text="Submit", command=set_match_time)
    btn.pack(pady=5)
main_menu()
root.mainloop()

import tkinter as tk

root = tk.Tk()

# root window title and dimension
root.title("PIng-Intelligent-Pong")

#root.geometry('1880x980')  max
root.geometry('280x180')
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

def Start():
    lbl = tk.Label(root, text = "Starting game\n")
    lbl.pack(pady=5)


def settings():
    root = tk.Tk()
    root.title("UI title")
    root.geometry('350x250')
    lbl = tk.Label(root, text = "Settings\n")
    lbl.pack(pady=5)
    btn = tk.Button(root,text = "Enter player names",fg = "black", command=player_names)
    btn.pack(pady=5)

    btn = tk.Button(root,text ="Enter player colors",fg = "black", command=Start)
    btn.pack(pady=5)
    btn = tk.Button(root,text ="Enter score limit",fg = "black", command=Start)
    btn.pack(pady=5)
    btn = tk.Button(root,text ="Enter game speed",fg = "black", command=Start)
    btn.pack(pady=5)
    btn = tk.Button(root,text ="Returning to main menu...",fg = "black", command=main_menu)
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
    global player_name1
    global player_name2

    root = tk.Tk()
    root.title("Player names")
    root.geometry('350x250')
    lbl = tk.Label(root,text = "Enter player names:\n")
    lbl.pack(pady=5)

    lbl = tk.Label(root,text = "Player 1: \n")
    lbl.pack(pady=5)
    p1n = tk.Entry(root)
    p1n.pack(pady=5)
    player_name1 = p1n.get()

    lbl = tk.Label(root,text = "Player 2: \n")
    lbl.pack(pady=5)
    p2n = tk.Entry(root)
    p2n.pack(pady=5)
    player_name2 = p2n.get()

    btn = tk.Button(root, text="Submit", command=dispPlayerNames)
    btn.pack(pady=5)

def dispPlayerNames():
    root = tk.Tk()
    root.title("confirmation screen")
    root.geometry('350x200')
    lbl = tk.Label(root, text = f"Player 1: {player_name1}, Player 2: {player_name2}")
    lbl.pack(pady=5)
    btn = tk.Button(root, text="Confirm", command=settings)
    btn.pack(pady=5)
    btn = tk.Button(root, text="Cancel", command=player_names)
    btn.pack(pady=5)

main_menu()
root.mainloop()
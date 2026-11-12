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
#this is a baisic menu for the game
while True: 
    print("Main Menu\n1. Start\n2. Settings\n3. Exit")
    scan = input()
    if scan == "1":
        print("Starting the program...")


    if scan == "2":
    #this is the settings menu for the game
        while True:
            print("Settings\n1. player names\n2. player colors\n3. score limit\n4. game speed\n5. back")
            settings_scan = input()
            if settings_scan == "1":
                print("Enter player names:")
                player_name1 = input("Player 1: ")
                player_name2 = input("Player 2: ")
                print(f"Player 1: {player_name1}, Player 2: {player_name2}")
            elif settings_scan == "2":
                print("Enter player colors:")
                player_colors = input()
            elif settings_scan == "3":
                print("Enter score limit:")
                score_limit = input()
            elif settings_scan == "4":
                print("Enter game speed:")
                game_speed = input()
            elif settings_scan == "5":
                print("Returning to main menu...")
                break
            else:
                print("Invalid option. Please try again.")
    
    if scan == "3":
        print("Closing program")
        exit()

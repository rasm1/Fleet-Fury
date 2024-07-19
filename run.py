class Board:
    """
    Main class for the game board.
    """
    def __init__(self,board_size,num_of_ships,player_name,type):
        self.board_size = board_size
        self.num_of_ships = num_of_ships
        self.player_name = player_name
        self.type = type

def playGame():
    print("_"*30)
    print("Welcome to Fleet fury")
    print("A console based battleships game")
    print("press a key")
    print("_"*30)
    player_name = input("please enter your name here:")



playGame()
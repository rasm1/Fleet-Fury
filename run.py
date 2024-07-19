class Board:
    """
    Main class for the game board.
    """
    def __init__(self,board_size,num_of_ships,player_name,type):
        self.board_size = board_size
        self.num_of_ships = num_of_ships
        self.player_name = player_name
        self.type = type

    def print_board(self):
        print("_"* 6)


def get_num_of_ships():
    """
    Get number of ships to populate the board with
    """
    
    num_of_ships = input("Please enter the amount of ships you want to play with:")
    validate_num_of_ships(num_of_ships)

def validate_num_of_ships(num_of_ships):
    """
    validates if number entered is correct data type
    """
    try:
        if num_of_ships > 36:
            raise ValueError(
                print(f"{num_of_ships} is too many ships, try playing with less ships")
            )
    except ValueError as e:
        print(f"{num_of_ships} is not a number, try entering a number")


    

def playGame():
    print("_"*30)
    print("Welcome to Fleet fury")
    print("A console based battleships game")
    print("press a key")
    print("_"*30)
    player_name = input("please enter your name here:")
    

    player_board = Board(6,4,player_name,type = "player")



playGame()
get_num_of_ships()
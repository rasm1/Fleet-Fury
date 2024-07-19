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
    
    
    validate_num_of_ships()

def validate_num_of_ships():
    """
    validates if number entered is correct data type
    """
    try:
        num_of_ships = input("Please enter the amount of ships you want to play with:")
        if "." in num_of_ships:
            raise ValueError(f"{num_of_ships} is a decimal, please try again")
        num_of_ships = int(num_of_ships)
        if num_of_ships <= 0:
            raise ValueError("negative number or 0 was entered, please try a positive number")
        if num_of_ships > 36:
            raise ValueError(f"{num_of_ships} is too many ships, please try again")
    except ValueError as ve:
        print(f"invalid input: {ve}")

    

def playGame():
    print("_"*30)
    print("Welcome to Fleet fury")
    print("A console based battleships game")
    print("press a key")
    print("_"*30)
    player_name = input("please enter your name here:")
    

    player_board = Board(6,4,player_name,type = "player")


def main():
    playGame()
    get_num_of_ships()

main()
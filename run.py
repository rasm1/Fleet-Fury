from random import randint
class Grid:
    """
    Main class for the game grid.
    """
    def __init__(self,grid_size,num_of_ships,player_name,type):
        self.grid_size = [["_" for x in range(grid_size)] for y in range(grid_size)]
        self.num_of_ships = num_of_ships
        self.player_name = player_name
        self.type = type



def get_num_of_ships():
    """
    Get number of ships to populate the grid with
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
        print_grid()
    except ValueError as ve:
        print(f"invalid input: {ve}")

def print_grid():
    """
    prints the play grid
    """
    print(f"{player_name}'s grid:")
    print("  0  "," 1 ","  2  "," 3  "," 4  "," 5  ")
    for _ in range(6):
        print(_, "  _  "*6)

def populate_grid():
    """
    places ships on the grid
    """




def RunGame():
    print("_"*30)
    print("Welcome to Fleet fury")
    print("A console based battleships game")
    print("_"*30)
    global player_name
    player_name = input("please enter your name here:")
    

    player_grid = Grid(6,4,player_name,type = "player")


def main():
    RunGame()
    get_num_of_ships()
main()
from random import randint

GRID_SIZE = 6
hit = [6,2,5]
miss = [21,35,2]
guesses = hit + miss


def create_grid(size):
    return [[EMPTY] * size for _ in range(size)]

def print_grid(): #dr codie youtube
    """
    prints the play grid
    """
    print(f"{player_name}'s grid:")
    print("    0 ","  1 ","  2  "," 3  "," 4  "," 5  ")

    location = 0
    for x in range(6):
        row = ""
        for y in range(6):
            ch = " _ "
            if location in miss:
                ch = " / "
            elif location in hit:
                ch = " X "
            
            row = row + ch
            location = location + 1
        print(x, " ",row)


def get_shot(): 
    valid_shot = "n"
    while valid_shot == "n":
        try:
            shot = input("please choose a location:")
            shot = int(shot)
            if shot < 0 or shot > 36:
                print("incorrect shot, please try again")
            elif shot in guesses:
                print("You have already shot at that location")
            else:
                valid_shot = "y"
                break
        except:
            print("invalid guess ,please try again")
    return shot

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
    finally:
        return num_of_ships
        print(num_of_ships)



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


def main():
    RunGame()
    get_num_of_ships()
    populate_grid()
    get_shot()

main()


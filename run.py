from random import randint

# constant
GRID_SIZE = 6
# Global variables for player and computer
hit = []
miss = []
ships = []
guesses = []

computer_hit = []
computer_miss = []
computer_ships = []
computer_guesses = computer_hit + computer_miss

# legends:
# x = HIT
# / = MISS
# _ = EMPTY

def print_computer_grid(): 
    """
    Prints the play grid for the computer and logic for ships display
    """
    print("computer's grid:")
    print("     0 ","1 ","2 ","3 ","4"," 5  ")

    location = 0
    for x in range(GRID_SIZE):
        row = ""
        for y in range(GRID_SIZE):
            ch = " _ "
            if location in miss:
                ch = " / "
            elif location in hit:
                ch = " X "              
            row += ch
            location = location + 1
        print(location -6,"-",location-1," ", row,)
    print("\n")

def print_grid(player_name): 
    """
    Prints the play grid for the player
    """
    print(f"{player_name}'s grid:")
    print("     0 ","1 ","2 ","3 ","4"," 5  ")

    location = 0
    for x in range(GRID_SIZE):
        row = ""
        for y in range(GRID_SIZE):
            ch = " _ "
            if location in computer_miss:
                ch = " / "
            elif location in computer_hit:
                ch = " X "
            elif location in ships:
                ch = " @ "
            row += ch
            location += 1
        print(location -6,"-",location-1," ", row)
        


def get_shot(): 
    """
    gets and validates the shot
    """
    valid_shot = False
    while not valid_shot:
        try:
            shot = input("Please choose a location between 0 and 35:\n")
            shot = int(shot)
            if shot < 0 or shot >= GRID_SIZE * GRID_SIZE:
                print("Incorrect shot, please try again.")
            elif shot in guesses:
                print("You have already shot at that location.")
            else:
                valid_shot = True
                break
        except ValueError:
            print("Invalid guess, please try again.")
    return shot

def get_computer_shot():
    """
    generates computer shot randomly
    """
    computer_shot = randint(0,35)
    return computer_shot
    

def check_shot(shot,computer_shot,num_of_ships): 
    """
    checks to see if shots are hit/miss and
    checks to see if all ships were sunk, if so ends the game
    """

    guesses.append(shot)
    if shot in computer_ships:
        hit.append(shot)
        computer_ships.remove(shot)
        print("Hit!")
        
    else:
        miss.append(shot)
        print("Miss!")
    
    
    if computer_shot in ships:
        computer_hit.append(computer_shot)
        ships.remove(computer_shot)
        print("Computer Hit!")
        
    else:
        computer_miss.append(computer_shot)
        print("Computer Miss!")

    if len(computer_ships) == 0:
        print("YOU WIN")
        return True
    elif len(ships) == 0:
        print("YOU LOSE")
        return True
    return False
    
def get_num_of_ships():
    """
    Get number of ships and validates input
    """  
    while True:
        try:
            num_of_ships = input("Please enter the amount of ships you want to play with (0 - 36): \n")
            if num_of_ships == "":
                raise ValueError("Please choose an amount of ships higher than 0.\n")
            if "." in num_of_ships:
                raise ValueError(f"{num_of_ships} is a decimal, please try again.\n")
            num_of_ships = int(num_of_ships)
            if num_of_ships <= 0:
                raise ValueError("Negative number or 0 was entered, please try again.\n")
            if num_of_ships > 36:
                raise ValueError(f"{num_of_ships} is too many ships, please try again.\n")
            return num_of_ships
        except ValueError as ve:
            print(f"Invalid input: {ve}\n")

    


def populate_grid(num_of_ships):
    """
    populates the player grid by randomly placing ships, also checks for duplicate placements
    """

    while len(ships) < num_of_ships:
        ship_location = randint(0, 35)
        if ship_location not in ships:
            ships.append(ship_location)

def populate_computer_grid(num_of_ships):
    """
    populates the player grid by randomly placing ships, also checks for duplicate placements
    """
    while len(computer_ships) < num_of_ships:
        ship_location = randint(0, 35)
        if ship_location not in computer_ships:
            computer_ships.append(ship_location)


def RunGame():
    """
    prints welcome message and starts game by asking the player's name
    """
    print("_"*30)
    print("Welcome to Fleet fury")
    print("A console based battleships game")
    print("_"*30)
    player_name = input("please enter your name here: \n") 
    if player_name == "":
        player_name = "commander no-name"
    return player_name


def main():
    """
    main() function, contains game loop and game loop break
    """
    player_name = RunGame()
    num_of_ships = get_num_of_ships() 
    populate_grid(num_of_ships)   
    populate_computer_grid(num_of_ships)  
    while True:
        print_computer_grid()
        print_grid(player_name)
        shot = get_shot()
        computer_shot = get_computer_shot()
        game_over = check_shot(shot,computer_shot,num_of_ships)
        if game_over:
            break
        

main()
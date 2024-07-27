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

# legend:
# @ = ship
# x = HIT
# / = MISS
# _ = EMPTY


def print_grid(player_name):
    """
    Prints the play grid for the player
    """
    print(f"{player_name}'s grid: \n")
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
        location_string = str((location - 6)) + "-" + str((location - 1))
        # max length of 7 characters
        length_difference = 7 - len(location_string)
        if (length_difference > 0):
            for x in range(length_difference):
                location_string = location_string + (" ")
        print(location_string, row,)
    print("\n")


def print_computer_grid():
    """
    Prints the play grid for the computer and logic for ships display
    """
    print("computer's grid: \n")
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
            location += 1
        location_string = str((location - 6)) + "-" + str((location - 1))
        # max length of 7 characters
        length_difference = 7 - len(location_string)
        if (length_difference > 0):
            for x in range(length_difference):
                location_string = location_string + (" ")
        print(location_string, row,)


def get_shot():
    """
    gets and validates the shot for the player
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
    generates computer shot randomly and checks for duplicates
    """
    computer_shot = randint(0, 35)
    if computer_shot not in computer_guesses:
        return computer_shot


def check_shot(shot, computer_shot, num_of_ships):
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
        play_again()

        return True
    elif len(ships) == 0:
        print("YOU LOSE")
        play_again()
        return True
    return False


def get_num_of_ships():
    """
    Gets number of ships and validates input
    """
    while True:
        try:
            num_of_ships = input("Please enter desired amount of ships: \n")
            if num_of_ships == "":
                raise ValueError("You must have at least 1 ship\n")
            if "." in num_of_ships:
                raise ValueError(f"{num_of_ships} Must be a whole number\n")
            num_of_ships = int(num_of_ships)
            if num_of_ships <= 0:
                raise ValueError("Must be a positive number \n")
            if num_of_ships > 10:
                raise ValueError(f"{num_of_ships} is too many ships\n")
            return num_of_ships
        except ValueError as ve:
            print(f"Invalid input: {ve}\n")


def populate_grid(num_of_ships):
    """
    populates the player grid by randomly placing ships
    also checks for duplicate placements
    """

    while len(ships) < num_of_ships:
        ship_location = randint(0, 35)
        if ship_location not in ships:
            ships.append(ship_location)


def populate_computer_grid(num_of_ships):
    """
    populates the computer grid by randomly placing ships
    also checks for duplicate placements
    """
    while len(computer_ships) < num_of_ships:
        ship_location = randint(0, 35)
        if ship_location not in computer_ships:
            computer_ships.append(ship_location)


def validate_menu_choice():
    """
    validates player menu choice
    """
    print("Menu :")
    print("press 1 if you would like to see the rules")
    print("press 2 if you would like to play the game")
    print("press 3 if you would like to quit the game")
    print("_"*50)
    while True:
        try:
            menu_choice = input("Please enter your choice: ")
            menu_choice = int(menu_choice)
            if menu_choice <= 0 or menu_choice > 3:
                raise ValueError("Please choose an option between 1 and 3")
        except ValueError as ve:
            print(f"Invalid input: {ve}\n")
        else:
            return menu_choice


def show_menu(menu_choice):
    """
    logic for the menu
    """
    if menu_choice == 1:
        show_rules()
    if menu_choice == 2:
        pass
    if menu_choice == 3:
        quit()


def show_rules():
    """
    prints out the rules of the game
    """
    print("_"*50)
    print("The rules are as follows: ")
    print("- You will be facing off against the computer in a of battleships")
    print("- both players be presented with a grid")
    print("- your fleet of warships will be marked with an @")
    print("- The goal of the game is to sink the other player's fleet")
    print("- This can be done by shooting at the other players grid")
    print("- To shoot, the player must enter a number from 0 to 35")
    print("- if you hit the opponant's ship it will be market with an X")
    print("- if you miss, it will be marked with an /")
    print("- Both players alternate turns calling shots")
    print("- The game is won when a player sinks the opponent's entire fleet")
    print("_"*50)


def play_again():
    print("Would you like to play again?")
    next_game = input("if so press y, if not press any key: ")
    if next_game.lower() == "y":
        reset_game_state()
        main()
    else:
        quit()


def reset_game_state():
    """
    Resets the game state to initial conditions
    """
    global hit, miss, ships, guesses, computer_hit
    global computer_miss, computer_ships
    hit = []
    miss = []
    ships = []
    guesses = []
    computer_hit = []
    computer_miss = []
    computer_ships = []


def RunGame():
    """
    starts game by asking the player's name
    also validates playername
    """
    while True:
        player_name = input("please enter your name here: \n")
        try:
            if player_name.isalpha() is False:
                raise ValueError("name can only contain letters\n")
            if len(player_name) < 3:
                raise ValueError("name is too short\n")
            if len(player_name) > 15:
                raise ValueError("name is too long\n")
        except ValueError as ve:
            print(f"Invalid input: {ve}\n")
        else:
            return player_name


def main():
    """
    main() function, contains game loop and game loop break
    also prints welcome message
    """
    print("_"*30)
    print("Welcome to Fleet fury")
    print("A console based battleships game")
    print("_"*30)

    menu_choice = validate_menu_choice()
    show_menu(menu_choice)
    player_name = RunGame()
    num_of_ships = get_num_of_ships()
    populate_grid(num_of_ships)
    populate_computer_grid(num_of_ships)
    while True:
        print_grid(player_name)
        print_computer_grid()
        shot = get_shot()
        computer_shot = get_computer_shot()
        game_over = check_shot(shot, computer_shot, num_of_ships)
        if game_over:
            break


main()

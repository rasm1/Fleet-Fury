from random import randint

GRID_SIZE = 6
hit = []
miss = []
ships = []
guesses = hit + miss


def print_grid(player_name): 
    """
    Prints the play grid
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
            elif location in ships:
                ch = " @ "
                if player_name == "computer":
                    ch = " _ "
            
            row += ch
            location = location + 1
        print(x, " ", row)


def get_shot(): 
    valid_shot = False
    while not valid_shot:
        try:
            shot = input("Please choose a location between 0 and 35:")
            shot = int(shot)
            if shot < 0 or shot >= GRID_SIZE * GRID_SIZE:
                print("Incorrect shot, please try again.")
            elif shot in guesses:
                print("You have already shot at that location.")
            else:
                valid_shot = True
                break
        except ValueError:
            print("Invalid guess ,please try again.")
    return shot

def validate_shot(shot):
   
    if shot in ships:
        hit.append(shot)
        ships.remove(shot)
        print("Hit!")
    else:
        miss.append(shot)
        print("Miss!")

def get_num_of_ships():
    """
    Get number of ships and validates input
    """  
    while True:
        try:
            num_of_ships = input("Please enter the amount of ships you want to play with (1 - 36): ")
            if "." in num_of_ships:
                raise ValueError(f"{num_of_ships} is a decimal, please try again.\n")
            num_of_ships = int(num_of_ships)
            if num_of_ships <= 0:
                raise ValueError("Negative number or 0 was entered, please try again.\n")
            if num_of_ships > 36:
                raise ValueError(f"{num_of_ships} is too many ships, please try again.\n")
            return num_of_ships
        except ValueError as ve:
            print(f"Invalid input: {ve}")


        

def populate_grid(num_of_ships):
    for ship in range(num_of_ships):
       ship_location = randint(0,35)
       ships.append(ship_location)
    print(ships)

        


def RunGame():
   
    player_name = input("please enter your name here:") # split up in diffrent function
    return player_name


def main():
    player_name = RunGame()
    num_of_ships = get_num_of_ships() 
    populate_grid(num_of_ships)     
    while True:
        print_grid("computer")
        print_grid(player_name)
        shot = get_shot()
        valid_shot = validate_shot(shot)
        
   

print("_"*30)
print("Welcome to Fleet fury")
print("A console based battleships game")
print("_"*30)

main()
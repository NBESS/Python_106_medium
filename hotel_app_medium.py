# First, create a list of hotel dictionaries. 
# They should contain at least 3 identical dictionaries (like the one in the example above).

# Create a "while True" loop to show the following menu:
# 1. Print hotel room status
# 2. Check in customer
# 3. Check out customer
# 4. Quit


# - When printing, show all rooms for all hotels and the name of the occupant, if there is one.
# - When checking a customer in, make sure to choose a hotel as well as a room.
# - Do not let a customer check into an occupied room.
# - If the room is unoccupied, prompt for each piece of information (name, cell, etc.)
# - upon check out, print out whether or not the customer has paid

hotel1 = {
    '101': {},
    '102': {},
    '103': {
        'guest': {
            'name': 'Bugs Bunny',
            'phone': '2221234',
        }
    },
    '104': {
        'guest': {
            'name': 'Tweety Bird',
            'phone': '2221255',
        }
    },
    '105': {},
}

hotel2 = {
    '101': {
        'guest': {
            'name': 'Joe Montana',
            'phone': '5551616',
        }
    },
    '102': {},
    '103': {},
    '104': {},
    '105': {
        'guest': {
            'name': 'Barry Sanders',
            'phone': '5552020',
        }
    },
}

hotel3 = {
    '101': {},
    '102': {
        'guest': {
            'name': 'Claire Huckstable',
            'phone': '4441234',
        }
    },
    '103': {},
    '104': {},
    '105': {},
}

hotel = [hotel1, hotel2, hotel3]

main_menu = '''

1. Print hotel room status
2. Check in customer
3. Check out customer
4. Quit

'''

# Creates a function that checks if a room is vacant
def is_vacant(which_hotel, room_number):
    if which_hotel[room_number] != {}:
        return f'Room {room_number} is vacant.' 

    else:
        return f'Room {room_number} is occupied'

# Defines a function that adds a guest to a specific room
def check_in(which_hotel, room_number, guest_dictionary):
    which_hotel[room_number]['guest'] = guest_dictionary

# Defines a function that returns the guest dictionary for room number
def check_out(which_hotel, room_number):
    return f'{which_hotel[room_number]["guest"]}'

while True:

    while True:
        # Prints the hotel menu
        print(main_menu)

        # Prompt for a menu option
        if int(input('Choose a menu option: ')) == 1:

            # Print vacancies for all hotels or the names of occupants
            print('1')
        
        elif int(input('Choose a menu option: ')) == 2:
            
            # Check a customer into a hotel and room
            # Do not allow user to check into an occupied room

            # Prompt for each piece of information
            print('2')

        elif int(input('Choose a menu option: ')) == 3:

            # Check custom out
            # Print whether or not the customer has paid
            print('3')

        else:

            # Quit app
            break

print('Thank you, for using the hotel app!')    

    



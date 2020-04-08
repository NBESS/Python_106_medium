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

hotels = [hotel1, hotel2, hotel3]

main_menu = '''

1. Print hotel room status
2. Check in customer
3. Check out customer
4. Quit

'''

for key in range(len(hotels)):
    
    if 'guest' in hotels[key] == True:
        print('there is a guest') 

    print(hotels[key])
#

# # Creates a function that checks if a room is vacant
# def is_vacant(which_hotel, room_number):
#     if which_hotel[room_number] != {}:
#         return f'Room {room_number} is vacant.' 

#     else:
#         return f'Room {room_number} is occupied'

# # Defines a function that adds a guest to a specific room
# def check_in(which_hotel, room_number, guest_dictionary):
#     which_hotel[room_number]['guest'] = guest_dictionary

# # Defines a function that returns the guest dictionary for room number
# def check_out(which_hotel, room_number):
#     return f'{which_hotel[room_number]["guest"]}'

while True:
    # Prompt for a menu option
    menu_choice = int(input(main_menu))
    if menu_choice == 1:

        # Print vacancies for all hotels or the names of occupants
        for key in range(len(hotels)):
    
            print(hotels[key])

    elif menu_choice == 2:
    
        # Check a customer into a hotel and room
        # Do not allow user to check into an occupied room

        # Prompt for each piece of information
        print('2')

    elif menu_choice == 3:

        # Check custom out
        # Print whether or not the customer has paid
        print('3')

        
    elif menu_choice == 4:

        # Quit app
        break

print('Thank you, for using the hotel app!')    

    



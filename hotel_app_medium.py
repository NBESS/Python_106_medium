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
    'hotel name': 'Hotel1',
    '101': {},
    '102': {},
    '103': {},
    '104': {},
    '105': {},
}

hotel2 = {
    'hotel name': 'Hotel2',
    '101': {},
    '102': {},
    '103': {},
    '104': {},
    '105': {},
}

hotel3 = {
    'hotel name': 'Hotel3',
    '101': {},
    '102': {},
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

# Creates a function that checks if a room is vacant
def is_vacant(which_hotel, room_number):
    if which_hotel[room_number] == {}:
        return True

    else:
        return False

# Defines a function that adds a guest to a specific room
def check_in(which_hotel, room_number, guest_dictionary):

    # If room is occupied prompt to choose another room
    if is_vacant(which_hotel, room_number):
        
        which_hotel[room_number]['guest'] = guest_dictionary
        return which_hotel[room_number]['guest']

    else:

        return f'{room_number} is occupied. Please choose a different room.'
        

# # Defines a function that returns the guest dictionary for room number
def check_out(which_hotel, room_number):
    return f'{which_hotel[room_number]["guest"]}'

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
        # Provide details for customer in a dictionary
        hotel_to_check_in = input('Which Hotel would you like to check guest into? ').lower()
        room_to_check_in =  input('Which room will the guest be staying in? ')

        # Converts the string inputs for "hotel to check-in" into variables
        if hotel_to_check_in == 'hotel1':
            hotel_to_check_in = hotel1
        
        elif hotel_to_check_in == 'hotel2':
            hotel_to_check_in = hotel2

        elif hotel_to_check_in == 'hotel3':
            hotel_to_check_in = hotel3

        guest = {

            'name': input("What is the guest's name? "),
            'phone': input("What is the guest's phone number? ")
        }

        while is_vacant(hotel_to_check_in, room_to_check_in):
            print(is_vacant(hotel_to_check_in, room_to_check_in))
            room_to_check_in = input('Which room will the guest be staying in? ')
            

        print(check_in(hotel_to_check_in, room_to_check_in, guest))

    elif menu_choice == 3:

        # Check custom out
        # Print whether or not the customer has paid
        print('3')

        
    elif menu_choice == 4:

        # Quit app
        break

print('Thank you, for using the hotel app!')    

    



# import sys
# import time
# def slowprint(s):
#     for c in s + '\n':
#         sys.stdout.write(c)
#         sys.stdout.flush()
#         time.sleep(1./10)

# Locations that the user can/will encounter on their journey depending on their choices

# Location 
# starting_bedroom = Location("")
# front_yard_outside_house = Location("")
# library = Location("")
# gym = Location("")
# shady_woods = Location("")
# rec_center = Location("")
#  = Location("")
# = Location("")

# class location:
#     def __init__(self, name, description):
#         self.name = name
#         self.description = description 
#     def __str__(self):
#         return "You chose to walk towards "




# def choose_location(room):
#     if starting_bedroom ==:
#         return 
#     if front_yard_outside_house ==:
#         return
#     if library ==:
#         return
#     if gym ==:
#         return

# # Loop to allow location input
# def choose_location(user):
#     while True:
#         choose_location = input(""" 
# #                                     1. The Front Yard
# #                                     2. The Library
# #                                     3. The Gym
# #                                     4. The Shady Looking Woods
# #                                     5. The Recreation Center
# #                                 """)
#         print():
#             if choose_location == "1":
#                 front_yard_outside_house()
#                 front_yard_outside_house_menu(user)
#             elif choose_location == "2":
#                 library()
#                 library_menu(user)
#             elif choose_location == "3":
#                 gym()
#                 gym_menu(user)
#             elif choose_location == "4":
#                 shady_woods()
#                 shady_woods_menu(user)
#             elif choose_location == "5":
#                 rec_center()
#                 rec_center_menu(user)

def living_room():
    # interaction throughout one of the starting areas
    print("\nYou run into the livingroom, feeling a slight sense of relief. You dont know what was in the bathroom but you weren't going to stick around and find out.")
    print(" ")




def game_over():
    # printing the game over reason in a new line (\n)
    print("clearly you cant spell and could not type either Y or N so You decide to toss your phone down and go back to bed. You cannot be bothered today with some random Karen hitting you up complaining about something.")



# Starting location 
def starting_room():
    # location/room prompts
    # '\n' prints the line in a new line everytime
    print("\nYou slowly open your eyes, head beating hard from shredding the keyboard up last night.")
    print("You slowly get up and realize you have a message on your phone from an unknown contact. Who could it be?")
    print("Do you check the message or ignore the unknown contact? (Y or N)")

    # Converting the player's input() to upper_case
    answer = input(">").upper()

    if "Y" in answer:
        # if player typed "yes" or "Y", have the player check the phone
        print("Hello, you uneducated swine. You have mispelled one too many words. You will soon realize how important spelling is MWWWAAAAAHHHHAAAAA.")
        print("You begin to worry who texted you this odd message. Why would they send this to you? As you wonder you begin to feel an odd presence in the room with you....")
        print("You notice something strange coming from the bathroom. Will you go and check it out? (Y or N)")
        if "Y" in answer:
            print("You slowly begin to walk over to the bathroom door.")
        
        if "N" in answer: 
            print("You panic and decide to leave your room hastefully.")
            living_room()

    elif "N" in answer:
        #  if player typed "no" or "N", the player will be prompted with an even ruder message from the spelling nemesis attacking him for his lack of respect for grammer
        print("You fool.... How dare you ignore my message. I will now show you the severity of your action.")
    
    else:
        # if the player decides to input anything other than that, secret ending..... You just go to lunch and ignore the "Karen" messaging you
        game_over()
        exit() 

# Starting the game up
starting_room()


# class Location:
#     def __init__(self, name, description, connections):
#         self.name = name
#         self.description = description
#         self.connections = connections
# # Inside of the Bedroom
#     def dialogue(self, player):
#         while True:
#             if player.location == 'bedroom':
#                 while True:
#                     # You are in the BEDROOM
#                     print(self.description)
#                     print('What would you like to do?')
#                     print('\n1. Take a Nap')
#                     print('2. Check the Trashbin')
#                     print("3. Go to the Bathroom")
#                     print("4. Go to the Lobby")
#                     print("5. Quit.\n")
#                     user_input = int(input('> '))
#                     if user_input == 1:
#                         player.restore()
#                     elif user_input == 2:
#                         player.trash()
#                     elif user_input == 3:
#                         player.location = 'bathroom'
#                         break
#                     else:
#                         print('Please enter a valid option.')
#             # You are in the Bathroom
#             if player.location == 'bathroom':
#                 while True:
#                         print('\nYou are in the BATHROOM.')
#                         print('What would you like to do?')

#                         print('\n1. Check the Mirror')
#                         print('2. Go back to the Bedroom')
#                         user_input = int(input('> '))
#                         # Check the Mirror
#                         if user_input == 1:
#                                 player.mirror()
#                         # Go back to the Bedroom
#                         elif user_input == 2:
#                                 player.location = 'bedroom'
#                                 break
#                         else:
#                             print('Please enter a valid option.')
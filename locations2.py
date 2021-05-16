
# def living_room():
#     # interaction throughout one of the starting areas
#     print("You run into the livingroom, feeling a slight sense of relief. You dont know what was in the bathroom but you weren't going to stick around and find out.")
#     print("")




# def game_over():
#     # printing the game over reason in a new line (\n)
#     print("clearly you cant spell and could not type either Y or N so You decide to toss your phone down and go back to bed. You cannot be bothered today with some random Karen hitting you up complaining about something.")



# # Starting location 
# def starting_room():
#     # location/room prompts
#     # '\n' prints the line in a new line everytime
#     print("\nYou slowly open your eyes, head beating hard from shredding the keyboard up last night.")
#     print("You slowly get up and realize you have a message on your phone from an unknown contact. Who could it be?")
#     print("Do you check the message or ignore the unknown contact? (Y or N)")

#     # Converting the player's input() to upper_case
#     answer = input(">").upper()

#     if "Y" in answer:
#         # if player typed "yes" or "Y", have the player check the phone
#         print("Hello, you uneducated swine. You have mispelled one too many words. You will soon realize how important spelling is MWWWAAAAAHHHHAAAAA.")
#         print("You begin to worry who texted you this odd message. Why would they send this to you? As you wonder you begin to feel an odd presence in the room with you....")
#         print("You notice something strange coming from the bathroom. Will you go and check it out? (Y or N)")
#         if "Y" in answer:
#             print("You slowly begin to walk over to the bathroom door.")
        
#         if "N" in answer: 
#             print("You panic and decide to leave your room hastefully.")
#             living_room()

#     elif "N" in answer:
#         #  if player typed "no" or "N", the player will be prompted with an even ruder message from the spelling nemesis attacking him for his lack of respect for grammer
#         print("You fool.... How dare you ignore my message. I will now show you the severity of your action.")
    
#     else:
#         # if the player decides to input anything other than that, secret ending..... You just go to lunch and ignore the "Karen" messaging you
#         game_over()
#         exit() 

# # Starting the game up
# starting_room()





# class Game:
#     def __init__(self):
#         pass

#     # The Nemesis Chance to Challenge the Player
#     def encounter(self, chance, player, nemesis):
#         dice = random.randint(chance, 100)
#         if dice == 100:
#             while True:
#                 print('Oh no! It\'s the Spelling Nemesis!')
#                 print('\nYou have ' + str(player.health) + ' hp!')
#                 print('The Spelling Nemesis has ' + str(nemesis.health) + ' hp.\n')
#                 print()
#                 print("What do you want to do?")

#                 # Attack Option
#                 if 'a' in player.inventory:
#                     print ('1. Attack!')
#                 else: print ('1. ttck!')
#                 # Defend Option
#                 if 'd' in player.inventory:
#                     print("2. Defend!")
#                 else:
#                     print('2. efen!')
#                 # Run Away!
#                 print("3. run")

#                 print("> ",)
#                 user_input = int(input())
#                 if user_input == 1:
#                     player.attack(nemesis)
#                     nemesis.attacksChance(player)
#                 if nemesis.health <= 0:
#                     print("Impossible!") #Literally Impossible
#                 elif user_input == 2:
#                     player.defend(nemesis)
#                 elif user_input == 3:
#                     print("You run away from the Nemesis.")
#                     break
#         else: 
#             pass
    
    # The Final Encounter with the Nemesis
    # def final_encounter(self, chance, player, nemesis):
    #     while True:
            # You are in the BEDROOM
            # if player.location == '':
            #     while True:
            #         print('\nYou are in the BEDROOM.')
            #         print('What would you like to do?')
            #         print('\n1. Take a Nap')
            #         print('2. Check the Trashbin')
            #         print("3. Go to the Bathroom")
            #         print("4. Go to the Lobby")
            #         print("5. Quit.\n")
            #         user_input = int(input('> '))
            #         if user_input == 1:
            #             player.restore()
            #         elif user_input == 2:
            #             player.trash()
            #         elif user_input == 3:
            #             player.location = 'bathroom'
            #             break
            #         else:
            #             print('Please enter a valid option.')

    # The Game Itself
    def dialogue(self, player, nemesis):
        while True:
            # You are in the BEDROOM
            if player.location == 'bedroom':
                while True:
                    print('\nYou are in the BEDROOM.')
                    print('What would you like to do?')
                    print('\n1. Take a Nap')
                    print('2. Check the Trashbin')
                    print("3. Go to the Bathroom")
                    print("4. Go to the lobby")
                    print("5. Quit.\n")
                    user_input = int(input('> '))
                    if user_input == 1:
                        player.restore()
                        print("You lay down in bed and when you wake, you feel less hungover and refreshed.")
                    elif user_input == 2:
                        player.trash()
                        print("You check the trash, but nothing seems to be in it.... maybe check back later.")
                    elif user_input == 3:
                        player.location = 'bathroom'
                    elif user_input == 4:
                        player.location = 'lobby'
                        break
                    else:
                        print('Please enter a valid option.')


            # You are in the Bathroom
            if player.location == 'bathroom':
                while True:
                        print('\nYou are in the BATHROOM.')
                        self.encounter(100, player, nemesis)
                        print('What would you like to do?')
                        print('\n1. Check the Mirror')
                        print('2. Go back to the Bedroom')
                        user_input = int(input('> '))
                        # Check the Mirror
                        if user_input == 1:
                                player.mirror()
                                print("You look at the sweat dripping from your forehead. Was that thing real?")
                                print("You try and convince yourself it was not and you decide to continue on with your day.")
                        # Go back to the Bedroom
                        elif user_input == 2:
                                player.location = 'bedroom'
                                print("You decide to head back into the bedroom.")
                                break
                        else:
                            print('Please enter a valid option.')


            if player.location == 'lobby':
                while True:
                    print('\nYou are in the lobby.')
                    print("What would you like to do?")
                    print('\n1. Interact with shading guy leaning against wall')
                    print('2. Go outside')
                    print("3. Return to your bedroom")
                    user_input = int(input('> '))
                    if user_input == 1:
                        print("You cautiously walk towards the shady guy")
                        self.samconverse1()
                    elif user_input == 2:
                        player.location = 'outside'
                    elif user_input == 3:
                        player.location = 'bedroom'
                        break
                    else:
                        print('Please enter a valid option.')


            if player.location == 'outside':
                while True:
                    print('\nYou are outside.')
                    print('What would you like to do?')
                    print('\n1. Look around and enjoy the view')
                    print('2. Get a Pump at the Gym')
                    print("3. Interact with a wise-looking man")
                    print("4. Head to the Library")
                    user_input = int(input('> '))
                    if user_input == 1:
                        print("Something seems off as you scan the area. Letters seem to be missing from signs and words. I wonder if i am the only one seeing this...")
                    elif user_input == 2:
                        player.location = 'gym'
                    elif user_input == 3:
                        print("You walk up to the man, wondering what he might have to say")
                        self.seanconverse1()
                    elif user_input == 4:
                        player.location = 'library'
                        break
                    else:
                        print('Please enter a valid option.')

            if player.location == 'library':
                while True:
                    print('\nYou are in the LIBRARY.')
                    print('What would you like to do?')
                    print('\n1. Read a book')
                    print('2. Talk to the man starring at you behind a stack of books')
                    print("3. Return outside")
                    user_input = int(input('> '))
                    if user_input == 1:
                        print("")
                    elif user_input == 2:
                        print("The man jumps up from behind the books as you approach")
                        self.zachconverse1()
                    elif user_input == 3:
                        player.location = 'outside'
                        break
                    else:
                        print('Please enter a valid option.')
            if player.location == 'gym':
                while True:
                    print('\nYou are in the GYM.')
                    print('What would you like to do?')
                    print('\n1. Read the sign posted on the door')
                    print('2. Head back')
                    user_input = int(input('> '))
                    if user_input == 1:
                        print("Due to COVIB restrictions, the gym is closeb until further notice.")
                        print("You notice that the sign seemed to be off but you cannot put your finger on it. Do you want to read it again?")
                        if user_input ==1:
                            print("You notice that B\'s appear to be in the wrong place")
                            print("Your memories slowly start to come back once again...")
                            player.inventory.append('d')
                            print("You obtained the letter \'a\'!')
                        elif user_input == 2:
                            player.location() = 'outside'
                            break
                    else:
                        print('Please enter a valid option.')


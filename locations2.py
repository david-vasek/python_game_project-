# # # Global-Scope
# # import random

# # class Location:
# #     def __init__(self, name, description, connections):
# #         self.name = name
# #         self.description = description
# #         self.connections = connections
# # # Inside of the Bedroom
# #     def dialogue(self, player):
# #         while True:
# #             if player.location == 'bedroom':
# #                 while True:
# #                     # You are in the BEDROOM
# #                     print(self.description)
# #                     print('What would you like to do?')
# #                     print('\n1. Take a Nap')
# #                     print('2. Check the Trashbin')
# #                     print("3. Go to the Bathroom")
# #                     print("4. Go to the Lobby")
# #                     print("5. Quit.\n")
# #                     user_input = int(input('> '))
# #                     if user_input == 1:
# #                         player.restore()
# #                     elif user_input == 2:
# #                         player.trash()
# #                     elif user_input == 3:
# #                         player.location = 'bathroom'
# #                         break
# #                     else:
# #                         print('Please enter a valid option.')
# #             # You are in the Bathroom
# #             if player.location == 'bathroom':
# #                 while True:
# #                         print('\nYou are in the BATHROOM.')
# #                         print('What would you like to do?')

# #                         print('\n1. Check the Mirror')
# #                         print('2. Go back to the Bedroom')
# #                         user_input = int(input('> '))
# #                         # Check the Mirror
# #                         if user_input == 1:
# #                                 player.mirror()
# #                         # Go back to the Bedroom
# #                         elif user_input == 2:
# #                                 player.location = 'bedroom'
# #                                 break
# #                         else:
# #                             print('Please enter a valid option.')

# # class Character:
# #     def __init__(self, name, health, power):
# #         self.name = name
# #         self.health = health
# #         self.power = power


# # class Player(Character):
# #     def __init__(self, name, health, power, location):
# #         super().__init__(name, health, power)
# #         self.inventory = []
# #         self.awareness = []
# #         self.trashbin = []
# #         self.location = location

# #     def alive(self):
# #         if self.health > 0:
# #             return True

# #     # Check the Trash for letters. Boss can append letters here.
# #     def trash(self):
# #         if 'd' in self.trashbin:
# #             pass
# #         elif 's' in self.trashbin:
# #             pass
# #         elif '?' in self.trashbin:
# #             pass
# #         else: print('\nThere is nothing in the trashbin.')

# #     # Rest in bedroom to restore HP
# #     def restore(self):
# #         self.health = 45
# #         print('\nYou take a nap and recover to full hp!')
    
# #     # Talk to Sam
# #     def chat(self):
# #         print('You are talking to Sam.')


# #     # Player encounters the Spelling Nemesis
# #     def encounter(self, target):
# #         print('You hear a maniacal laughter.')
# #         print('The Spelling Nemesis challenges you!')

# #     # Attack the Target
# #     def attack(self, target):
# #         if 'a' in self.inventory: 
# #             target.health -= self.power
# #             print('You attack ' + target.name + ' for ' + str(self.power) + 'dmg!')
# #         # Does not have the correct letter
# #         else: print('You fail to ttck ' + target.name + '.')


# #     # Defend against the Target
# #     def defend(self, target):
# #         if 'd' in self.inventory:
# #             self.health = self.health - target.power/2
# #             print('\nYou defend yourself against the onslaught of ' + target.name + '. ' + target.name + ' does '+ str(target.power/2) + ' dmg. \n')

# #             # Chance to Heal
# #             dice = random.randint(1, 3)
# #             if dice == 2:
# #                 self.health = self.health + 5
# #                 print('BONUS! You were able to heal for 5 hp!\n')
# #                 # Keeps HP to max
# #                 if self.health >= 45:
# #                     self.health = 45
     
# #         # Does not have the correct letter
# #         else:
# #             print('You failed to efen yourself against ' + target.name + '.')
    

# #     # Found a Letter, Goes to Inventory
# #     def obtain(self, letter='none'):
# #         if letter == 'a':
# #             test = 'a'
# #             self.inventory.append(test)
# #         if letter == 'd':
# #             test2 = 'd'
# #             self.inventory.append(test2)
# #         if letter == 's':
# #             test3 = 's'
# #             self.inventory.append(test3)


# # class Boss(Character):
# #     def __init__(self, name, health, power):
# #         super().__init__(name, health, power)

# #     def alive(self):
# #         if self.health > 0:
# #             return True

# #     # Basic Attack
# #     def attack(self, player):
# #         player.health -= self.power



# #     # Special Attack: Nemesis will prompt you to spell a word.
# #     def specialAttack(self, player):
# #         dice = random.randint(1, 2)
# #         if dice == 1:
# #             testing = input('So you think you can spell? Very well. How do you spell DEFINE? ')
# #             if testing == 'define':
# #                 print('AGGGGGHHH!!')
# #             else:
# #                 player.health -= self.power 
# #                 print('I knew you were a fool!')
# #                 print(self.name + ' kicks you for ' + str(self.power) + 'dmg.')
# #         if dice == 2:
# #             pass

# #     # Steals a Letter from the Player, Throws in the Trash
# #     # [???] How to remove a letter and put it somewhere else
# #     def curse(self, player):
# #         print(player.inventory)
# #         player.inventory.pop()
# #         print('Oh no! ' + self.name + ' threw one of your letters in the trash!')
# #         print(player.inventory)


# # class NPC:
# #     def __init__(self, name, greeting, converse1, converse2):
# #         self.name = name 
# #         self.greeting = greeting
# #         self.converse1 = converse1
# #         self.converse2 = converse2

# #     def hello(self, player):
# #         print(self.greeting)
        
# #     def secret(self, player):
# #         pass



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





class Game:
    def __init__(self):
        pass

    # The Nemesis Chance to Challenge the Player
    def encounter(self, chance, player, nemesis):
        dice = random.randint(chance, 100)
        if dice == 100:
            while True:
                print('Oh no! It\'s the Spelling Nemesis!')
                print('\nYou have ' + str(player.health) + ' hp!')
                print('The Spelling Nemesis has ' + str(nemesis.health) + ' hp.\n')
                print()
                print("What do you want to do?")

                # Attack Option
                if 'a' in player.inventory:
                    print ('1. Attack!')
                else: print ('1. ttck!')
                # Defend Option
                if 'd' in player.inventory:
                    print("2. Defend!")
                else:
                    print('2. efen!')
                # Run Away!
                print("3. run")

                print("> ",)
                user_input = int(input())
                if user_input == 1:
                    player.attack(nemesis)
                    nemesis.attacksChance(player)
                if nemesis.health <= 0:
                    print("Impossible!") #Literally Impossible
                elif user_input == 2:
                    player.defend(nemesis)
                elif user_input == 3:
                    print("You run away from the Nemesis.")
                    break
        else: 
            pass
    
    # The Final Encounter with the Nemesis
    def final_encounter(self, chance, player, nemesis):
        while True:
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
                    print("4. Go to the Lobby")
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
                                print("You look into the mirror and notice some of the leeters on your shirt are missing. What could this mean?")
                        # Go back to the Bedroom
                        elif user_input == 2:
                                player.location = 'bedroom'
                                print("You decide to head back into the bedroom.")
                                break
                        else:
                            print('Please enter a valid option.')
            if player.location == 'livingroom':
                while True:
                    print('\nYou are in the LIVINGROOM.')
                    print('What would you like to do?')
                    print('\n1. Inspect the Livingroom')
                    print('2. Go into the Kitchen')
                    print("3. Go to the Bathroom")
                    print("4. Head Outside")
                    print("5. Quit.\n")
                    user_input = int(input('> '))
                    if user_input == 1:
                        print("You flop onto the couch and feel something inbetween the cushions. When you pull it out, it is the letter A")
                    elif user_input == 2:
                        player.location = 'kitchen'
                    elif user_input == 3:
                        player.location = 'bathroom'
                    elif user_input == 4:
                        player.location = 'frontyard'
                    elif user_input == 5: 
                        break
                    else:
                        print('Please enter a valid option.')
            if player.location == 'kitchen':
                while True:
                    print('\nYou are in the KITCHEN.')
                    print('What would you like to do?')
                    print('\n1. Attempt to Cook a Meal')
                    print('2. Investigate the Smell Coming from the Trash')
                    print("3. Go to the Livingroom")
                    print("4. Sit and think (Get a Hint)")
                    print("5. Quit.\n")
                    user_input = int(input('> '))
                    if user_input == 1:
                        print("You open up your fridge to get some milk for cereal. Sadly you don't have any. Maybe you should go to the store...")
                    elif user_input == 2:
                        print("You slowly open the lid to the trash. The smell of 2 week old fish hits you hard.")
                    elif user_input == 3:
                        player.location = 'livingroom'
                    elif user_input == 4:
                        print("You should start thinking about how you can aquire letters. Maybe that will help you down the line.")
                    elif user_input == 5: 
                        break
                    else:
                        print('Please enter a valid option.')

            if player.location == 'frontyard':
                while True:
                    print('\nYou are in the frontyard.')
                    print('What would you like to do?')
                    print('\n1. Investigate the Frontyard')
                    print('2. Get a Pump at the Gym')
                    print("3. Go back inside")
                    print("4. Head to the Library")
                    print("5. Make Your Way to the Middle of Campus")
                    print("5. Quit.\n")
                    user_input = int(input('> '))
                    if user_input == 1:
                        player.restore()
                    elif user_input == 2:
                        player.trash()
                    elif user_input == 3:
                        player.location = 'bathroom'
                        break
                    else:
                        print('Please enter a valid option.')

            if player.location == 'library':
                while True:
                    print('\nYou are in the LIBRARY.')
                    print('What would you like to do?')
                    print('\n1. Take a Nap')
                    print('2. Check the Trashbin')
                    print("3. Go to the Bathroom")
                    print("4. Go to the Lobby")
                    print("5. Quit.\n")
                    user_input = int(input('> '))
                    if user_input == 1:
                        player.restore()
                    elif user_input == 2:
                        player.trash()
                    elif user_input == 3:
                        player.location = 'bathroom'
                        break
                    else:
                        print('Please enter a valid option.')
            if player.location == 'gym':
                while True:
                    print('\nYou are in the GYM.')
                    print('What would you like to do?')
                    print('\n1. Take a Nap')
                    print('2. Check the Trashbin')
                    print("3. Go to the Bathroom")
                    print("4. Go to the Lobby")
                    print("5. Quit.\n")
                    user_input = int(input('> '))
                    if user_input == 1:
                        player.restore()
                    elif user_input == 2:
                        player.trash()
                    elif user_input == 3:
                        player.location = 'bathroom'
                        break
                    else:
                        print('Please enter a valid option.')

            if player.location == 'middleofcampus':
                while True:
                    print('\nYou are in the middle of campus.')
                    print('What would you like to do?')
                    print('\n1. Take a Nap')
                    print('2. Check the Trashbin')
                    print("3. Go to the Bathroom")
                    print("4. Go to the Lobby")
                    print("5. Quit.\n")
                    user_input = int(input('> '))
                    if user_input == 1:
                        player.restore()
                    elif user_input == 2:
                        player.trash()
                    elif user_input == 3:
                        player.location = 'bathroom'
                        break
                    else:
                        print('Please enter a valid option.')


            if player.location == 'administrationbuilding':
                while True:
                    print('\nYou are in the administration building.')
                    print('What would you like to do?')
                    print('\n1. Take a Nap')
                    print('2. Check the Trashbin')
                    print("3. Go to the Bathroom")
                    print("4. Go to the Lobby")
                    print("5. Quit.\n")
                    user_input = int(input('> '))
                    if user_input == 1:
                        player.restore()
                    elif user_input == 2:
                        player.trash()
                    elif user_input == 3:
                        player.location = 'bathroom'
                        break
                    else:
                        print('Please enter a valid option.')

dialogue()
# class Player(Character):
#     def __init__(self, name, health, power, location):
#         super().__init__(name, health, power)
#         self.inventory = []
#         self.awareness = []
#         self.trashbin = []
#         self.location = location

#     def alive(self):
#         if self.health > 0:
#             return True

    def congratulations():
        # print("Insert Congradulations art work?")
        print("Congradulations Player!")
        print("You have vanquished the Spelling Nemesis and regained the ability to spell.")
        print("Hopefully this gave you a new appreciation towards the importance of spelling.")
        print("Exit game?")
        user_input = input("\n Press [ENTER] to end game")
        if user_input == "":
            quit()

# congratulations()

    def game_over(self):
        pass # Add Dialogue, Game Over Screen, Quit Game
        print("MWUHAHAAAAAHAAAAHAAAA! You still havent mastered the ability to spell, you nimrod....")
        print("Enjoy life as a blumbling buffoon.")
        print("Start over?")
        user_input = input("\n Press [ENTER] to restart")
        if user_input == "":
            your_room()


# game_over()
    
    # def print_status(self):
    #     print()
    #     print('You have ' + str(self.health) + ' hp.')
    #     print('You have ' + str(self.power) + ' power!')
    #     print('Your inventory contains: ')
    #     for letter in range(len(self.inventory)):
    #         print(self.inventory[letter])


    # # Check the Trash for letters. Boss can append letters here.
    # def trash(self):
    #     print('You check the trashbin.')
    #     if 'd' in self.trashbin:
    #         self.inventory.append('d')
    #         # index = self.inventory.index('d')
    #         # self.trashbin.pop(index)
    #         print('You recover the letter: \'d\'.')
    #     if 'a' in self.trashbin:
    #         self.inventory.append('a')
    #         # index = self.inventory.index('a')
    #         # self.trashbin.pop(index)
    #         print('You recover the letter: \'a\'.')
    #     if 's' in self.trashbin:
    #         self.inventory.append('s')
    #         print('You recover the letter \'s\'')
    #     else: print('\nThere is nothing in the trashbin.')
    
    # # Interact with the Sign in the Gym
    # def sign(self, player):
    #     print("Due to COVIB restrictions, the gym is closeb until further notice.")
    #     print("Hmm. The sign seems to be off, but you're not sure in what way.")
    #     print("Read it again? Type \'y\' or \'n\'.")
    #     user_input = input('> ')
    #     if user_input == 'y':
    #         print("You squint at the sign and read closer.") 
    #         print('The Bs are actually Ds!')
    #         print("Your memory gradually comes back to you...")
    #         player.inventory.append('d')
    #         print('You obtain the letter: \'D\'!')
    #     else: 
    #         print("You can't figure it out and decide to leave it alone.")

    # # Rest in bedroom to restore HP
    # def restore(self):
    #     self.health = 45
    #     print('\nYou take a nap and recover to full hp!')

    # # Attack the Target
    # def attack(self, target):
    #     if 'a' in self.inventory: 
    #         target.health -= self.power
    #         print('You attack ' + target.name + ' for ' + str(self.power) + 'dmg!')
    #     # Does not have the correct letter
    #     else: print('You fail to ttck ' + target.name + '.')
    
    # def teach(self, target):
    #     if 's' in self.inventory:
    #         target.health -= self.power * 2
    #         print('You decide to teach The Spelling Nemesis a lesson. Literally.')
    #     else: print('Can\'t you read? This option is INVALID.')


    # # Defend against the Target
    # def defend(self, target):
    #     if 'd' in self.inventory:
    #         self.health = self.health - target.power/2
    #         print('\nYou defend yourself against the onslaught of ' + target.name + '. ' + target.name + ' does '+ str(target.power/2) + ' dmg. \n')

    #         # Chance to Heal
    #         dice = random.randint(1, 3)
    #         if dice == 2:
    #             self.health = self.health + 5
    #             print('BONUS! You were able to heal for 5 hp!\n')
    #             # Keeps HP to max
    #             if self.health >= 45:
    #                 self.health = 45
     
    #     # Does not have the correct letter
    #     else:
    #         print('You failed to efen yourself against ' + target.name + '.')
    
    # # Find a Book in the Library, 100% Encounter
    # def book(self, player):
    #     print('You decide to read a book.')
    #     player.power = player.power + 5
    #     print('Your power increases by 5!')
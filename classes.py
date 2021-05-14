# Global-Scope
import random

class Location:
    def __init__(self, name, description, connections):
        self.name = name
        self.description = description
        self.connections = connections
# Inside of the Bedroom
    def dialogue(self, player):
        while True:
            if player.location == 'bedroom':
                while True:
                    # You are in the BEDROOM
                    print(self.description)
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
            # You are in the Bathroom
            if player.location == 'bathroom':
                while True:
                        print('\nYou are in the BATHROOM.')
                        print('What would you like to do?')

                        print('\n1. Check the Mirror')
                        print('2. Go back to the Bedroom')
                        user_input = int(input('> '))
                        # Check the Mirror
                        if user_input == 1:
                                player.mirror()
                        # Go back to the Bedroom
                        elif user_input == 2:
                                player.location = 'bedroom'
                                break
                        else:
                            print('Please enter a valid option.')

class Character:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power


class Player(Character):
    def __init__(self, name, health, power, location):
        super().__init__(name, health, power)
        self.inventory = []
        self.awareness = []
        self.trashbin = []
        self.location = location

    def alive(self):
        if self.health > 0:
            return True

    # Check the Trash for letters. Boss can append letters here.
    def trash(self):
        if 'd' in self.trashbin:
            pass
        elif 's' in self.trashbin:
            pass
        elif '?' in self.trashbin:
            pass
        else: print('\nThere is nothing in the trashbin.')

    # Rest in bedroom to restore HP
    def restore(self):
        self.health = 45
        print('\nYou take a nap and recover to full hp!')
    
    # Talk to Sam
    def chat(self):
        print('You are talking to Sam.')


    # Player encounters the Spelling Nemesis
    def encounter(self, target):
        print('You hear a maniacal laughter.')
        print('The Spelling Nemesis challenges you!')

    # Attack the Target
    def attack(self, target):
        if 'a' in self.inventory: 
            target.health -= self.power
            print('You attack ' + target.name + ' for ' + str(self.power) + 'dmg!')
        # Does not have the correct letter
        else: print('You fail to ttck ' + target.name + '.')


    # Defend against the Target
    def defend(self, target):
        if 'd' in self.inventory:
            self.health = self.health - target.power/2
            print('\nYou defend yourself against the onslaught of ' + target.name + '. ' + target.name + ' does '+ str(target.power/2) + ' dmg. \n')

            # Chance to Heal
            dice = random.randint(1, 3)
            if dice == 2:
                self.health = self.health + 5
                print('BONUS! You were able to heal for 5 hp!\n')
                # Keeps HP to max
                if self.health >= 45:
                    self.health = 45
     
        # Does not have the correct letter
        else:
            print('You failed to efen yourself against ' + target.name + '.')
    

    # Found a Letter, Goes to Inventory
    def obtain(self, letter='none'):
        if letter == 'a':
            test = 'a'
            self.inventory.append(test)
        if letter == 'd':
            test2 = 'd'
            self.inventory.append(test2)
        if letter == 's':
            test3 = 's'
            self.inventory.append(test3)


class Boss(Character):
    def __init__(self, name, health, power):
        super().__init__(name, health, power)

    def alive(self):
        if self.health > 0:
            return True

    # Basic Attack
    def attack(self, player):
        player.health -= self.power



    # Special Attack: Nemesis will prompt you to spell a word.
    def specialAttack(self, player):
        dice = random.randint(1, 2)
        if dice == 1:
            testing = input('So you think you can spell? Very well. How do you spell DEFINE? ')
            if testing == 'define':
                print('AGGGGGHHH!!')
            else:
                player.health -= self.power 
                print('I knew you were a fool!')
                print(self.name + ' kicks you for ' + str(self.power) + 'dmg.')
        if dice == 2:
            pass

    # Steals a Letter from the Player, Throws in the Trash
    # [???] How to remove a letter and put it somewhere else
    def curse(self, player):
        print(player.inventory)
        player.inventory.pop()
        print('Oh no! ' + self.name + ' threw one of your letters in the trash!')
        print(player.inventory)


class NPC:
    def __init__(self, name, greeting, converse1, converse2):
        self.name = name 
        self.greeting = greeting
        self.converse1 = converse1
        self.converse2 = converse2

    def hello(self, player):
        print(self.greeting)
        
    def secret(self, player):
        pass


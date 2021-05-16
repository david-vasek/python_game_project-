# Global-Scope
import audio
import random
import os
clear = lambda: os.system('clear')
import sys
import time
from pygame import mixer
from text import title, story, slowprint, your_room, bathroom, fake_victory, falling_asleep, wake_up, trash_can, trash_can_a, trash_can_d, find_item, rustle_sound, sleeping_frame, punch_sound, nemesis_laugh, jarble_attack, battle_music, nemesis_fight

class Game:
    def __init__(self):
        pass

    # The Nemesis Chance to Challenge the Player
    def encounter(self, chance, player, nemesis):
        slowprint("You thought you were safe in the " + str(player.location))
        mixer.Sound.play(nemesis_laugh)
        dice = random.randint(chance, 100)
        if dice == 100:
            while True:
                nemesis_fight()
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
                    mixer.music.load('audio/home_song.wav')
                    mixer.music.play(-1)
                    bathroom()
                    print("You run away from the Nemesis.")
                    
                    break
        else: 
            pass
    
    # The Final Encounter with the Nemesis
    def final_encounter(self, chance, player, nemesis):
        pass

    # The Game Itself
    def dialogue(self, player, nemesis):
        while True:
            if player.location == 'bedroom':
                while True:
                    your_room()
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
                    elif user_input == 2:
                        player.trash()
                    elif user_input == 3:
                        player.location = 'bathroom'
                        break
                    elif user_input == 5:
                        quit()
                    else:
                        print('Please enter a valid option.')
            # You are in the Bathroom
            if player.location == 'bathroom':
                while True:
                        bathroom()
                        self.encounter(100, player, nemesis)
                        print('You are in the BATHROOM.')
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
        self.inventory = ['a', 'd']
        self.awareness = []
        self.trashbin = []
        self.location = location

    def alive(self):
        if self.health > 0:
            return True

    # Check the Trash for letters. Boss can append letters here.
    def trash(self):
        trash_can()
        slowprint('You check the trashbin.')
        if 'd' in self.trashbin:
            trash_can_d()
            self.inventory.append('d')
            # index = self.inventory.index('d')
            # self.trashbin.pop(index)
            slowprint('You recover the letter: \'d\'.')
            user_input = input ('[ENTER]')
            if user_input == "":
                pass
            else:
                 pass
        if 'a' in self.trashbin:
            trash_can_a()
            self.inventory.append('a')
            # index = self.inventory.index('a')
            # self.trashbin.pop(index)
            slowprint('You recover the letter: \'a\'.')
            user_input = input ('[ENTER]')
            if user_input == "":
                pass
            else:
                pass           
        if '?' in self.trashbin:
            pass
        else: slowprint('\nThere is nothing in the trashbin.')

    # Rest in bedroom to restore HP
    def restore(self):
        sleeping_frame()
        self.health = 45
        slowprint('\nYou take a nap and recover to full hp!')
    
    # Talk to Sam
    def chat(self):
        print('You are talking to Sam.')

    # Attack the Target
    def attack(self, target):
        if 'a' in self.inventory: 
            mixer.Sound.play(punch_sound)
            target.health -= self.power
            print('You attack ' + target.name + ' for ' + str(self.power) + 'dmg!')
            press_enter = input('Press [ENTER]')
        # Does not have the correct letter
        else: slowprint('You fail to ttck ' + target.name + '.')


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
    def obtain(self, letter=''):
        if letter == 'a':
            test = 'a' #Array
            self.inventory.append(test)
        if letter == 'd':
            test2 = 'd' # Define
            self.inventory.append(test2)
        if letter == 's':
            test3 = 's' #String
            self.inventory.append(test3)


class Boss(Character):
    def __init__(self, name, health, power):
        super().__init__(name, health, power)

    def alive(self):
        if self.health > 0:
            return True

    # Basic Attack
    def attack(self, player):
        mixer.Sound.play(jarble_attack)
        player.health -= self.power
        print('The Spelling Nemesis attacks you with a jarble of words!')
        press_enter = input('Press [ENTER]')


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

    # Steals a letter from the Player, Throws in the Trash
    def curse(self, player):
        player.trashbin.append(player.inventory.pop())
        print('Oh no! ' + self.name + ' threw one of your letters in the trash!')
    
    # Randomizes what attck is used.
    def attacksChance(self, player):
        dice = random.randint(1, 3)
        if dice == 1:
            self.curse(player)
        # elif dice > 1 and dice <= 20:
        #     self.specialAttack(player)
        else:
            self.attack(player)
        


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


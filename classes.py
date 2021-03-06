# Global-Scope
import audio
import random
import os
clear = lambda: os.system('clear')
import sys
import time  
from pygame import mixer
from text import title, nemesis_gfx, sean_head, goofy_nemesis, go_outside, shush_sound, library_lady, gym_location, closed_sign, library_scene, zach_lobby, mirror, final_battle, story, that_impossible, slowprint, your_room, bathroom, fake_victory, falling_asleep, wake_up, trash_can, trash_can_a, trash_can_d, rustle_sound, sleeping_frame, battle_music, nemesis_fight

find_item = mixer.Sound("audio/item_fanfare.wav")
puzzle_solved = mixer.Sound("audio/puzzle_solved.wav")
find_item_big = mixer.Sound("audio/item_fanfare_big.wav")
punch_sound = mixer.Sound("audio/punch_sound.wav")
kick_sound = mixer.Sound("audio/kick.wav")
voice_1 = mixer.Sound("audio/voice_1.wav")
voice_2 = mixer.Sound("audio/voice_2.wav")
voice_3 = mixer.Sound("audio/voice_3.wav")
nemesis_laugh = mixer.Sound("audio/nemesislaugh.wav")
jarble_attack = mixer.Sound("audio/jarble_attack.wav")


class Game:
    def __init__(self):
        pass

    # The Nemesis Chance to Challenge the Player
    def encounter(self, chance, player, nemesis):
        slowprint("You thought you were safe in the " + str(player.location) + " but...")
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
                user_input = input()
            
                if user_input == '1':
                    player.attack(nemesis)
                    nemesis.attacksChance(player)
                if player.health <= 0:
                    player.game_over()
                    

                elif user_input == '2':
                    player.defend(nemesis)

                elif user_input == '3':
                    mixer.music.load('audio/home_song.wav')
                    mixer.music.play(-1)
                    bathroom()
                    print("You run away from the Nemesis...")
                    break
                else: 
                    pass
    
#-------------------------------------------------------------------------------------

    def outsideEncounters(self, player, nemesis):
        dice = random.randint(1, 100)
        if dice < 10:
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
                print("3. Run Away!")

                print("> ",)
                # The Actual Options
                user_input = int(input())

                # Attack Function Call
                if user_input == 1:
                    player.attack(nemesis)
                    nemesis.attacksChance(player)
                    if player.health <= 0:
                        player.game_over()
                if nemesis.health <= 0:
                    print("Impossible!") #Literally Impossible
                # Defend Function Call
                elif user_input == 2:
                    player.defend(nemesis)
        
                # Run Away Function Call
                elif user_input == 3:
                    print("You run away from the Nemesis...")
                    break
        else: 
            print('Have you forgotten how to count? Please enter a valid input.')

 #-------------------------------------------------------------------------------------

    # The Final Encounter with the Nemesis
    def final_encounter(self, player, nemesis):
        mixer.music.pause()
        mixer.music.load('audio/final_battle.wav')
        mixer.music.play(-1)
        nemesis_gfx()
        print('Oh no! It\'s the Spelling Nemesis!')
        press_enter = input('Press [ENTER] to continue ')
        # record scratch?
        library_lady()
        print('You hear a loud \"SHHHH!\" from the librarian.')
        print('You decide to take this outside.')
        slowprint('.....')
        press_enter = input('Press [ENTER] to continue ')
        goofy_nemesis()
        print()
        print('You two step OUTSIDE.')
        press_enter = input('Press [ENTER] .. to continue your fight..')
        mixer.music.load('audio/final_battle.wav')
        mixer.music.play(-1)
        

        if 'a' in player.inventory and 'd' in player.inventory and 's' in player.inventory:
            nemesis.set_health(150)
            player.health = 100
        elif 'a' in player.inventory and 'd' in player.inventory:
            nemesis.set_health(150)
            player.health = 70
        else: 
            pass

    # Final Battle Sequence
        while player.alive() and nemesis.alive():
            nemesis_gfx()
            print('\nYou have ' + str(player.health) + ' hp!')
            print('The Spelling Nemesis has ' + str(nemesis.health) + ' hp.\n')
            print()
            print("What do you want to do?")
            print ('1. Attack!')
            print("2. Defend!")
            if 's' in player.inventory:
                print('3. Teach')
            else: 
                print('3. invalid')
            print("4. Run")
            print()
            # The Actual Options
            user_input = int(input('> '))

            # Attack Function Call
            if user_input == 1:
                player.attack(nemesis)
                nemesis.attacksFinal(player)

                # [ Win Sequence ]
                if nemesis.health <= 0:
                    player.congratulations() 
                # [ Lose Sequence ]
                if player.health <= 0:
                    player.game_over()

            # Defend Function Call
            elif user_input == 2:
                player.defend(nemesis)
            
            elif user_input == 3:
                player.teach(nemesis)

            # Special Function Call
            elif user_input == 3:
                player.teach(nemesis)
                nemesis.attacksFinal(player)
                # [ Win Sequence ]
                if nemesis.health <= 0:
                    player.congratulations()
                # [ Lose Sequence ]
                if player.health <= 0:
                    player.game_over()    

            # Run Away Function Call
            elif user_input == 4:
                print("You run away from the Spelling Nemesis...")
                break
            else: 
                print('Have you also forgotten how to count? Try again. ')

    # The Game Itself
    def dialogue(self, player, nemesis, sean, zach, sam):
        while True:
            # You are in the BEDROOM
            if player.location == 'bedroom':
                while True:
                    your_room()
                    print('\nYou are in the BEDROOM.')
                    print('What would you like to do?')
                    print('\n1. Take a Nap')
                    print('2. Check the Trashbin')
                    print("3. Go to the Bathroom")
                    print("4. Go to the Lobby")
                    print()
                    user_input = int(input('> '))
                    if user_input == 1:
                        print("You lay down in bed and when you wake, you feel less hungover and refreshed.")
                        player.restore()
                    elif user_input == 2:
                        player.trash()
                        print("You check the trash, but nothing seems to be in it.... maybe check back later.")
                    elif user_input == 3:
                        player.location = 'bathroom'
                        break
                    elif user_input == 4:
                        player.location = 'lobby'
                        break
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
                        print()
                        user_input = int(input('> '))
                        # Check the Mirror
                        if user_input == 1:
                                mirror()
                                print("You look at the sweat dripping from your forehead. Was that thing real?")
                                print("You try and convince yourself it was not and you decide to go back to your room...")
                                press_enter = input('Press [ENTER] to continue ')
                                player.location = 'bedroom'
                                break
                        # Go back to the Bedroom
                        elif user_input == 2:
                                player.location = 'bedroom'
                                print("You decide to head back into the bedroom.")
                                break
                        else:
                            print('Please enter a valid option.')

            # You are in the LOBBY.
            if player.location == 'lobby':
                while True:
                    zach_lobby()
                    print('\nYou are in the LOBBY.')
                    print('Your friend Zach is working the front desk.')
                    print('It looks like he\'s studying.')
                    print("What would you like to do?")
                    if 'zach1' and 'zach2' in player.awareness:
                        print('\n1. Talk to Zach again')
                    elif 'zach1' in player.awareness:
                        print('\n1. Help Zach with his writing')
                    else:
                        print('\n1. Talk to Zach')
                    print('2. Go outside')
                    print("3. Return to your bedroom")
                    print()
                    user_input = int(input('> '))
                    print()
                    if user_input == 1:
                        if 'zach1' and 'zach2' in player.awareness:
                            zach.zachTalk3(player)
                        elif 'zach1' in player.awareness:
                            zach.zachTalk2(player) 
                        else: zach.zachTalk(player)
                    elif user_input == 2:
                        player.location = 'outside'
                        break
                    elif user_input == 3:
                        player.location = 'bedroom'
                        break
                    else:
                        print('Please enter a valid option.')

            # You are OUTSIDE.
            if player.location == 'outside':
                while True:
                    go_outside()
                    self.outsideEncounters(player, nemesis)
                    print('\nYou are OUTSIDE')
                    print('There is an instructor dude checking their phone nearby.')
                    print('What would you like to do?')
                    print()
                    if 'sean1' and 'sean2' in player.awareness:
                        print('1. Talk to Instructor Dude again')
                    elif 'sean1' in player.awareness:
                        print('1. Ask Instructor Dude for a contrived example')
                    else:
                        print('1. Talk to the Instructor Dude')
                    print('2. Check your surroundings')
                    print('3. Get a Pump at the Gym')
                    print("4. Head to the Library")
                    print("5. Return to the Lobby")
                    user_input = int(input('> '))
                    if user_input == 2:
                        print('Something seems off as you scan the area.')
                        press_enter = input("Press [ENTER] to continue ")
                        print('Letters seem to be missing from signs and words.') 
                        press_enter = input("Press [ENTER] to continue ")
                        print('You wonder if you\'re the only one seeing this...')
                        press_enter = input("Press [ENTER] to continue ")
                    elif user_input == 3:
                        player.location = 'gym'
                        break
                    elif user_input == 1:
                        sean_head()
                        print("You walk up to the instructor, wondering what he might have to say.")  
                        if 'sean1' and 'sean2' in player.awareness:
                            sean.seanTalk3()
                        elif 'sean1' in player.awareness:
                            sean.seanTalk2(player) 
                        else: 
                            sean.seanTalk(player)

                    elif user_input == 4:
                        player.location = 'library'
                        break
                    elif user_input == 5:
                        player.location = 'lobby'
                        break
                    else:
                        print('Please enter a valid option.')

            # You are at the LIBRARY!
            if player.location == 'library':
                while True:
                    library_scene()
                    print('\nYou are at the LIBRARY.')
                    print('The librarian welcomes you.')
                    print('There is someone looking in your direction nearby.')
                    print('What would you like to do?')
                    if 'sam1' and 'sam2' in player.awareness:
                        print('1. Talk to Sam... again!')
                    elif 'sam1' in player.awareness:
                        print('1. Talk to Sam')
                    else: 
                        print('1. Talk to the man staring')
                    print("2. Return outside")
                    # Does this actually work? #
                    if 'd' and 'a' in player.inventory and 'sam2' in player.awareness:
                        print("3. Read a Book")
                    else:
                        pass
                    user_input = int(input('> '))
                    if user_input == 1:
                        if 'sam1' in player.awareness and 'sam2' in player.awareness:
                            sam.samTalk3(player)
                        elif 'sam1' in player.awareness:
                            sam.samTalk2(player) 
                        else: sam.samTalk(player)
                    elif user_input == 2:
                        player.location = 'outside'
                        break
                    elif user_input == 3:
                        player.book(player)
                        self.final_encounter(player, nemesis)
                    else:
                        print('Please enter a valid option.')
                    
            # You are at the GYM
            if player.location == 'gym':
                while True:
                    gym_location()
                    self.outsideEncounters(player, nemesis)
                    print('\nYou are in the GYM.')
                    print('\n There is a sign posted on the entrance.')
                    print('What would you like to do?')
                    print('\n1. Read the Sign')
                    print('2. Head Back')
                    user_input = int(input('> '))
                    if user_input == 1:
                        closed_sign()
                        player.sign(player)
                    elif user_input == 2:
                        player.location = 'outside'
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

    def congratulations(self):
        # print("Insert Congradulations art work?")
        print("Congratulations Player!")
        print("You have vanquished the Spelling Nemesis and regained the ability to spell.")
        print("Hopefully this gave you a new appreciation towards the importance of spelling.")
        print("Exit game?")
        user_input = input("\n Press [ENTER] to end game")
        if user_input == "":
            quit()

    def game_over(self):
        print("MWUHAHAAAAAHAAAAHAAAA! You still haven't mastered the ability to spell, you nimrod....")
        print("Enjoy life as a blumbling buffoon.")
        print("Start over?")
        user_input = input("\n Press [ENTER] to restart")
        if user_input == "":
            your_room()
    
    def print_status(self):
        print()
        print('You have ' + str(self.health) + ' hp.')
        print('You have ' + str(self.power) + ' power!')
        print('Your inventory contains: ')
        for letter in range(len(self.inventory)):
            print(self.inventory[letter])

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
        if 'a' in self.trashbin:
            trash_can_a()
            self.inventory.append('a')
            # index = self.inventory.index('a')
            # self.trashbin.pop(index)
            slowprint('You recover the letter: \'a\'.')
        if 's' in self.trashbin:
            trash_can_s()
            self.inventory.append('s')
            slowprint('You recover the letter \'s\'')        

        else: slowprint('\nThere is nothing in the trashbin.')

    # Interacting with the sign
    def sign(self, player):
        print("Due to COVIB restrictions, the gym is closeb until further notice.")
        print("Hmm. The sign seems to be off, but you're not sure in what way.")
        print("Read it again?")
        user_input = input('> ')
        if user_input == 'y':
            print("You squint at the sign and read closer. The Bs are actually Ds!")
            print('The Bs are actually Ds!')
            press_enter = input ('Press [ENTER] to continue ')
            mixer.Sound.play(puzzle_solved)
            print("Your memory gradually comes back to you...")
            press_enter = input ('Press [ENTER] to continue ')
            player.inventory.append('d')
            print('You obtain the letter: \'D\'!')
            mixer.Sound.play(find_item)
            press_enter = input ('Press [ENTER] to continue ')
        else: 
            print("You can't figure it out and decide to leave it alone.")
            press_enter = input ('Press [ENTER] to continue ')

    # Rest in bedroom to restore HP
    def restore(self):
        sleeping_frame()
        self.health = 45
        print('\nYou take a nap and recover to full hp!')
        press_enter = input ('Press [ENTER] to continue ')

    # Attack the Target
    def attack(self, target):
        if 'a' in self.inventory: 
            mixer.Sound.play(punch_sound)
            target.health -= self.power
            print('You attack ' + target.name + ' for ' + str(self.power) + 'dmg!')
            press_enter = input('Press [ENTER] to continue ')
        # Does not have the correct letter
        else: 
            print('You fail to ttck ' + target.name + '.')
            press_enter = input("Press [ENTER] to continue ")

    def teach(self, target):
        if 's' in self.inventory:
            target.health -= self.power * 2
            print('You decide to teach The Spelling Nemesis a lesson. Literally.')
            press_enter = input ('Press [ENTER] to continue ')
        else: 
            print('Can\'t you read? This option is INVALID.')
            press_enter = input ('Press [ENTER] to continue ')

    # Defend against the Target
    def defend(self, target):
        if 'd' in self.inventory:
            self.health = self.health - target.power/2
            print('\nYou defend yourself against the onslaught of ' + target.name + '. ' + target.name + ' does '+ str(target.power/2) + ' dmg. \n')
            press_enter = input ('Press [ENTER] to continue ')
            
            # Chance to Heal
            dice = random.randint(1, 3)
            if dice == 2:
                self.health = self.health + 5
                print('BONUS! You were able to heal for 5 hp!\n')
                press_enter = input ('Press [ENTER] to continue ')
                # Keeps HP to max
                if self.health >= 45:
                    self.health = 45
     
        # Does not have the correct letter
        else:
            mixer.Sound.play(buzz)
            print('You failed to efen yourself against ' + target.name + '.')
            press_enter = input('Press [ENTER] to continue ')
    
    # Find a Book in the Library, 100% Encounter
    def book(self, player):
        print('You decide to read a book.')
        mixer.Sound.play(puzzle_solved)
        press_enter = input ('Press [ENTER] to continue ')
        player.power = player.power + 10
        mixer.Sound.play(find_item_big)
        print('Your power increases by 10!')
        press_enter = input ('Press [ENTER] to continue ')

class Boss(Character):
    def __init__(self, name, health, power):
        super().__init__(name, health, power)

    # Check Status
    def alive(self):
        if self.health > 0:
            return True

    # Change Health 
    def set_health(self, value):
        self.health = value

    # Basic Attack
    def attack(self, player):
        mixer.Sound.play(jarble_attack)
        player.health -= self.power
        print('The Spelling Nemesis attacks you with a jarble of words!')
        press_enter = input('Press [ENTER] to continue ')


    # Special Attack: Nemesis will prompt you to spell a word.
    def specialAttack(self, player):
        dice = random.randint(1, 2)
        if dice == 1:
            mixer.Sound.play(nemesis_laugh)
            testing = input('So you think you can spell? Very well. How do you spell DEFINE? ')
            if testing == 'define':
                mixer.Sound.play(that_impossible)
                print('AGGGGGHHH!!')
                press_enter = input('Press [ENTER] to continue ')
            else:
                player.health -= self.power 
                print('I knew you were a fool!')
                mixer.Sound.play(kick_sound)
                print(self.name + ' kicks you for ' + str(self.power) + 'dmg.')
                press_enter = input('Press [ENTER] to continue ')
        if dice == 2:
            print('So you think you can spell? Very well.')
            spelling2 = input('How do you spell PRINT? ')
            if spelling2 == 'print':
                mixer.Sound.play(that_impossible)
                print('AGGGGGHHH!!')
                press_enter = input('Press [ENTER] to continue ')
            else:
                player.health -= self.power 
                print('I knew you were a fool!')
                mixer.Sound.play(kick_sound)
                print(self.name + ' kicks you for ' + str(self.power) + 'dmg.')
                press_enter = input('Press [ENTER] to continue ')

    # Steals a letter from the Player, Throws in the Trash
    def curse(self, player):
        if player.inventory.len() > 1:
            player.trashbin.append(player.inventory.pop())
            print('Oh no! ' + self.name + ' threw one of your letters in the trash!')
            press_enter = input("Press [ENTER] to continue ")
        else: 
            print('The Spelling Nemesis tried to steal a letter from you!')
            print('There\'s not enough letters in your vocabulary to steal!')
            print('The attack fails.')
            press_enter = input("Press [ENTER] to continue ")

    # Randomizes what attck is used.
    def attacksChance(self, player):
        dice = random.randint(1, 100)
        if dice == 1:
            self.curse(player)
        elif dice > 1 and dice <= 20:
            self.specialAttack(player)
        else:
            self.attack(player)

    # Final Battle Options
    def attacksFinal(self, player):
        dice = random.randint(1, 100)
        if dice == 1:
            print("The Spelling Nemesis tries to steal one of your letters, but fails! Your spelling ability is too solid.")
            press_enter = input('Press [ENTER] to continue ')
            mixer.Sound.play(that_impossible)
            print('The Spelling Nemesis: \"Where has all this power come from?!\"')
            press_enter = input('Press [ENTER] to continue ')
        elif dice > 1 and dice <= 20:
            self.specialAttack(player)
        else:
            self.attack(player)

class NPC:
    def __init__(self, name):
        self.name = name 

    def hello(self, player):
        print(self.greeting)
        
    def secret(self, player):
        pass

# ====================================================================================================

    # First Conversation Zach
    def zachTalk(self, player):
        player.awareness.append('zach1')
        print('You decide to chat with Zach.')
        press_enter = input('Press [ENTER] to continue ')
        mixer.Sound.play(voice_3)
        print('Zach: \"Hey! I\'m finishing my weekly write-up right now.')
        mixer.Sound.play(voice_2)
        print('Can you believe I found some of my notes in the trash? Glad I checked!\"')
        press_enter = input('Press [ENTER] to continue ')
        # Change option to 'Help Zach wih his Work'
        # Create the append for self.awareness to make this work
        # if player.awareness == 'zach1':

    # Second Conversation Zach
    def zachTalk2(self, player):
        print('You see that Zach is deep in thought.')
        press_enter = input('Press [ENTER] to continue ')
        print('Zach: \"Oh? I\'m alright. I was just trying to remember another word for a list.\"')
        answer = input('Zach: What was it again? >> ').lower()
        if answer == 'array':
            print()
            player.awareness.append('zach2')
            mixer.Sound.play(voice_1)
            print('Zach: \"Wow thanks! Now I can finish my write-up.\"')
            press_enter = input('Press [ENTER] to continue ')
            mixer.Sound.play(puzzle_solved)
            print('Your memories are slowly coming back to you...')
            press_enter = input('Press [ENTER] to continue ')
            player.inventory.append('a')
            mixer.Sound.play(find_item)
            print('You obtain the letter \'A\'! Now you can attack!')
            press_enter = input('Press [ENTER] to continue ')
        else:
            print()
            mixer.Sound.play(voice_3)
            print('Zach: \"I don\'t think that\'s it...\"')
            press_enter = input('Press [ENTER] to continue ')
    
    def zachTalk3(self, player):
        mixer.Sound.play(voice_2)
        print('Zach: \"Thanks again! I\'d head outside if you need some fresh air.\"')
        press_enter = input('Press [ENTER] to continue ')

    # First Conversation Sam
    def samTalk(self, player):
        player.awareness.append('sam1')
        print('You decide to approach Sam.')
        press_enter = input('Press [ENTER] to continue ')
        mixer.Sound.play(voice_1)
        print('Sam: \"Hey! What\'s up? Are you looking for a new book? You should check the manga section. They\'ve added some really great additions recently. You might want to prepare yourself before you read it though.\"')
        press_enter = input('Press [ENTER] to continue ')

    # Second Conversation Sam
    def samTalk2(self, player):
        player.awareness.append('sam2')
        print('You talk to Sam again.')
        press_enter = input('Press [ENTER] to continue ')
        mixer.Sound.play(voice_2)
        print('Sam: \"Have you been by the Gym? It\'s right across the street to the right from here.\"')
        press_enter = input('Press [ENTER] to continue ')

    def samTalk3(self, player):
        player.awareness.append('sam3')
        mixer.Sound.play(voice_3)
        print('Sam: \"Don\'t be afraid to ask questions!\"')
        press_enter = input('Press [ENTER] to continue ')



    # First Conversation ID Sean
    def seanTalk(self, player):
        player.awareness.append('sean1')
        mixer.Sound.play(voice_1)
        print('Sean: \"Nice to see you outside! Make sure you get some rest if you aren\'t feeling good.\"')
        press_enter = input('Press [ENTER] to continue ')
    
    # Second Conversation ID Sean
    def seanTalk2(self, player):
        mixer.Sound.play(voice_3)
        print('Sean: \"You want a bonus question? OK!\"')
        press_enter = input('Press [ENTER] to continue ')
        mixer.Sound.play(voice_2)
        print('Sean: \"What\'s a word for wrapping related data?\"')
        answer = input('It starts with an \'E\'? >> ').lower()
        if answer == 'encapsulate' or answer == 'encapsulation':
            mixer.Sound.play(voice_3)
            print('Sean: \"Awesome job!\"')
            player.inventory.append('s')
            player.awareness.append('sean2')
            mixer.Sound.play(voice_3)
            print('Your ability to spell is SUPERB!')
            press_enter = input('Press [ENTER] to continue ')
            mixer.Sound.play(find_item_big)
            print('You obtain the letter \'S\'!')
            press_enter = input('Press [ENTER] to continue ')
        else:
            mixer.Sound.play(voice_3)
            print('Sean: \"Nope! Sorry. You can always do a Google search for help!\"')
            press_enter = input('Press [ENTER] to continue ')
    
    # Ending Conversation
    def seanTalk3(self):
        mixer.Sound.play(voice_2)
        print('Sean: \"Make sure you take breaks!\"')
        press_enter = input('Press [ENTER] to continue ')
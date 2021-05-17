from classes import *
import audio
import os
clear = lambda: os.system('clear')
import sys
import time
from pygame import mixer
from text import opening_sequence

# Character Instances
player = Player('You', 45, 5, 'bedroom')
nemesis = Boss('The Spelling Nemesis', 9999, 3)
sean = NPC('Sean')
zach = NPC('Zach')
sam = NPC('Sam')
# lobby = Location('Lobby', 'You are in the LOBBY.', [])
# gym = Location('Gym', 'You are outside of the GYM.', [])

start = Game()
opening_sequence()
start.dialogue(player, nemesis, sean, zach, sam)
start.final_encounter(player, nemesis)
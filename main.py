from classes import *
import audio
import os
clear = lambda: os.system('clear')
import sys
import time
from pygame import mixer
from text import opening_sequence

voice_1 = mixer.Sound("audio/voice_1.wav")
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
from classes import Game, Player, Boss, NPC

# Character Instances
player = Player('You', 45, 5, 'bedroom')
nemesis = Boss('The Spelling Nemesis', 9999, 3)
sean = NPC('Sean')
zach = NPC('Zach')
sam = NPC('Sam')
# lobby = Location('Lobby', 'You are in the LOBBY.', [])
# gym = Location('Gym', 'You are outside of the GYM.', [])

start = Game()
# start.dialogue(player, nemesis)
start.final_encounter(player, nemesis)


# sean.seanTalk2(player)
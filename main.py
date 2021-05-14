from classes import Location, Player, Boss

# Character Instances
player = Player('You', 45, 5, 'bedroom')
nemesis = Boss('The Spelling Nemesis', 100, 3)
# sean = NPC('Sean')
# zach = NPC('Zach')
# sam = NPC('Sam')

# Locations
bedroom = Location("Bedroom", "You are in the bedroom.", ['bathroom', 'lobby'])
bathroom = Location('Bathroom', 'You are in the BATHROOM.', ['bedroom'])
# lobby = Location('Lobby', 'You are in the LOBBY.', [])
# gym = Location('Gym', 'You are outside of the GYM.', [])

# START in the BEDROOM
bedroom.dialogue(player)

# player.obtain('a')
# player.obtain('d')
# player.attack(nemesis)
# player.defend(nemesis)
# nemesis.curse(player)
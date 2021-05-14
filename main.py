from classes import Player, Boss, NPC, Location

# Character Instances
player = Player('You', 45, 5)
nemesis = Boss('The Spelling Nemesis', 100, 3)
# sean = NPC('Sean')
# zach = NPC('Zach')
# sam = NPC('Sam')

# Locations
bedroom = Location('Bedroom', '\nYou are in the BEDROOM.')
bathroom = Location('Bathroom', 'You are in the BATHROOM.')
lobby = Location('Lobby', 'You are in the LOBBY.')
gym = Location('Gym', 'You are outside of the GYM.')

# START in the BEDROOM

bedroom.bedroom_dialogue(player)

# player.obtain('a')
# player.obtain('d')
# player.attack(nemesis)
# player.defend(nemesis)
# nemesis.curse(player)
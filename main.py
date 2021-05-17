from classes import Game, Player, Boss, NPC

# Character Instances
player = Player('You', 45, 5, 'bedroom')
nemesis = Boss('The Spelling Nemesis', 9999, 3)
sean = NPC('Sean')
zach = NPC('Zach')
sam = NPC('Sam')

start = Game()
start.dialogue(player, nemesis, sean, zach, sam)
# sean.seanTalk2(player)
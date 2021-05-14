# Global-Scope
import random

class Location:
    pass

class Character:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power


class Player(Character):
    def __init__(self, name, health, power):
        super().__init__(name, health, power)
        self.inventory = []

    def alive(self):
        if self.health > 0:
            return True

    # Attack the Target
    def attack(self, target):
        if 'a' in self.inventory: 
            target.health -= self.power
            print('You attack ' + target.name + ' for ' + str(self.power) + 'dmg!')
        # Does not have the correct letter
        else: print('You fail to strike ' + target.name + '.')


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
            print('You failed to guard yourself against ' + target.name + '.')
    

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


    def curse(self, player):
        print(player.inventory)
        player.inventory.pop()
        print('Oh no! ' + self.name + ' threw one of your letters in the trash!')
        print(player.inventory)


class NPC:
    def __init__(self, name):
        self.name = name 

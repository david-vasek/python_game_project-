class Location:
    def __init__(self, name, description, connections):
        self.name = name
        self.description = description
        self.connections = connections
        


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

dialogue()

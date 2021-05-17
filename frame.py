import tabulate

table = [["Option 1", 'Start game'], 
         ["Option 2", 'Go to bedroom'], 
         ["Option 3", 'Check trash bin'],
         ["Option 4", 'Go to the gym']]
headers = ['Choose an option to continue']
print(tabulate(table, headers, tablefmt="fancy_grid"))
print(tabulate(table, headers, tablefmt="simple"))
print(tabulate(table, headers, tablefmt="rst"))

def option_4():
    print('option_4 has beeen called')

while True: 
    option = int(input('Enter your option '))
    if option == 1:
        # calls the option selected by the player
        print('This will call the function for this option. An example is - a Start game option')
        break

    elif option == 2:
        # calls the option selected by the player
        print('This will call the function for this option. An example is  - Go to bedroom')

    elif option == 3:

        # calls the option selected by the player
        print(
            'This will call the function for this option. An example is  - Check trash bin')

    elif option == 4:
        option_4()

    else:
        print('Invalid option')
        table = [["Option 1", 'Start game'],
             ["Option 2", 'Go to bedroom'],
             ["Option 3", 'Check trash bin'],
             ["Option 4", 'Go to the gym']]
        headers = ['Choose an option to continue']
        print(tabulate(table, headers, tablefmt="fancy_grid"))
        print(tabulate(table, headers, tablefmt="simple"))
        print(tabulate(table, headers, tablefmt="rst"))
        option = int(input('Enter your option '))








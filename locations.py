# Locations that the user can/will encounter on their journey depending on their choices

# Location 
starting_bedroom = Location("")
front_yard_outside_house = Location("")
library = Location("")
gym = Location("")
shady_woods = Location("")
rec_center = Location("")
 = Location("")
= Location("")

class location:
    def __init__(self, name, description):
        self.name = name
        self.description = description 
    def __str__(self):
        return "You chose to walk towards "




def choose_location(room):
    if starting_bedroom ==:
        return 
    if front_yard_outside_house ==:
        return
    if library ==:
        return
    if gym ==:
        return

# Loop to allow location input
def choose_location(user):
    while True:
        choose_location = input(""" 
                                    1. The Front Yard
                                    2. The Library
                                    3. The Gym
                                    4. The Shady Looking Woods
                                    5. The Recreation Center
                                """)
        print():
            if choose_location == "1":
                front_yard_outside_house()
                front_yard_outside_house_menu(user)
            elif choose_location == "2":
                library()
                library_menu(user)
            elif choose_location == "3":
                gym()
                gym_menu(user)
            elif choose_location == "4":
                shady_woods()
                shady_woods_menu(user)
            elif choose_location == "5":
                rec_center()
                rec_center_menu(user)

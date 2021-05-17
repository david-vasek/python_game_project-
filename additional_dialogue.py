class Dialogue:

# First Interaction with Sam
def samTalk():
    print("You cautiously walk up to the shady guy.")
    print("As you approach him, you realize he appears to be friendly. You begin to feel slightly relieved")
    print("Sam: Good afternoon! I\'m Sam.")
    print("Sam: You look like you could use some advice... (yes or no)")
    answer = input(">").upper()
    if "yes" in answer:
        print("Sam: You might want to consider hitting the gym.")
        print("Looks like you have never touched a weight in your life... your brain might benefit from it too.")
    elif "no" in answer:
        print("Well i am still going to give you some anyways because you look like you need it...")
        print("Hit the gym bro. Might help you not just physically but mentally as well.")


# Second Interaction with Sam
def samTalk2(self, player):
    print("You decide to approach Sam again.")
    print("Sam: Hey again! What\'s up?")
    print("You explain to him what is happening in hopes he has more advice on what to do")
    print("Sam: Looks like you could use some more help. ")
    print("If you have gained all the letters back, you should consider heading towards the library. ")

# First Interaction with Zach
def zachTalk(self, player):
    # print("have him give useful information to the player in the form of a hint")

# Second Interaction with Zach
def zachTalk2(self, player):
    print("Hey! You look like you have found your sense of spelling again.")
    print("Before you leave you should really check out the Manga section here.")
    print("You might be surprised by what you find...")

# First Interaction with Sean
def seanTalk(self, player):
    print("You decide to approach Sean.")
    print("Nice to see you outside! Make sure to get some rest ig you are not feel good.")
    
# Second Interaction with Sean
def seanTalk2(self, player):
    # print("give a puzzle to obtain the bonus letter")


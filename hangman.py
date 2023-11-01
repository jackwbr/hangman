import random
begin = input("This is a basic two-player hangman game. Would you like to begin? Please enter 'yes' or 'no' ")
if begin == "no":
    print("Then why did you come here? ")

#REAL CODE STARTS BELOW

if begin == "yes":
    p1 = input("Great! Who is player 1? ")
    p2 = input("And who is player 2? ")

word = input("Okay, " + p1 + " and " + p2 + ", let's begin. " + p1 + ", please enter a word. ")
listword = list(word)
underword = list(word)
lenword = len(word)

z = len(word)

i = 0
while i < z:
    underword[i] = "_"
    i = i + 1
    
faillist = ["Nope, try again", "Sorry, try again", "FAIL, give it another shot", \
            "Imagine guessing the wrong answer. Give it another shot", "You're getting closer, try again", \
                '"Another one" - DJ Khaled']
lecontrol = 0

while lecontrol <= lenword:
    g1 = input("Okay, " + p2 + ", please guess a letter. ")
    if g1 in listword:
        print("Correct! " + g1 + " is in the word.")                  #This doesn't work, need to fix double letter words
        lecontrol = lecontrol + 1
    else:
        randomfail = random.choice(faillist)
        print(randomfail)

#CREATE A LIST FOR BLANK SPACES AND USE A FUCNTUIB TI REMOVE THINGS FROM THE MAIN LIST
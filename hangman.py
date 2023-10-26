begin = input("This is a basic two-player hangman game. Would you like to begin? Please enter 'yes' or 'no' ")
if begin == "no":
    print("Then why did you come here? ")

if begin == "yes":
    p1 = input("Great! Who is player 1? ")
    p2 = input("And who is player 2? ")

word = input("Okay, " + p1 + " and " + p2 + ", let's begin. " + p1 + ", please enter a word. ")
listword = list(word)

g1 = input("Okay, " + p2 + ", please guess a letter. ")
if g1 in listword:
    print("Correct! " + g1 + " is in the word.")


import random
def pick_random_char():
    string=input("enter a string")
    random_char=random.choice(string)
    print("Random character from your string", random_char)
pick_random_char()

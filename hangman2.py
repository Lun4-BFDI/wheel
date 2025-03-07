import sys
import random

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.free_play = False
        self.wild_card = False

    def __str__ (self):
        return self.name

    def display_score(self):
        print(self.score)

    def vowel_cost(self):
        self.score -= 250

    def wedge_store(self, wedge):
        self.wedge = wedge

class Letter:
    def __init__(self, letter):
        self.letter = letter
        self.revealed = True if letter == " " or letter == "!" or letter == "?" else False
        self.vowel = True if letter in ["A","E","I","O","U"] else False

    def __str__(self):
        return self.letter if self.revealed else "_"

class Wild:
    def __init__(self):
        self.picked_up = False



puzzle = "HAPPY BIRTHDAY!"
#puzzle_letters = [Letter("H"), Letter("A"), Letter("N"), Letter("G"), Letter("M"), Letter("A"), Letter("N")]
puzzle_letters = [Letter(letter) for letter in puzzle.upper()]
consonants = ["B","C","D","F","G","H","J","K","L","M","N","P","Q","R","S","T","V","W","X","Y","Z"]
vowels = ["A","E","I","O","U"]
playing = False
player_total = 0

def letter_call(guess):
    in_puzzle = False
    letter_total = 0
    for letter in puzzle_letters:
        if letter.revealed == True and letter.letter == guess:
            print("You already said that!")
        elif letter.letter == guess:
            letter.revealed = True
            in_puzzle = True
            print("Ding!")
            letter_total += 1
    if in_puzzle == False:
        print("Buzz!")
    print(" ".join(str(letter) for letter in puzzle_letters))
    revealed_count = int(0)
    for letter in puzzle_letters:
        if letter.revealed == True:
            revealed_count += 1
    if revealed_count == int(len(puzzle_letters)):
        print("You win!!!")
        sys.exit()
    else:
        return(letter_total)

def buy_vowel(guess):
    in_puzzle = False
    for letter in puzzle_letters:
        if letter.revealed == True and letter.letter == guess:
            print("You already said that!")
        elif letter.letter == guess:
            letter.revealed = True
            in_puzzle = True
            print("Ding!")
    if in_puzzle == False:
        print("Buzz!")
    print(" ".join(str(letter) for letter in puzzle_letters))
    revealed_count = int(0)
    for letter in puzzle_letters:
        if letter.revealed == True:
            revealed_count += 1
    if revealed_count == int(len(puzzle_letters)):
        print("You win!!!")
        sys.exit()

def FP_call(guess):
    in_puzzle = False
    letter_total = 0
    for letter in puzzle_letters:
        if letter.revealed == True and letter.letter == guess:
            print("You already said that!")
        elif letter.letter == guess:
            letter.revealed = True
            in_puzzle = True
            print("Ding!")
            letter_total += 1
    if in_puzzle == False:
        print("Buzz!")
    print(" ".join(str(letter) for letter in puzzle_letters))
    revealed_count = int(0)
    for letter in puzzle_letters:
        if letter.revealed == True:
            revealed_count += 1
    if revealed_count == int(len(puzzle_letters)):
        print("You win!!!")
        sys.exit()
    else:
        user.free_play = False
        return(letter_total)

def spin_wheel():
    wedge = random.randint(1,24)
    if wedge == 1:
        user.wedge_store(2500)
    if wedge == 2:
        user.wedge_store(500)
        if wild.picked_up == False:
            print("Pick up that Wild Card!")
            wild.picked_up = True
            user.wild_card = True
    if wedge == 3:
        user.wedge_store(600)
    if wedge == 4:
        user.wedge_store(700)
    if wedge == 5:
        user.wedge_store(600)
    if wedge == 6:
        user.wedge_store(650)
    if wedge == 7:
        user.wedge_store(500)
    if wedge == 8:
        user.wedge_store(700)
    if wedge == 9:
        user.wedge_store(0)
        print("Lose a turn!")
    if wedge == 10:
        user.wedge_store(600)
    if wedge == 11:
        user.wedge_store(550)
    if wedge == 12:
        user.wedge_store(500)
    if wedge == 13:
        user.wedge_store(600)
    if wedge == 14:
        user.wedge_store(0)
        print("Bankrupt!")
        user.score = 0
    if wedge == 15:
        user.wedge_store(650)
    if wedge == 16:
        user.wedge_store(500)
        user.free_play = True
    if wedge == 17:
        user.wedge_store(700)
    if wedge == 18:
        user.wedge_store(500)
    if wedge == 19:
        user.wedge_store(800)
    if wedge == 20:
        user.wedge_store(500)
    if wedge == 21:
        user.wedge_store(650)
    if wedge == 22:
        user.wedge_store(500)
    if wedge == 23:
        user.wedge_store(900)
    if wedge == 24:
        user.wedge_store(0)
        print("Bankrupt!")
        user.score = 0

user_name = input("Please enter your name: ")
user = Player(user_name)
playing = True
wild = Wild()
print(" ".join(str(letter) for letter in puzzle_letters))
while playing == True:
    print(user.score)
    user_type = input("Please enter SPIN, VOWEL, or SOLVE: ").upper()
    if user_type == "SPIN":
        spin_wheel()
        print(user.wedge)
        if user.wedge == 0:
            print("Spin again.")
        elif user.free_play == True:
            user_letter = input("Free Play! You can pick any letter. Vowels worth nothing, consonants worth $500 per letter. ")
            if user_letter in consonants:
                user.score += user.wedge * FP_call(user_letter)
            elif user_letter in vowels:
                FP_call(user_letter)
            else:
                print("Invalid letter!")
        else:
            user_letter = input("Please enter a letter: ").upper()
            if user_letter in consonants:
                user.score += user.wedge * letter_call(user_letter)
            else:
                print("Invalid letter!")
            if user.wild_card == True:
                using_wild = input("Would you like to use your Wild Card? Type Y or N: ")
                if using_wild == "Y":
                    user_letter = input("Please enter a letter: ").upper()
                    if user_letter in consonants:
                        user.score += user.wedge * letter_call(user_letter)
                        user.wild_card = False
                    else:
                        print("Invalid letter!")
                else:
                    pass
    if user_type == "VOWEL":
        user_vowel = input("Please enter a vowel: ")
        if user_vowel in vowels:
            if user.score >= 250:
                user.vowel_cost()
                buy_vowel(user_vowel)
            else:
                print("Sorry, you cannot buy a vowel now.")
        else:
            print("Invalid letter!")
    if user_type == "SOLVE":
        trytosolve = input("Please enter your solve: ").upper()
        if trytosolve == puzzle.upper():
            print(f"Congratulations, {user.name}! You win!!!")
            sys.exit()
        else:
            print("Sorry, your solve was wrong.")

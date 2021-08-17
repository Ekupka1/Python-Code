# Keynan Pearson & Ethan Kupka
# Programming Assignment 3
# CSC 140 Block 2, October 15, 2019

hand_initial = []
dhand = []
deck = []

def make_deck(deck):
    suit_init = ["Hearts", "Clubs", "Spades", "Diamonds"]
    faces = ["Jack of", "Queen of", "King of"]
    ace = [1, 11]
    for i in suit_init:
        for n in range (2, 11):
            card = [n , i]
            deck += [card]
        for k in faces:
            card = [10, k, i]
            deck += [card]
        for j in ace:
            card = [j, "Ace of", i]
            deck += [card]
    return deck

wins = {"DEALER":0, "PLAYER_1":0}
points = {"DEALER":1500, "PLAYER_1":500}
bet = {"DEALER":0, "PLAYER_1":0}

import random

def start(ans):
    if ans == "y" or ans == "Y":
        getbet()
        make_deck(deck)
        drawcard(dhand, deck)
        print('')
        print('DEALER HAND:')
        print(dhand, count_total(dhand))
        print('DEALER TOTAL: <', count_total(dhand),'>')

        starthand()
        hit(hand_initial)
    elif ans == "n" or ans == "N":
        end_game()
    else:
        ans = input("Invalid input, try again: ")
        start(ans)

def getbet(): #Lets the player determine their bet
    print("")
    print("Remaining points: ", points["PLAYER_1"])
    print('')
    betans = input("PLACE YOUR BET: ")
    try:
        if int(betans) <= points["PLAYER_1"]:
            bet["PLAYER_1"] = int(betans)

        elif int(betans) > points["PLAYER_1"]:
            print("YOU ARE GONNA NEED ANOTHER JOB IF YOU LOSE THAT")
            getbet()

    except ValueError:
        print("")
        print("TRY PUTTING IN A NUMBER THIS TIME")
        getbet()

    return bet["PLAYER_1"]

def starthand():
    while len(hand_initial) <= 1:
        drawcard(hand_initial, deck)
    print("")
    print("PLAYER 1 HAND:")
    print(hand_initial)
    print('PLAYER 1 TOTAL: <', count_total(hand_initial),'>')
    return hand_initial

def hit(ahand):
    print("")
    print('-----------------------------------------------')
    ans = input("HIT OR STAY: ")
    while ans != 'STAY':
        drawcard(ahand, deck)
        print("")
        print("PLAYER 1 HAND:")
        print(ahand)
        print('PLAYER 1 TOTAL: <', count_total(hand_initial),'>')
        if count_total(ahand) <= 21:
            print("")
            ans = input("HIT OR STAY: ")
        elif count_total(ahand) > 21:
            ans = 'STAY'
        print('-----------------------------------------------')
    dealer()


def dealer():
    if count_total(hand_initial) > 21:
        print("")
        print("PLAYER 1 BUST!")
        game_won("DEALER")
        check_game()

    else:
        print("")
        print("DEALER HAND:")
        get_dealerhand(dhand)
        if count_total(dhand) > count_total(hand_initial) and count_total(dhand) <= 21:
            game_won("DEALER")
            check_game()
        elif count_total(dhand) > 21:
            print("")
            print("DEALER BUST!")
            game_won("PLAYER_1")
            check_game()
        elif count_total(dhand) == count_total(hand_initial):
            print("")
            print("PUSH, SCORE REMAINS THE SAME")
            print(wins)
            print(points)
            check_game()

def check_game():
        if points['PLAYER_1'] == 0:
            print("")
            print("PLAYER 1 LOSES; OUT OF POINTS")
            end_game()
        elif points['DEALER'] == 0:
            print("")
            print("PLAYER_1 WINS!!!; DEALER OUT OF POINTS")
            end_game()
        else:
            intro()

def game_won(who):
    if who == 'DEALER':
        print("")
        print("DEALER WINS")
        wins['DEALER'] += 1
        points['PLAYER_1'] -= bet["PLAYER_1"]
        points['DEALER'] += bet["PLAYER_1"]

    elif who == 'PLAYER_1':
        print("")
        print("PLAYER ONE WINS!")
        wins["PLAYER_1"] += 1
        points['PLAYER_1'] += bet["PLAYER_1"]
        points['DEALER'] -= bet["PLAYER_1"]
    print(wins)
    print(points)

def get_dealerhand(dhand):
    drawcard(dhand, deck)
    print(dhand)
    print('DEALER TOTAL: <', count_total(dhand),'>')

    while count_total(dhand) < 17 or count_total(dhand) < count_total(hand_initial):
        drawcard(dhand, deck)
    print('')
    print("DEALER HAND:")
    print(dhand)
    print('DEALER TOTAL: <', count_total(dhand),'>')

def count_total(hand):
    total = 0
    for n in range(len(hand)):
        total = total + (hand[n][0])
    return total

def drawcard(hand, deck):
    length = len(deck)
    order = random.randrange(length)
    card = deck[order]
    junk_pile(card, deck)
    hand += [card]
    return hand

'''def drawcard(n, hand, deck):
    for i in range(n):
        suit = get_suit()
        number = random.randrange(2, 16)

        if number > 10 and number != 15:
            face = get_face()
            number = 10
            card = [number, face, suit]
            junk_pile(card, deck)
            hand += [card]

        elif number == 15:
            if hand is hand_initial:
                print("")
                print("PLAYER 1 HAND:")
                print(hand)
                print('PLAYER 1 TOTAL: <', count_total(hand_initial),'>')
                print('')
                print('-----------------------------------------------')
                number = int(input("ACE HIGH OR LOW (1 or 11?):" ))

            elif hand is dhand:
                if count_total(hand) + 11 <= 21:
                    number = 11
                else:
                    number = 1

            suit = get_suit()
            card = [number, 'Ace of', suit]
            junk_pile(card, deck)
            hand += [card]

        else:
            card = [number, suit]
            junk_pile(card, deck)
            hand += [card]'''

def get_suit():
    suit = random.randrange(4)
    if suit == 0:
        suit = "Clubs"
    elif suit == 1:
        suit = "Hearts"
    elif suit == 2:
            suit = "Spades"
    elif suit == 3:
        suit = "Diamonds"
    return suit

def get_face():
    face = random.randrange(1,4) # could be 10, jack, queen or king
    if face == 1:
        face = 'Jack of'
    elif face == 2:
        face = 'Queen of'
    elif face == 3:
        face = 'King of'
    return face

def junk_pile(card, deck): #this is the check to see if a card is used
    if card in deck:
        del deck[deck.index(card)]
    else:
        drawcard(hand, deck)
    if len(deck) == 0:
        make_deck()
        print('')
        print("OUT OF CARDS, SHUFFLING DECK...")
    return deck

def reset_hand():
    del hand_initial[:]
    del dhand[:]

def end_game():
    print("")
    print("See ya later aligata'")

def intro():
    print('')
    reset_hand()
    print('')
    print('-----------------------------------------------')
    start(input("WOULD YOU LIKE TO PLAY AGAIN? Y / N: "))

print("Hello and Welcome to Keynan and Ethan's Project #3!")
print("")
start(input("WOULD YOU LIKE TO PLAY BLACKJACK? Y / N: "))

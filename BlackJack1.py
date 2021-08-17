# Keynan Pearson & Ethan Kupka
# Programming Assignment 3
# CSC 140 Block 2, October 15, 2019

hand_initial = []
dhand = []
cards_used = []

wins = {"DEALER":0, "PLAYER_1":0}
points = {"DEALER":500, "PLAYER_1":500}
bet = {"DEALER":0, "PLAYER_1":0}

# start function, prints first response
import random
def start(ans):
    if ans == "y" or ans == "Y":
        getbet()
        drawcard(1, dhand, cards_used)
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
        #end of start function

# function for getting, Lets the player determine their bet
def getbet():
    print("")
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
    #end of getbet function

# function starthand, prints players hand and count of hand for the round
def starthand():
    drawcard(2, hand_initial, cards_used)
    print("")
    print("PLAYER 1 HAND:")
    print(hand_initial)
    print('PLAYER 1 TOTAL: <', count_total(hand_initial),'>')
    return hand_initial
    #end of starthand function

# function hit, if the player wants another card
def hit(ahand):
    print("")
    ans = input("HIT OR STAY: ")
    while ans != 'stay':
        drawcard(1, ahand, cards_used)
        print("")
        print("PLAYER 1 HAND:")
        print(ahand)
        print('PLAYER 1 TOTAL: <', count_total(hand_initial),'>')
        if count_total(ahand) <= 21:
            print("")
            ans = input("HIT OR STAY: ")
        elif count_total(ahand) > 21:
            ans = 'stay'
    dealer()
    #end of hit function

# function dealer, if the dealer goes over or hits again
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
            #end of dealer function


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
    drawcard(1, dhand, cards_used)
    print(dhand)
    print('DEALER TOTAL: <', count_total(dhand),'>')

    while count_total(dhand) < 17 or count_total(dhand) < count_total(hand_initial):
        drawcard(1, dhand, cards_used)
    print('')
    print("DEALER HAND:")
    print(dhand)
    print('DEALER TOTAL: <', count_total(dhand),'>')

def count_total(hand):
    total = 0
    for n in range(len(hand)):
        total = total + (hand[n][0])
    return total

def drawcard(n, hand, cards_used):
    for i in range(n):
        suit = get_suit()
        number = random.randrange(1, 16)

        if number > 10 and number != 15:
            face = get_face()
            number = 10
            card = [number, face, suit]
            junk_pile(card, cards_used)
            hand += [card]

        elif number == 15:
            if hand is hand_initial:
                print("")
                print("PLAYER 1 HAND:")
                print(hand)
                print('PLAYER 1 TOTAL: <', count_total(hand_initial),'>')
                print('')
                number = int(input("ACE HIGH OR LOW (1 or 11?):" ))

            elif hand is dhand:
                if count_total(hand) + 11 <= 21:
                    number = 11
                else:
                    number = 1

            suit = get_suit()
            card = [number, 'Ace of', suit]
            junk_pile(card, cards_used)
            hand += [card]

        else:
            card = [number, suit]
            junk_pile(card, cards_used)
            hand += [card]

# funtion get_suit, gets suit for card
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
    #end of get_suit

# function get_face, gets face for card
def get_face():
    face = random.randrange(1,4) # could be 10, jack, queen or king
    if face == 1:
        face = 'Jack of'
    elif face == 2:
        face = 'Queen of'
    elif face == 3:
        face = 'King of'
    return face
    #end of get_face

# function junk_pile, trash card pile so cards aren't re-used till deck is out
def junk_pile(card, cards_used): #this is the check to see if a card is used
    cards_used += [card]
    if len(cards_used) >= 54:
        print('')
        print("OUT OF CARDS, SHUFFLING DECK...")
        del cards_used[:]
    return cards_used
    #end of junk_pile

#
def reset_hand():
    del hand_initial[:]
    del dhand[:]

# said at the end
def end_game():
    print("")
    print("See ya later Aligata'")

# stats of the game
def intro():
    print('')
    reset_hand()
    print("CARDS USED: ", cards_used)
    print('')
    start(input("WOULD YOU LIKE TO PLAY AGAIN? Y / N: "))

#Intro
print("Hello and Welcome to Keynan and Ethan's Project #3!")
print("")
print("Respond in all CAPS!")
print("")
print("Your starting points are:", points)
print("")
start(input("WOULD YOU LIKE TO PLAY BLACKJACK? Y / N: "))

#End of Code
